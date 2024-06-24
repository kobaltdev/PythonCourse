# Exemples de Slicing
# Slicing sur une Liste

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extraire les éléments de l'indice 2 à 5 (5 exclus)
sous_liste = liste[2:5]
print(sous_liste)  # Affichera : [2, 3, 4]

# Extraire les éléments du début jusqu'à l'indice 4 (4 exclus)
sous_liste = liste[:4]
print(sous_liste)  # Affichera : [0, 1, 2, 3]

# Extraire les éléments de l'indice 6 jusqu'à la fin
sous_liste = liste[6:]
print(sous_liste)  # Affichera : [6, 7, 8, 9]

# Extraire tous les éléments avec un pas de 2
sous_liste = liste[::2]
print(sous_liste)  # Affichera : [0, 2, 4, 6, 8]

# Extraire les éléments dans l'ordre inverse
sous_liste = liste[::-1]
print(sous_liste)  # Affichera : [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Slicing sur une Chaîne de Caractères

chaine = "Bonjour le monde"

# Extraire les caractères de l'indice 8 à 10 (10 exclus)
sous_chaine = chaine[8:10]
print(sous_chaine)  # Affichera : "le"

# Extraire les caractères du début jusqu'à l'indice 7 (7 exclus)
sous_chaine = chaine[:7]
print(sous_chaine)  # Affichera : "Bonjour"

# Extraire les caractères de l'indice 11 jusqu'à la fin
sous_chaine = chaine[11:]
print(sous_chaine)  # Affichera : "monde"

# Extraire tous les caractères avec un pas de 3
sous_chaine = chaine[::3]
print(sous_chaine)  # Affichera : "Boeoe"

# Extraire les caractères dans l'ordre inverse
sous_chaine = chaine[::-1]
print(sous_chaine)  # Affichera : "ednom el ruojnoB"