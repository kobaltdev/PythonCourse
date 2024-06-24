import random
import collections

mini = 1
maxi = 100
nb_valeurs = 50
repete = 1


def generer_valeurs_et_afficher(val_mini, val_max, qte, repetition):
    for j in range(0, repetition):
        valeurs = []
        for i in range(0, qte):
            valeurs.append(random.randint(val_mini, val_max))
        return valeurs


# generer_valeurs_et_afficher(mini, maxi, nb_valeurs, repete)


# liste = [61, 23, 46, 71, 5, 87, 89, 4, 69, 91, 74, 39, 61, 6, 42, 82, 90, 41, 40, 85, 48, 11, 51, 14, 54, 38, 27, 1,
#         32, 78, 33, 60, 39, 67, 58, 83, 27, 19, 20, 53, 76, 85, 93, 17, 33, 75, 79, 27, 32, 9, 61, 30, 1, 94, 49, 97,
#         45, 40, 8, 50, 19, 49, 93, 73, 1, 16, 74, 8, 73, 98, 38, 61, 95, 63, 61, 32, 81, 95, 8, 34, 25, 41, 94, 12, 40,
#         24, 65, 49, 19, 18, 31, 98, 73, 52, 57, 24, 31, 85, 52, 28]

for k in range(0, 100):
    l2 = generer_valeurs_et_afficher(mini, maxi, nb_valeurs, repete)
    print(sorted(l2))
    print(sorted(l2, reverse=True))
    k += 1


# personne = {'nom': 'Melanie',
#             'age': 25,
#             'taille': 2.60
#             }
#
# print(personne)
# print(personne['nom'])
#
# personne['nom'] = "claire"
# personne['poste'] = 'dev'
#
# print(personne)
#
# for i in personne:
#     print(i)
#     print(personne[i])
