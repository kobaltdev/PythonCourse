""" 
WORKSHOP analyse de fichier de log

Ta mission : extraire le données d'un fichier de log

Tu devras :

    - Ouvrir le fichier et en lire les lignes
    - Créer une fonction analyse_logs()
    - Compter :
        - Les occurrences de chaque adresse IP (v4 ou V6)
        - Compter les codes de statut http (erreurs 404, 500, etc.), et afficher leur nombre par type d'erreur
        - Compter les occurrences de chaque user agent 
"""

####################
# Imports
####################
import os
from collections import Counter

####################
# FONCTIONS 
####################


def set_file_path(filename):
    # Path du dossier de travail
    directory = os.path.dirname(__file__)
    # contruction du chemin de fichier complet
    file_to_compute = os.path.join(directory, filename)
    return file_to_compute


def count_lines(file):
    line_count = 0
    with open(file, 'r') as fichier:
        raw_content = fichier.read()
        count = raw_content.split("\n")
        for i in count:
            if i:
                line_count += 1
    print("Nombre de lignes à analyser :", line_count)
    return line_count


def analyze_logs(log_file_to_analyse):
    # initialisation des variables de comptage
    error_count = 0
    access_403 = 0
    access_404 = 0
    http_codes_list = []
    http_codes = {}
    user_agents = {}
    ip_list = []
    ip_count = {}
   

    # Affichage du nombre de lignes à traiter
    line_count = count_lines(log_file_to_analyse)

    # Ouverture du fichier et dump des logs
    with open(log_file_to_analyse, 'r') as fichier:
        content = fichier.readlines()

        # boucle principale
        for i in range(0, line_count):
            log_lines = content[i].split(" ")

            # comptage des IPs 
            ip_list.append(log_lines[0]) # append à une liste de toutes les IP
            ip_count = Counter(ip_list) # on utilise Counter pour créer le dictionnaire d'occurences
        
            # comptage des codes HTTP
            http_codes_list.append(log_lines[8])
            http_codes = Counter(http_codes_list)
        



####################
# MAIN
####################

# Construction du path
logfile = set_file_path('logz.log')

# analyse des logs
analyze_logs(logfile)


# Analyser les logs
# error_count, access_403, access_404, user_agents, ip_count = analyze_logs(logs)

# Affichage des résultats

# Nombre d'erreurs 500 :

# Nombre d'accès 403 :

# Nombre d'accès 404 :

# Top User Agents : agent : x fois

# Nombre d'accès par adresse IP :

# IP : x fois