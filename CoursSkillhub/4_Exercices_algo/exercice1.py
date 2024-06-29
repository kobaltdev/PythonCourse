""" 
Exercice 1 : Décodage de message alien

Scénario : Tu as intercepté un message en provenance d'une civilisation extraterrestre.
Malheureusement, il est encodé dans un fichier JSON.

Fichier à traiter : alien_message.json
"""


import json
import base64
import os

# Get current working dir
cwd = os.getcwd()

# contruction du chemin de fichier complet
file_to_decode = os.path.join(cwd, "alien_message.json")
print()
print(f"chemin du fichier à decoder : {file_to_decode}")

# ouverture du fichier
with open(file_to_decode, 'r') as fichier:
    # import du fichier dans un dictionnaire
    base64_message_dict = json.load(fichier)
    # Decocade avec base64
    message_decode = base64.b64decode(base64_message_dict["message"])
    # Conversion en ascii
    message_decode_str = message_decode.decode("ascii")


print(message_decode_str)

