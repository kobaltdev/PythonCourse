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
    print()
    print("Travail dans le fichier :", file)
    print("Nombre de lignes à analyser :", line_count)
    print()
    return line_count


def sort_dict_by_decreasing_values(dict):
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get, reverse=True)
    for w in sorted_keys:
        sorted_dict[w] = dict[w]
    return sorted_dict


def analyze_logs(log_file_to_analyse):
    # initialisation des variables de comptage
    http_codes_list = []
    user_agents_list = []
    ip_list = []
   

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
            ip_count_withcounter = Counter(ip_list) # on utilise Counter pour créer le dictionnaire d'occurences
            # et on créé un dico à partir du counter
            ip_count_unsorted = dict(ip_count_withcounter)
            # tri du dico par valeur, en decroissant
            ip_count_sorted = sort_dict_by_decreasing_values(ip_count_unsorted)
        
            # comptage des codes HTTP
            http_codes_list.append(log_lines[8]) # append à une liste de tous les codes HTTP
            http_codes_withcounter = Counter(http_codes_list) # on utilise Counter pour créer le dictionnaire d'occurences
            # et on créé un dico à partir du counter
            http_codes_unsorted = dict(http_codes_withcounter)
            # tri du dico par valeur, en decroissant
            http_codes_sorted = sort_dict_by_decreasing_values(http_codes_unsorted)


            # pour les user agent, on va faire un slice à partir du 1er element qui nous interesse
            # jusqu'au dernier element, ici on utilise la longueur de la liste qu'on est en train de traiter

            # Doc combined logs apache : https://httpd.apache.org/docs/current/logs.html#combined
            
            # Creation d'une liste intermédiaire dans laquelle on vient joindre les differents elements
            # qui composent la partie user agent, afin de reconstruire le contenu du log.
            list_join = " ".join(log_lines[11:len(log_lines)])
            
            # on append chaque element à la liste des user agents + Counter
            # et on créé un dico à partir du counter
            user_agents_list.append(list_join)
            user_agents_withcounter = Counter(user_agents_list)
            user_agents_unsorted = dict(user_agents_withcounter)
            # tri du dico par valeur, en decroissant
            user_agents_sorted = sort_dict_by_decreasing_values(user_agents_unsorted)
   
    return http_codes_sorted, user_agents_sorted, ip_count_sorted


def print_results(httpcodes, useragents, ipcount):
    print("--- ANALYSE DES LOGS ---")
    print()
    
    # Codes HTTP
    print("CODES HTTP")
    for k in httpcodes:
        print(f"  - Code {k} : {httpcodes[k]} occurence(s)")
    print()

    # Adresses IP
    print("ADRESSES IP")
    for k in ipcount:
        print(f"  - {k} : {ipcount[k]} accès")
    print()

    # User agents
    print("TOP 10 USER AGENTS")
    j = 10
    for k in useragents:
        print(f"  - {k} : {useragents[k]} occurence(s)")
        j -= 1
        if j == 0:
            break


####################
# MAIN
####################

# Construction du path
logfile = set_file_path('logz.log')

# analyse des logs
http, uagents, ips = analyze_logs(logfile)

# Affichage des résultats
print_results(http, uagents, ips)