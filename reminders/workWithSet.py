# Création de Sets

# Set vide :
mon_set = set()

# Set avec des éléments :
mon_set = {1, 2, 3, 'a', 'b'}

# Fonctions Utiles pour les Sets

# len() : Renvoie le nombre d'éléments dans le set
len(mon_set)  # 5

# set() : Convertit un itérable en set
liste = [1, 2, 3, 1, 2]
mon_set = set(liste)  # {1, 2, 3}

# Méthodes des Sets

# add(x) : Ajoute l'élément x au set
mon_set.add(4)
print(mon_set)  # {1, 2, 3, 'a', 'b', 4}

# remove(x) : Supprime l'élément x du set. Lève une exception si l'élément n'existe pas
mon_set = {1, 2, 3, 'a', 'b'}
mon_set.remove('a')
print(mon_set)  # {1, 2, 3, 'b', 4}

# discard(x) : Supprime l'élément x du set s'il existe
mon_set.discard('b')
print(mon_set)  # {1, 2, 3, 4}

# pop() : Supprime et renvoie un élément arbitraire du set
element = mon_set.pop()
print(element)  # 1 (ou un autre élément aléatoire)
print(mon_set)  # {2, 3, 4}

# clear() : Supprime tous les éléments du set
mon_set.clear()
print(mon_set)  # set()

# copy() : Renvoie une copie superficielle du set
mon_set = {1, 2, 3}
copie_set = mon_set.copy()
print(copie_set)  # {1, 2, 3}

# union(*others) : Renvoie un nouveau set contenant tous les éléments de plusieurs sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5}

# intersection(*others) : Renvoie un nouveau set contenant les éléments communs à plusieurs sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # {3}

# difference(*others) : Renvoie un nouveau set contenant les éléments présents dans le set d'origine mais pas dans les autres
difference_set = set1.difference(set2)
print(difference_set)  # {1, 2}

# symmetric_difference(other) : Renvoie un nouveau set contenant les éléments présents dans un seul des sets, mais pas dans les deux
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)  # {1, 2, 4, 5}

# isdisjoint(other) : Renvoie True si le set n'a aucun élément en commun avec other
set3 = {7, 8, 9}
print(set1.isdisjoint(set3))  # True

# issubset(other) : Renvoie True si tous les éléments du set sont dans other
set4 = {1, 2}
print(set4.issubset(set1))  # True

# issuperset(other) : Renvoie True si tous les éléments de other sont dans le set
print(set1.issuperset(set4))  # True