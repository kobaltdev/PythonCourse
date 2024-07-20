"""
Cherchez le prochain vendredi 13.

Rédigez une fonction nommée friday_the_13th, n’acceptant aucun paramètre et renvoyant la date du prochain vendredi 13.

Appelée lors d’un vendredi 13 la fonction doit renvoyer le vendredi 13 actuel, pas le prochain.

Renvoyez la date sous forme d'une chaîne de caractère au format : YYYY-MM-DD.
"""

from datetime import date

def friday_the_13th():
    year = date.today().year
    while True:
        for m in range(1, 13):
            if date(year, m, 13).weekday() == 4:
                next_friday_13 = date(year, m, 13)
                return str(next_friday_13)
        year += 1


print(friday_the_13th())
