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


# Path du dossier de travail
directory = os.path.dirname(__file__)
# contruction du chemin de fichier complet
file_to_compute = os.path.join(directory, "base_resources.json")
# print(file_to_compute)


def show_resources_from_json(json_resources):
    # ouverture du fichier et import json
    with open(json_resources, 'r') as fichier:
        extracted_dict_from_json = json.load(fichier)
    # affichage du resultat
    print(extracted_dict_from_json)
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
                print("Valeur mise à jour")
                print("------------------")
                return answer
            else:
                print("Merci de saisir une valeur supérieure au stock actuel")
        except ValueError:
            print("Merci de saisir un nombre valide")


def show_and_fix_resources(resources_cur, exp_resources):
    print("GESTION DES RESSOURCES")
    print("* * * * * * * * * * * ")
    # print("Niveau de ressources attendu :")
    # # boucle de lecture du contenu :
    # for k in expected_resources.keys():
    #     print(k, expected_resources[k])
    # print("-----------------------------")
    # print("Niveau de ressources actuel :")
    print()
    # boucle de lecture du contenu : 
    for k in resources_cur.keys():
        print(k)

        if resources_cur[k] < expected_resources[k]:
            print(k, resources_cur[k], "- INSUFFISANT")
            print()
            print("Correction requise !!")
            print()
            time.sleep(1)
            new_value = input_new_value(resources_cur[k])
            resources_cur.update({k:new_value})
        else:
            print(k, resources_cur[k], "- OK")
            time.sleep(1)
            print()
    print("Nouvelles valeurs pour les ressources :")
    for k in resources_cur.keys():
        print(k, resources_cur[k])




resources_current = show_resources_from_json(file_to_compute)
show_and_fix_resources(resources_current, expected_resources)