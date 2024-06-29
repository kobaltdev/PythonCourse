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

# Get current working dir
cwd = os.getcwd()
# contruction du chemin de fichier complet
file_to_compute = os.path.join(cwd, "base_resources.json")
print(file_to_compute)


def show_resources_from_json(json_resources):
    # ouverture du fichier et import json
    with open(json_resources, 'r') as fichier:
        resources_dict = json.load(fichier)
    print(resources_dict)
    print("Niveau de ressources actuel :")
    [print(v) for v in resources_dict.values()]



def manage_base_resources(file_path):
    pass

# Appel de la fonction


show_resources_from_json(file_to_compute)

manage_base_resources('base_resources.json')
