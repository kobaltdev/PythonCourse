"""
Rédigez une fonction choisissant les élèves reçus et refusés selon un seuil.

La fonction doit s'appeler select_student et prendre deux arguments :

    une liste dont chaque élément est une liste de deux éléments : le nom et la note d'un étudiant,
    un seuil. La note d’un étudiant doit être supérieure ou égale au seuil afin d’être reçu.

Votre fonction doit renvoyer un dictionnaire contenant deux entrées :

    "Accepted" : la liste des étudiants acceptés triés par notes décroissantes.
    "Refused" : la liste des étudiants refusés triés par notes croissantes.
"""
from operator import itemgetter


def select_student(list, trigger):
    status = ['Accepted', 'Refused']
    results = {key: [] for key in status}
    for e in list:
        if e[1] >= trigger:
            results['Accepted'].append(e)
        else :
            results['Refused'].append(e)

    results['Accepted'] = sorted(results['Accepted'], key=itemgetter(1), reverse=True)
    results['Refused'] = sorted(results['Refused'], key=itemgetter(1))

    return results






my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ahomas Albert', 34], ['Ben Ball', 5], ['William Lee', 2]]


res = select_student(my_class, 20)
print(res)