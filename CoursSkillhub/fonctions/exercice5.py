""" 
Exercice 5 : Conversion de coordonnées galactiques
Scénario :
Dans l'univers de la science-fiction, les coordonnées galactiques sont souvent exprimées en tuples. 
Écris une fonction qui convertit une liste de coordonnées tuples en une liste de chaînes de caractères.
"""

def conversion_coordonnees(coord):
    # liste de tuples, donc on va parcourir chaque tuple a la suite
    for tup in coord:
        s = ""   # initialise un chaine vide
        for i in range(len(tup)):
            s += str(tup[i])    # on incremente chaque element a la chaine
        print(f"Coordonnees : {s}")


coordonnees = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

conversion_coordonnees(coordonnees)