"""
Exercice 4 : Répertoire des films de science-fiction

Scénario :
Tu es responsable de la gestion d'une vidéothèque spécialisée en films de science-fiction.
Un fichier movies.txt contient la liste des films avec l'année de sortie.
Tu dois extraire et afficher les films sortis après l'année 2000.

Fichier associé : movies.txt
"""

# IMPORTS
import os


######################
# FUNCTIONS
######################


def set_file_path(filename):
    # Path du dossier de travail
    directory = os.path.dirname(__file__)
    # contruction du chemin de fichier complet
    file_to_compute = os.path.join(directory, filename)
    return file_to_compute


def show_movies_after_release_date(movie_dict, date):
    print(f"Films sortis après {date}:")
    for movie in movie_dict:
        movie_year = int(movie_dict.get(movie))
        if movie_year >= date:
            print(movie, ":", movie_dict.get(movie))


######################
# MAIN
######################

# construction du chemin de travail pour le fichier
movie_file = set_file_path("movies.txt")


# Lecture du répertoire des films
with open(movie_file, 'r') as file:
    movies = file.readlines()


# Import dans un dictionnaire
recent_movies = {}
for movie in movies:
    key, value = movie.strip().split(':')
    recent_movies[key.strip()] = value.strip()


# Appel fonction
show_movies_after_release_date(recent_movies, 2000)