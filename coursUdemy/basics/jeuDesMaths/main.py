# IMPORTS
import random

# CONSTANTS
BORNE_MIN = 1
BORNE_MAX = 10
NB_QUESTIONS = 5


def poser_question():
    a = random.randint(BORNE_MIN, BORNE_MAX)
    b = random.randint(BORNE_MIN, BORNE_MAX)
    o = random.randint(0, 1)
    operateur = "+"
    if o == 1:
        operateur = "x"
    reponse = ""
    while reponse == "":
        try:
            reponse = int(input(f"Combien font {a} {operateur} {b} ? = "))
        except ValueError:
            print("Merci de saisir un nombre valide !")
    bonne_reponse = a + b
    if o == 1:
        bonne_reponse = a * b
    if reponse == bonne_reponse:
        print("Bonne réponse !")
        return True
    else:
        print("Mauvaise Réponse !")


def notation(score_joueur, score_max):
    moyenne = int(score_max/2)
    if score_joueur == 0:
        print("Révisez vos Maths !")
    elif score_joueur == score_max:
        print("Bravo, tout juste !")
    elif score_joueur <= moyenne:
        print("Peut mieux faire")
    elif score_joueur > moyenne:
        print("Pas mal !")


score = 0
for i in range(0, NB_QUESTIONS):
    print("")
    print(f"Question n° {i+1} sur {NB_QUESTIONS}")
    print("")
    if poser_question():
        score += 1

print("Partie Terminée")
print(f"Votre score : {score} sur {NB_QUESTIONS}")

notation(score, NB_QUESTIONS)
