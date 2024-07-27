import sqlite3
import os
import time


#################
# SQL Requests
#################


sql_request_create_datas = """CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);

    CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY,
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    annee_sortie INTEGER);

    INSERT INTO artiste (nom) VALUES ("Michael Jackson");
    INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (1, "Thriller", 1983);

    INSERT INTO artiste (nom) VALUES ("Celine Dion");
    INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (2, "Falling into You", 1996);
    INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (2, "Let's Talk About Love", 1997);
"""

#################
# FONCTIONS
#################

# set Working dir
def set_db_file(filename):
    # Path du dossier de travail
    directory = os.path.dirname(__file__)
    # contruction du chemin de fichier complet
    file_to_compute = os.path.join(directory, filename)
    return file_to_compute

# fonction de clear screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def show_choices(filename_short, filename_full, sql_creation_script):
    print("Saisissez une commande : \n")
    print(f" - taper 1  : Supprimer le fichier {filename_short}")
    print(" - taper 2  : Vider toutes les tables de la DB")
    print(" - taper 3  : Générer le contenu de la DB")
    print(" - taper 4  : Afficher le contenu de la DB")
    print(" - taper Q  : Quitter le programme")
    print()
    answer = input("Votre choix ? = ")
    answer_lower = answer.lower()
    print()
    match answer_lower:
        case "1":
            cls()
            delete_existing_file(filename_full)
        case "2":
            cls()
            empty_existing_db(filename_full)
        case "3":
            cls()
            build_db_entries(filename_full, sql_creation_script)
        case "4":
            cls()
            print_db_content(filename_full)
        case "q":
            print("Bye !")
            quit()
        case _:
            print("Saisissez un choix valide !\n")
            time.sleep(2)
            cls()


def delete_existing_file(filename):
    try:
        os.remove(filename)
        print("Ok, fichier supprimé! \n")
    except FileNotFoundError as e:
        print()
        print(e)
        print("Le fichier n'existe pas !\n")


def empty_existing_db(db_name):

    if os.path.exists(db_name):
        try: 
            get_sql_tables = "SELECT name FROM sqlite_schema WHERE type='table';"
                
            connection = sqlite3.connect(db_name)
            print("Connected to SQLite DB !")
            cursor = connection.cursor()

            cursor.execute(get_sql_tables)
            tables = cursor.fetchall()
            print("Liste des tables à supprimer : ")
            print(tables)
            for i in range(len(tables)):
                # la variable pour accéder au nom de la table ici (voir avec le debugger)
                cursor.execute(f"DROP TABLE {tables[i][0]};")

            print("Ok, toutes les tables de la DB ont été vidées !\n")
        
        except sqlite3.Error as error:
            print("Erreur : " + error)
        
        finally:
            connection.commit()
            connection.close()
    
    else:
        print("Le fichier n'existe pas, action non effectuée !\n")


def build_db_entries(filename, sqlscript):
    
    try:
        # ouverture de la connexion
        connection = sqlite3.connect(filename)
        print("Connected to SQLite !\n")
        print("Execution du script SQL de création !")
        # creation du curseur
        cursor = connection.cursor()

        # execution de la requete
        cursor.executescript(sqlscript)
        connection.commit()

    except sqlite3.Error as error:
        print("Erreur :", error)

    finally:
       if connection:
           connection.close()
           print("La DB et ses entrées sont créées !\n")
           print("Connexion à la DB fermée")

def print_db_content(dbname):

    get_sql_tables = "SELECT name FROM sqlite_schema WHERE type='table';"

    if os.path.exists(dbname):
        try: 
            connection = sqlite3.connect(dbname)
            print("Connected to SQLite !\n")
            cursor = connection.cursor()
            cursor.execute(get_sql_tables)
            # récupération des tables
            tables = cursor.fetchall()
            print("Contenu de la DB : \n")

            for i in range(len(tables)):
                print(f"Table : {tables[i]}\n")
                for v in cursor.execute(f'SELECT * FROM {tables[i][0]}'):
                    print(v)
                print()
        
        except sqlite3.Error as error:
            print("Erreur :", error)

        finally:
            if connection:
                connection.close()
    else:
        print("Le fichier n'existe pas ou son contenu est vide !\n")


#################
# MAIN
#################


db_file_name = "albums.db"

full_path_db_file = set_db_file(db_file_name)

while True:
    show_choices(db_file_name, full_path_db_file, sql_request_create_datas)
    