"""
Exercice 1 : Le compte à rebours de l'astéroïde
Scénario :
Tu es un membre d'équipage sur un vaisseau spatial et un astéroïde se dirige vers la Terre. 
Tu dois créer un script qui affiche un compte à rebours de 10 à 1 
et ensuite afficher "Impact imminent !".
"""

import time


def compte_a_rebours(valeur_depart, message):
    for i in range(valeur_depart, 0, -1):
        print(i)
        time.sleep(1)
    print(message)


compte_a_rebours(10, "Impact imminent !")
