# Corrigé exercice 1

def compte_a_rebours():
    for i in range(10, 0, -1):
        print(i)
    print("Impact imminent !")

compte_a_rebours()

# Corrigé exercice 2

def calcul_score(taches, points):
    total = 0
    for point in points:
        total += point
    return total

taches = ["mission1", "mission2", "mission3"]
points = [10, 20, 30]

print(calcul_score(taches, points))

# Corrigé exercice 3

def filtre_suspects(suspects, alibis):
    return [suspect for suspect in suspects if suspect not in alibis]

suspects = ["Alice", "Bob", "Charlie", "David"]
alibis = ["Bob", "David"]

print(filtre_suspects(suspects, alibis))

# Corrigé exercice 4

def film_favori(votes):
    return max(votes, key=votes.get)

votes = {"Star Wars": 100, "Star Trek": 150, "Matrix": 90}

print(film_favori(votes))

# Corrigé exercice 5

def conversion_coordonnees(coordonnees):
    return [f"({x}, {y}, {z})" for x, y, z in coordonnees]

coordonnees = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

print(conversion_coordonnees(coordonnees))

# Corrigé exercice 6

def verification_codes(codes):
    return [len(code) == 6 and code.isdigit() for code in codes]

codes = ["123456", "abcdef", "1234", "789101", "654321"]

print(verification_codes(codes))

# Corrigé Workshop

def generateur_quete(*personnages, **details):
    quetes = []
    for personnage in personnages:
        quetes.append(f"{personnage} doit {details['objectif']} à {details['lieu']}.")
    return quetes

personnages = ["Arthur", "Merlin"]
details = {
    "lieu": "la forêt de Brocéliande",
    "objectif": "trouver l'épée magique"
}

print(generateur_quete(*personnages, **details))