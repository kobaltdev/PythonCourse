# imports
import time


def intro():
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("Pensez à un nombre entier positif que je vais devoir trouver!")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("C'est parti !")
    print()


def bornage():
    borne_max = 10
    print("Ok, je dois d'abord déterminer l'ordre de grandeur de votre nombre")
    print("-----------")
    while True:
        reponse = input(f"Votre nombre est-il inférieur à {borne_max} ? (o / n) : ")
        match reponse:
            case "o":
                break
            case "n":
                borne_max = borne_max * 10
            case _:
                print("Merci de répondre 'o' ou 'n'")
    print()
    print(f"Ok, votre nombre est inférieur à {borne_max} !")
    print()
    return borne_max


def trouver_nombre(borne_max):
    bmin = 0
    bmax = 10
    


intro()
bmax = bornage()
