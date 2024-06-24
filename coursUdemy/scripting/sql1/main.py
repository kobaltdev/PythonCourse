import sqlite3
import os

# Get the current working directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

fichier_db = "/home/jc/PythonCourse/coursUdemy/scripting/sql1/album.db"


# Creation de la requete
req_create = """CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);"""

req_delete = """DROP TABLE artiste;"""

# ouverture connexion ET creation du curseur
connection = sqlite3.connect(fichier_db)
cursor = connection.cursor()

try:
    # Execution de la requete
    cursor.execute(req_create)
except sqlite3.OperationalError:
    print("Erreur la table existe déjà")
    while True:
        reponse = input("Supprimer la table existante ? (y / n) : ")
        match reponse:
            case "y":
                cursor.execute(req_delete)
                break
            case "n":
                exit()
            case _:
                print("Saisir 'y' ou 'n'")

# Commit de la requete
connection.commit()

# Affichage de la table
try:
    with sqlite3.connect(fichier_db) as conn:
        # lire data
        req = "SELECT * FROM artiste"
        cursor.execute(req)

        # fetch des colonnes
        rows = cursor.fetchall()

        # Affichage
        for row in rows:
            print(row)

except sqlite3.Error as e:
    print(e)
finally:
    # Fermeture de la requête
    connection.close()
