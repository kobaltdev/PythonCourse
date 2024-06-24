# Liste vide
ma_liste = []

# Liste avec éléments
ma_liste = [1, 2, 3, 'a', 'b', 'c']

# Fonctions Utiles pour les Listes

# len() : Renvoie la longueur de la liste
len(ma_liste)  # 6

# max() : Renvoie l'élément maximal (pour les listes de nombres)
chiffres = [1, 2, 3]
max(chiffres)  # 3

# min() : Renvoie l'élément minimal (pour les listes de nombres)
min(chiffres)  # 1

# sum() : Renvoie la somme des éléments (pour les listes de nombres)
sum(chiffres)  # 6

# Méthodes des Listes

# append(x) : Ajoute un élément à la fin de la liste.
ma_liste.append(4)
print(ma_liste)  # [1, 2, 3, 'a', 'b', 'c', 4]

# extend(iterable) : Ajoute tous les éléments d'un itérable à la fin de la liste
ma_liste.extend([5, 6])
print(ma_liste)  # [1, 2, 3, 'a', 'b', 'c', 4, 5, 6]

# insert(i, x) : Insère un élément à la position donnée
ma_liste.insert(2, 'z')
print(ma_liste)  # [1, 2, 'z', 3, 'a', 'b', 'c', 4, 5, 6]

# remove(x) : Supprime la première occurrence de l'élément x
ma_liste.remove('a')
print(ma_liste)  # [1, 2, 'z', 3, 'b', 'c', 4, 5, 6]

# pop(i) : Supprime et renvoie l'élément à la position i (dernier élément par défaut)
element = ma_liste.pop()
print(element)  # 6
print(ma_liste)  # [1, 2, 'z', 3, 'b', 'c', 4, 5]

# clear() : Supprime tous les éléments de la liste
ma_liste.clear()
print(ma_liste)  # []

# index(x) : Renvoie l'indice de la première occurrence de l'élément x
ma_liste = [1, 2, 3, 'b', 'c', 4, 5]
print(ma_liste.index('b'))  # 3

# count(x) : Renvoie le nombre de fois que l'élément x apparaît dans la liste
print(ma_liste.count(2))  # 1

# sort() : Trie la liste en place
chiffres = [3, 1, 2]
chiffres.sort()
print(chiffres)  # [1, 2, 3]

# reverse() : Inverse l'ordre des éléments de la liste
ma_liste.reverse()
print(ma_liste)  # [5, 4, 'c', 'b', 3, 2, 1]

# copy() : Renvoie une copie superficielle de la liste
nouvelle_liste = ma_liste.copy()
print(nouvelle_liste)  # [5, 4, 'c', 'b', 3, 2, 1]