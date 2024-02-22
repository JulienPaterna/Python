def recherche_min(tab):
    i = len(tab) - 1
    min = tab[i]
    while i >= 0:
        if tab[i] <= min:
            min = tab[i]
            indice = i
        i -= 1
    return indice



print(recherche_min([5]))
# 0
print(recherche_min([2, 4, 1]))
# 2
print(recherche_min([5, 3, 2, 2, 4]))
# 2