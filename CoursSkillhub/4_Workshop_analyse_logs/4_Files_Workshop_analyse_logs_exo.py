""" 
WORKSHOP analyse de fichier de log

Ta misssion : extraire le données d'un fichier de log

Tu devras :

    - Ouvrir le fichier et en lire les lignes
    - Créer une fonction analyse_logs()
    - Compter :
        - Les occurrences de chaque adresse IP (v4 ou V6)
        - Compter les codes de statut http (erreurs 404, 500, etc.), et afficher leur nombre par type d'erreur
        - Compter les occurrences de chaque user agent 
"""

# Charger le fichier de logs


# Fonction pour analyser les logs (avec étapes)
def analyze_logs(logs):
    error_count = 0
    access_403 = 0
    access_404 = 0
    user_agents = {}
    ip_count = {}

        # Compter les occurrences de chaque adresse IP


        # Compter les codes de statut HTTP


        # Compter les occurrences de chaque user agent


# Analyser les logs
error_count, access_403, access_404, user_agents, ip_count = analyze_logs(logs)

# Affichage des résultats

# Nombre d'erreurs 500 :

# Nombre d'accès 403 :

# Nombre d'accès 404 :

# Top User Agents : agent : x fois

# Nombre d'accès par adresse IP :

# IP : x fois