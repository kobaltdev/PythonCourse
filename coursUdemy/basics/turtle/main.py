import turtle

t = turtle.Turtle()

NB_MARCHES = 5
LONGUEUR_MARCHES = 30


def escalier(taille, nbmarches):
    for i in range(0, nbmarches):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


def carre(taille):
    for i in range(0, 3):
        t.forward(taille)
        t.right(90)
    t.forward(taille)
    t.right(90)


def carres(taille_depart, pas, nb):
    for i in range(0, nb):
        carre(taille_depart)
        taille_depart = taille_depart + pas


carres(20, 20, 10)

turtle.done()

