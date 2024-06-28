""" 
Exercice 1 : Décodage de message alien

Scénario : Tu as intercepté un message en provenance d'une civilisation extraterrestre. Malheureusement, il est encodé dans un fichier JSON.

Fichier à traiter : alien_message.json
"""
import json
import base64

# Charge le fichier JSON


# Décode le message


print(decoded_message)

""" 
Exercice 2 : Calcul de la moyenne des scores (JSON)

Scénario : Tu es en charge de calculer la moyenne des scores des participants à un tournoi de jeux vidéo.

Fichier associé : scores.json
"""

import json

def calculate_average_score(file_path):
    # Ton code ici

# Appel de la fonction
calculate_average_score('scores.json')

""" 
Exercice 3 : Gestion des ressources d'une base (Fichiers, JSON, Boucles, Structures conditionnelles)

Scénario : Tu dois gérer les ressources d'une base martienne en lisant les données d'un fichier JSON et en décidant des actions à entreprendre.

    - Lis les données des ressources depuis le fichier JSON base_resources.json.
    - Vérifie les niveaux des ressources.
    - Si une ressource est en dessous d'un certain seuil (100 pour l'eau, 200 pour la nourriture, 150 pour l'énergie), demande à l'utilisateur de saisir une nouvelle valeur pour cette ressource via une entrée clavier.
    - Met à jour les valeurs des ressources dans le fichier JSON avec les nouvelles valeurs saisies.
    - Affiche les actions entreprises et confirme la mise à jour des ressources dans le fichier JSON.

Fichier associé : base_resources.json
"""

import json

def manage_base_resources(file_path):
    # Ton code ici

# Appel de la fonction
manage_base_resources('base_resources.json')


""" 
Exercice 4 : Répertoire des films de science-fiction

Scénario :
Tu es responsable de la gestion d'une vidéothèque spécialisée en films de science-fiction. Un fichier movies.txt contient la liste des films avec l'année de sortie. Tu dois extraire et afficher les films sortis après l'année 2000.

Fichier associé : movies.txt
"""
# Lecture du répertoire des films
with open('movies.txt', 'r') as file:
    movies = file.readlines()

# Extraction des films après l'année 2000
recent_movies = []

# Ton code ici

print("Films sortis après 2000:")
for movie in recent_movies:
    print(movie)

""" 
Exercice 5: Les robots dans la base spatiale

Scénario :
Bienvenue à la base spatiale "Galactica". Ta mission est de mettre à jour les informations des robots de la base dans un fichier JSON.

Fichier associé : robots.json
"""

import json

def update_robot_status(file_path, robot_id, new_status):
    # Ton code ici

update_robot_status('robots.json', 3, 'active')

""" 
Exercice 6: Les composants de la machine à voyager dans le temps

Scénario :
Tu dois mettre à jour la liste des composants nécessaires pour réparer la machine à voyager dans le temps.

Fichier associé : components.json
"""

import json

def update_component_quantity(file_path, component_name, new_quantity):
    # Ton code ici

update_component_quantity('components.json', 'Plutonium', 5)
