def recherche_indices_classement(elt, tab):
    first = []
    second = []
    third = []
    for i in range(len(tab)):
        if (tab[i] < elt):
            first.append(i)
        elif (tab[i] == elt): 
            second.append(i)
        elif (tab[i] > elt):
            third.append(i)
    return first, second, third




print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
print(recherche_indices_classement(3, [1, 1, 1, 1]))
print(recherche_indices_classement(3, []))