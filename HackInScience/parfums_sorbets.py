"""Vous travaillez pour un restaurant, et on vous demande de générer le menu des sorbets...

Fournissez un script qui affiche tous les sorbets de deux boules possibles (la liste des parfums vous est fournie).

Ne proposez pas deux boules du même parfum (pas de "Chocolate Chocolate"), 
et attention, si vous avez affiché "Chocolate Banana", n'affichez pas "Banana Chocolate" plus loin.

Affichez une paire par ligne, en séparant les parfums par des virgules"""

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

while len(FLAVORS) > 1:
    temp_values = FLAVORS[1:]
    for i in range(len(temp_values)):
        print(f"{FLAVORS[0]}, {temp_values[i]}")
    del FLAVORS[0]
