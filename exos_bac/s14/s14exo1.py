def recherche(elt, tab): 
    i = 0
    for elem in tab: 
        if (elem != elt):
            i += 1
        else:
            return i
    if i == 0 or i == len(tab):
        return (-1)



print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))
print(recherche(50, []))
print(recherche(4, [2, 4, 4, 3, 4]))