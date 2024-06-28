# Manipulation des Fichiers en Python avec open et close
# Fichiers TXT
# Lire un fichier TXT

# Pour lire le contenu d'un fichier TXT en utilisant open et close :

fichier = open('fichier.txt', 'r')
contenu = fichier.read()
print(contenu)
fichier.close()

# Écrire dans un fichier TXT

# Pour écrire du texte dans un fichier TXT :

fichier = open('fichier.txt', 'w')
fichier.write("Ceci est un exemple de texte.\n")
fichier.close()

# Ajouter du texte dans un fichier TXT

# Pour ajouter du texte à un fichier TXT existant :

fichier = open('fichier.txt', 'a')
fichier.write("Ajout de texte supplémentaire.\n")
fichier.close()

# Méthode plus efficace avec le gestionnaire de contexte (pas besoin de fermer le fichier)

# Pour lire le contenu d'un fichier TXT, utilisez la méthode open() en mode lecture ('r'), puis lisez le contenu avec la méthode read(), readline(), ou readlines().

with open('fichier.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)

# Écrire dans un fichier TXT

with open('fichier.txt', 'w') as fichier:
    fichier.write("Ceci est un exemple de texte.\n")

# Ajouter du texte dans un fichier TXT

with open('fichier.txt', 'a') as fichier:
    fichier.write("Ajout de texte supplémentaire.\n")

# Fichiers JSON

# Pour manipuler des fichiers JSON, Python propose le module json.
# Lire un fichier JSON

# Pour lire le contenu d'un fichier JSON, utilisez open() en mode lecture ('r') et la méthode json.load().

import json

with open('fichier.json', 'r') as fichier:
    data = json.load(fichier)
    print(data)

# Écrire dans un fichier JSON

import json

data = {"nom": "Alice", "age": 30}

with open('fichier.json', 'w') as fichier:
    json.dump(data, fichier)

# Ajouter des données dans un fichier JSON

import json

# Lire le contenu existant
with open('fichier.json', 'r') as fichier:
    data = json.load(fichier)

# Mettre à jour les données
data["ville"] = "Paris"

# Écrire les nouvelles données dans le fichier
with open('fichier.json', 'w') as fichier:
    json.dump(data, fichier)



