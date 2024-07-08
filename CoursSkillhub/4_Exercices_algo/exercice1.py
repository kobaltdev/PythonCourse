""" 
Exercice 1 : Décodage de message alien

Scénario : Tu as intercepté un message en provenance d'une civilisation extraterrestre.
Malheureusement, il est encodé dans un fichier JSON.

Fichier à traiter : alien_message.json
"""


import json
import base64
import os


def set_file_path(filename):
    # Path du dossier de travail
    directory = os.path.dirname(__file__)
    # contruction du chemin de fichier complet
    file_to_compute = os.path.join(directory, filename)
    return file_to_compute


##########################
#          MAIN          #
##########################

# contruction du chemin de fichier complet
file_to_decode = set_file_path("alien_message.json")


# ouverture du fichier
with open(file_to_decode, 'r') as fichier:
    # import du fichier dans un dictionnaire
    base64_message_dict = json.load(fichier)
    # Decode avec base64
    message_decode = base64.b64decode(base64_message_dict["message"])
    # Conversion en ascii
    message_decode_str = message_decode.decode("ascii")


print(message_decode_str)

