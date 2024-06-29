"""
Exercice 2 : Calcul de la moyenne des scores (JSON)

Scénario : Tu es en charge de calculer la moyenne des scores des participants à un tournoi de jeux vidéo.

Fichier associé : scores.json
"""

import json
import os

# Get current working dir
cwd = os.getcwd()

# contruction du chemin de fichier complet
file_to_compute = os.path.join(cwd, "scores.json")
print(file_to_compute)


def import_scores_from_json(file):
    # ouverture du fichier et import json
    with open(file, 'r') as fichier:
        dico = json.load(fichier)
    # print du dico obtenu
    print(dico)
    # Creation de la liste de score vide
    scores = []
    # Parcours des elements du dico
    for e in dico["players"]:
        print(f"Score de {e["name"]} : {e["score"]}")
        # Ajout de chaque score a la liste
        scores.append(e["score"])
    return scores


def calculate_average_score(liste_scores):
    somme_scores = sum(liste_scores)
    # moyenne absolue
    moyenne = somme_scores / len(liste_scores)
    # moyenne arrondie
    moyenne_arrondie = round(moyenne)
    print("La moyenne des scores est donc de", moyenne_arrondie, "points")


s = import_scores_from_json(file_to_compute)
calculate_average_score(s)
