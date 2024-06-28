""" 
Exercice 3 : Filtre de données dans une enquête policière
Scénario :
Dans une enquête policière, tu dois filtrer les suspects qui ont un alibi. 
Écris une fonction qui prend une liste de suspects et une liste de ceux qui ont un alibi, 
et retourne une liste de suspects sans alibi.
"""

def filtre_suspects(liste_suspects, liste_alibis):
    suspects_sans_alibis = []
    for suspect in liste_suspects:
        if suspect not in liste_alibis:
            suspects_sans_alibis.append(suspect)
    return suspects_sans_alibis



suspects = ["Alice", "Bob", "Charlie", "David", "Thomas"]
alibis = ["Bob", "David"]

liste_suspects_sans_alibis = filtre_suspects(suspects, alibis)
print("Liste des suspects sans alibi :")
print(liste_suspects_sans_alibis)
