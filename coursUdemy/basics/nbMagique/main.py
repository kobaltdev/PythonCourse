# imports
import random


def demander_nombre(nb_min, nb_max):
    reponse = ""
    while reponse == "":
        try:
            reponse = int(input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ? = "))
        except ValueError:
            print("Saisissez un nombre valide !")
        else:
            if not nb_min <= reponse <= nb_max:
                print(f"Merci de saisir un nombre entre {nb_min} et {nb_max} !! ")
                reponse = ""
    return reponse


def traitement(reponse_user, nb_magique):
    if reponse_user == nb_magique:
        print("Bravo, vous avez trouvé le nombre magique")
        return True
    elif reponse_user < nb_magique:
        print("")
        print("Le nombre magique est plus grand !")
    else:
        print("")
        print("Le nombre magique est plus petit !")


NOMBRE_MIN = 1
NOMBRE_MAX = 100
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_ESSAIS = 7
bonne_reponse = False

while not bonne_reponse and NB_ESSAIS > 0:
    rep = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if traitement(rep, NOMBRE_MAGIQUE):
        bonne_reponse = True
    else:
        NB_ESSAIS -= 1
        print("")
        print("Il vous reste : " + str(NB_ESSAIS) + " essais !")

if NB_ESSAIS == 0:
    print("Perdu ! Vous n'avez plus d'essais possibles.")
    print(f"Le nombre magique était : {NOMBRE_MAGIQUE}")
