from math import sqrt

def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    # print(sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    # print(point)
    return point

# distance((1, 0), (5, 3))
# distance((1, 0), (0, 1))
# plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0))
# plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2))

