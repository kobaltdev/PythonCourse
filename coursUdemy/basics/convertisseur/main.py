# constantes

UNITE1_TYPE = "centimètres"
UNITE2_TYPE = "pouces"
TAUX_CONVERSION = 2.54


# Fonctions


def choix_type_conversion():
    print()
    print(f"Programme de conversion | {UNITE1_TYPE} et {UNITE2_TYPE}")
    print("---------------------------------------------------------")
    print("Quel type de conversion voulez vous effectuer ? ")
    print(f"{UNITE1_TYPE} vers {UNITE2_TYPE} : Saisir 1")
    print(f"{UNITE2_TYPE} vers {UNITE1_TYPE} : Saisir 2")
    type_conversion = ""
    while type_conversion == "":
        try:
            type_conversion = int(input("Votre choix ? : "))
            if type_conversion < 1 or type_conversion >= 3:
                print("Merci de saisir une réponse valide (1 ou 2)")
                type_conversion = ""
        except:
            print("Merci de saisir une réponse valide !")
    return type_conversion


def saisie_valeur(conv_type):
    if conv_type == 1:
        valeur = ""
        while valeur == "":
            try:
                valeur = float(input(f"Entrez la valeur en {UNITE1_TYPE} à convertir en {UNITE2_TYPE} : "))
            except:
                print("Merci de saisir une valeur valide !")
        return valeur
    else:
        valeur = ""
        while valeur == "":
            try:
                valeur = float(input(f"Entrez la valeur en {UNITE2_TYPE} à convertir en {UNITE1_TYPE} : "))
            except:
                print("Merci de saisir une valeur valide !")
        return valeur


def convertir_et_afficher_resultat(valeur, type_conversion):
    if type_conversion == 1:
        valeur_convertie = round(valeur / TAUX_CONVERSION, 2)
        print()
        print(f"{valeur} {UNITE1_TYPE} vaut : {valeur_convertie} {UNITE2_TYPE}  (arrondi à 2 décimales)")
    else:
        print()
        valeur_convertie = round(valeur * TAUX_CONVERSION, 2)
        print(f"{valeur} {UNITE2_TYPE} vaut : {valeur_convertie} {UNITE1_TYPE}  (arrondi à 2 décimales)")


# Main
reponse = ""
while not reponse == "stop":
    type_de_conversion = choix_type_conversion()
    valeur_user = saisie_valeur(type_de_conversion)
    convertir_et_afficher_resultat(valeur_user, type_de_conversion)
    print()
    print("Voulez vous continuer ? Saisissez 'stop' pour arrêter, sinon ENTREE :")
    reponse = input("Votre choix : ").lower()
    if reponse == "stop":
        print("Fin de programme")
        break
