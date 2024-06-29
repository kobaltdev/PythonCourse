"""
Exercice 4 : Répertoire des films de science-fiction

Scénario :
Tu es responsable de la gestion d'une vidéothèque spécialisée en films de science-fiction.
Un fichier movies.txt contient la liste des films avec l'année de sortie.
Tu dois extraire et afficher les films sortis après l'année 2000.

Fichier associé : movies.txt
"""
# Lecture du répertoire des films
with open('movies.txt', 'r') as file:
    movies = file.readlines()

# Extraction des films après l'année 2000
recent_movies = []

# Ton code ici

print("Films sortis après 2000:")
for movie in recent_movies:
    print(movie)