# Utiliser range() avec un seul argument (stop)
# Génère des nombres de 0 à stop-1.

for i in range(5):
    print(i)
# Affichera :
# 0
# 1
# 2
# 3
# 4

# Utiliser range() avec deux arguments (start, stop)
# Génère des nombres de start à stop-1.

for i in range(2, 5):
    print(i)
# Affichera :
# 2
# 3
# 4

# Utiliser range() avec trois arguments (start, stop, step)
# Génère des nombres de start à stop-1 en incrémentant de step.

for i in range(1, 10, 2):
    print(i)
# Affichera :
# 1
# 3
# 5
# 7
# 9

# Utiliser range() avec un step négatif
# Génère des nombres en décrémentant.

for i in range(10, 0, -2):
    print(i)
# Affichera :
# 10
# 8
# 6
# 4
# 2