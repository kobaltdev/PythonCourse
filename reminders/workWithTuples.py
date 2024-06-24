# Création de Tuples

mon_tuple = (1, 2, 3) # Avec des parenthèses

mon_tuple = 1, 2, 3 # Sans parenthèses

tuple_vide = () # Tuple vide

tuple_unique = (1,) # Tuple a un seul élément

# Fonctions Utiles pour les Tuples

# len() : Renvoie la longueur du tuple.

len(mon_tuple)  # 3

# max() : Renvoie la valeur maximale du tuple.

max(mon_tuple)  # 3

# min() : Renvoie la valeur minimale du tuple.

min(mon_tuple)  # 1

# sum() : Renvoie la somme des éléments du tuple.

sum(mon_tuple)  # 6

# tuple() : Convertit un itérable en tuple.

liste = [1, 2, 3]
tuple_converti = tuple(liste)  # (1, 2, 3)

# Méthodes des Tuples

# count(x) : Renvoie le nombre de fois que x apparaît dans le tuple.

mon_tuple = (1, 2, 3, 2)
mon_tuple.count(2)  # 2

# index(x) : Renvoie l'index de la première occurrence de x dans le tuple.

mon_tuple.index(3)  # 2