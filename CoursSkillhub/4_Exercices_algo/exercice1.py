""" 


Exercice 1 : Décodage de message alien



Scénario : Tu as intercepté un message en provenance d'une civilisation extraterrestre. Malheureusement, il est encodé dans un fichier JSON.



Fichier à traiter : alien_message.json
"""


import json

import base64
import os




filename = os.path.join("4_Exercices_algo", "alien_message.json")


print(filename)



with open(filename, 'r') as fichier:
    base64_message_dict = json.load(fichier)
    print(type(base64_message_dict))
    s = list(base64_message_dict.values())
    print(str(s))
 
