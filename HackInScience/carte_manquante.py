"""
Rédigez une fonction nommée missing_card acceptant un jeu de carte dont une carte manque, 
et renvoyant le nom de la carte manquante.

Le jeu de carte sera donné à votre fonction sous forme d'une chaîne de noms de carte séparés par des espaces.

Un nom de carte contient la couleur et la valeur de la carte. La couleur est dans l’ensemble {"S", "H", "D", "C"} 
et sa valeur dans {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}, soit un total de 52 cartes.

Votre fonction recevra toujours 51 cartes, elle doit trouver la carte manquante.


Exemple : 
print(
    missing_card(
        "S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA "
        "H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA "
        "D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA "
        "C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK"
    )
)

-> doit afficher CA (attention, votre fonction doit renvoyer CA, dans mon exemple j'ai utilise print pour l'afficher).

"""

def missing_card(cards_set):
    colors = ('S', 'H', 'D', 'C')
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
 
    # construction d'une liste a partir du jeu passé en paramètre
    given_deck = cards_set.split()

    complete_deck = []
    for c in colors:        
        for v in values:
            complete_deck.append(str(c + v))
    
    # comprehension de liste, construire une liste : la différence entre les 2 autres
    dif = [x for x in complete_deck if x not in given_deck]
    
    return str(dif[0])




card_set = (
        "S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA "
        "H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA "
        "D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA "
        "C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK"
    )


print(missing_card(card_set))