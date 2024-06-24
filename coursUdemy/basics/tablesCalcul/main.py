# Fonctions

def saisie_parametres():
    print("TABLE DE MULTIPLICATION")
    print("-----------------------")
    table = ""
    while table == "":
        try:
            table = int(input("Quelle table voulez vous afficher ? Saisir : "))
            if table < 1:
                print("Merci de saisir un nombre plus grand que 0 !")
                table = ""
        except ValueError:
            print("Merci de saisir un nombre valide !")
    print()
    bornes_valides = False
    while not bornes_valides:
        print("Ok, saisissez maintenant les bornes de la table à afficher")
        minimum = ""
        while minimum == "":
            try:
                minimum = int(input("Borne mini = "))
                if minimum < 0:
                    print("Merci de saisir un nombre plus grand que 0 !")
                    minimum = ""
            except ValueError:
                print("Merci de saisir un nombre valide !")
        maximum = ""
        while maximum == "":
            try:
                maximum = int(input("Borne Maxi = "))
                if maximum < 0:
                    print("Merci de saisir un nombre plus grand que 0 !")
                    maximum = ""
            except ValueError:
                print("Merci de saisir un nombre valide !")
        if minimum <= maximum:
            bornes_valides = True
        else:
            print("Erreur, les bornes ne sont pas valides ! Recommencez.")
    return table, minimum, maximum


def afficher_table(n, mini=1, maxi=10):
    print()
    for i in range(mini, maxi + 1):
        print(f"{i} x {n} = {i*n}")


table_m, bmin, bmax = saisie_parametres()
afficher_table(table_m, bmin, bmax)
