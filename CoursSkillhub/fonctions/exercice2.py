""" 
Exercice 2 : Calcul des scores de jeu
Scénario :
Dans un jeu de société futuriste, les joueurs accumulent des points en fonction des tâches 
qu'ils accomplissent. 
Chaque tâche rapporte des points différents. Écris une fonction qui calcule le score total 
d'un joueur.
"""

def calcul_score(taches, points):
    for i in range(len(taches)):
        print(f"Mission {i+1} : le score est de {points[i]}")
    score = sum(points)
    print(f"Score total : {score} points")

taches = ["mission1", "mission2", "mission3"]
points = [10, 20, 30]

calcul_score(taches, points)

