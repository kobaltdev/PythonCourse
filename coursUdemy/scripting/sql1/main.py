import sqlite3
import os


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

sql_req_delete = """DROP TABLE artiste;"""

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

# Check si fichier existe + actions le cas echeant
def check_file_before_action(filename):

    if os.path.exists(filename):
        print(f"Le fichier {filename} existe, que voulez vous faire ? : \n")
        print(f"Supprimer le fichier : taper 1")
        print(f"Vider toutes les tables du fichier : taper 2")
        while True:
            answer = input("Votre Choix ? = ")
            match answer:
                case "1":
                    os.remove(filename)
                    print("Ok, la DB a été supprimée !")
                    break
                case "2":
                    empty_existing_db(filename)
                    print("Ok, toutes les tables de la DB ont été vidées !\n")
                    break
                case _:
                    print("Saisissez un choix valide !")

    else:
        print(f"Le fichier {filename} n'existe pas, OK !")
        

def empty_existing_db(db_name):
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

    connection.commit()
    connection.close()


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


#################
# MAIN
#################


fichier_db = set_db_file("albums.db")
check_file_before_action(fichier_db)
build_db_entries(fichier_db, sql_request_create_datas)