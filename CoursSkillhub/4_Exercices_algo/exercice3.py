"""
Exercice 3 : Gestion des ressources d'une base (Fichiers, JSON, Boucles, Structures conditionnelles)

Scénario : Tu dois gérer les ressources d'une base martienne en lisant les données d'un fichier JSON
et en décidant des actions à entreprendre.

    - Lis les données des ressources depuis le fichier JSON base_resources.json.
    - Vérifie les niveaux des ressources.
    - Si une ressource est en dessous d'un certain seuil (100 pour l'eau, 200 pour la nourriture, 150 pour l'énergie),
         demande à l'utilisateur de saisir une nouvelle valeur pour cette ressource via une entrée clavier.
    - Met à jour les valeurs des ressources dans le fichier JSON avec les nouvelles valeurs saisies.
    - Affiche les actions entreprises et confirme la mise à jour des ressources dans le fichier JSON.

Fichier associé : base_resources.json
"""

import json
import os
import time

# Constantes
MIN_WATER = 100
MIN_FOOD = 200
MIN_ENERGY = 150
expected_resources ={'eau': MIN_WATER, 
                     'nourriture': MIN_FOOD, 
                     'energie': MIN_ENERGY}



def set_file_path(filename):
    # Path du dossier de travail
    directory = os.path.dirname(__file__)
    # contruction du chemin de fichier complet
    file_to_compute = os.path.join(directory, filename)
    return file_to_compute


def get_resources_from_json(json_file):
    # ouverture du fichier et import json
    with open(json_file, 'r') as fichier:
        extracted_dict_from_json = json.load(fichier)
    # creation d'un nouveau dico pour les donnees ressources nested
    resources_dict = extracted_dict_from_json['ressources']
    return resources_dict


def input_new_value(ref_value):
    while True:
        try:
            print(f"Ancienne valeur : {ref_value}")
            answer = int(input("Saisir une nouvelle valeur pour la ressource : "))
            if answer > ref_value:
                print()
                print("-> Valeur mise à jour")
                print("------------------")
                print()
                time.sleep(1)
                return answer
            else:
                print("Merci de saisir une valeur supérieure au stock actuel")
        except ValueError:
            print("Merci de saisir un nombre valide")


def show_and_fix_resources(resources_cur, exp_resources):
    enough_resources = True
    print("* * * * * * * * * * * ")
    print("GESTION DES RESSOURCES")
    print("* * * * * * * * * * * ")
    print()
    print("Verification des ressources en cours ...")
    print()
    time.sleep(2)
    # boucle de lecture du contenu : 
    for k in resources_cur.keys():
        print(f"- {k.upper()}")
        print(f"Attendu : {exp_resources[k]}")
        if resources_cur[k] < expected_resources[k]:
            enough_resources = False
            print("En stock : ", resources_cur[k], "- INSUFFISANT")
            print()
            print("Correction requise !!")
            print()
            time.sleep(1)
            new_value = input_new_value(resources_cur[k])
            # update dictionnaire avec la nouvelle valeur retournee
            resources_cur.update({k:new_value})
        else:
            print("En stock : ", resources_cur[k], "- OK")
            time.sleep(1)
            print()
    print("Nouvelles valeurs pour les ressources :")
    for k in resources_cur.keys():
        print(k.upper(), "=", resources_cur[k])
    print("---------------------------------------")
    print()
    if not enough_resources:
        show_and_fix_resources(resources_cur, exp_resources)


def update_newressources_to_json(dict_name, filename_to_upload):
    # construction du nouveau dictionnaire avec la meme structure que le json
    dict_updated = {"ressources": {}}
    dict_updated["ressources"] = dict_name
    # generation du json à partir du dictionnaire
    json_file = json.dumps(dict_updated)
    # generation du path pour le fichier json
    json_absolute_path = set_file_path(filename_to_upload)

    print("- Mise a jour du nouveau fichier de ressources -")
    print()
    
    # verifier si le fichier existe deja et le supprimer le cas échéant
    if os.path.exists(json_absolute_path):
        print(f"Le fichier {filename_to_upload} existe déjà, suppression en cours")
        time.sleep(1)
        os.remove(json_absolute_path)
        print("Fichier supprimé !")

    # upload du nouveau fichier de ressources
    with open(json_absolute_path, 'w') as file:
        print()
        print("Ecriture du nouveau fichier de ressources...")
        print(f"Chemin du fichier : {json_absolute_path}")
        time.sleep(1)
        file.write(json_file)
        print("OK !")
        print()
        


##########################
#          MAIN          #
##########################

file_to_compute = set_file_path("base_resources.json")
resources_current = get_resources_from_json(file_to_compute)
show_and_fix_resources(resources_current, expected_resources)
update_newressources_to_json(expected_resources, "updated_resources.json")
