def recherche(a, tab):
    i = 0
    for elem in tab:
        if elem == a:
            i += 1   
    return i






print(recherche(5, []))
print(recherche(5, [-2, 3, 4, 8]))
print(recherche(5, [-2, 3, 1, 5, 3, 7, 4]))
print(recherche(5, [-2, 5, 3, 5, 4, 5]))