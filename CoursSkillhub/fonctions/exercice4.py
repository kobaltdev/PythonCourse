""" 
Exercice 4 : Analyse des résultats d'un sondage
Scénario :
Tu es responsable d'un sondage sur les films de science-fiction préférés. 
Écris une fonction qui prend un dictionnaire de votes et retourne le film avec le plus de votes.
"""

def film_favori(votes):
    # initialiser avec la premiere entrée du dico qui devient la meilleure note
    meilleur_film = next(iter(votes))

    # itération dans le dico
    for cle in votes:
        #On compare la clé courante avec la meilleure, devient la meilleure si plus grande
        if votes[cle] > votes[meilleur_film]:
            meilleur_film = cle
    # affichage résultat
    print(f"Meilleur film : {meilleur_film}")



sondage = {"Star Wars": 100,
            "Star Trek": 150, 
            "Matrix": 190
            }

film_favori(sondage)

