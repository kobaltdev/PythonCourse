"""
Rédigez une fonction trouvant la distance entre les deux nombres les plus éloignés d’une liste donnée.

Créez une fonction nommée dist, acceptant un paramètre : une liste de nombres (entiers ou flotants), 
et renvoyant la plus grande distance entre deux nombres de cette liste, typiquement entre le plus grand et le plus petit."""

def dist(points):
    mini = min(points)
    maxi = max(points)
    if mini < 0:
        mini = abs(mini)
        return mini + maxi
    return maxi - mini
    




points_A = [1,
            2,
            3]

points_B = [1,
            2,
            3,
            2.5,
            3.5,
            120]

points_C = [1,
            2,
            3,
            2.5,
            3.5,
            120,
            -1000]

points_D = [-10,
            -1000]

print(dist(points_D))