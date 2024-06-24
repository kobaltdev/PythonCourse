"""
noms = []
while True:
    nom = input("Saisissez le nom à ajouter : ")
    if nom == "":
        print("Fin de la saisie")
        break
    else:
        noms.append(nom)
for i in noms:
    print(i)
"""

noms = ["paul", "marc", "jean", "alice", "robert", "toto", "jc"]
valeurs = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]


def plus_petite_distance(liste_nom, liste_distance):
    mini = liste_distance[0]
    index_mini = 0
    for i in liste_distance:
        if i < mini:
            mini = i
            index_mini = liste_distance.index(i)
    chauffeur_le_plus_proche = liste_nom[index_mini]
    return mini, chauffeur_le_plus_proche


distance_min, chauffeur = plus_petite_distance(noms, valeurs)
print(f"La valeur la plus petite est {distance_min} km, le chauffeur associé est {chauffeur}")

