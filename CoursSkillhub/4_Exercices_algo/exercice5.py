"""
Exercice 5: Les robots dans la base spatiale

Scénario :
Bienvenue à la base spatiale "Galactica".
Ta mission est de mettre à jour les informations des robots de la base dans un fichier JSON.

Fichier associé : robots.json
"""

import json
import os


#####################
# FONCTIONS
#####################

def set_file_path(filename):
    # Path du dossier de travail
    directory = os.path.dirname(__file__)
    # contruction du chemin de fichier complet
    file_to_compute = os.path.join(directory, filename)
    print(file_to_compute)
    return file_to_compute


def update_robot_status(json_to_update, robot_id, new_status):
    # ouverture du fichier et import json
    with open(json_to_update, 'r') as fichier:
        data = json.load(fichier)
    # affichage du contenu du fichier
    print("Avant modification : ")
    for d in data:
        print(d)
    # maj de la cle status
    data[robot_id-1]['status'] = new_status
    # affichage du json modifié
    print("Après modification : ")
    for d in data:
        print(d)
    # mise à jour du fichier json
    with open(json_to_update, 'w') as fichier:
        json.dump(data, fichier, indent=4)
    


#####################
# MAIN
#####################

json_to_update = set_file_path("robots.json")
update_robot_status(json_to_update, 3, 'active')