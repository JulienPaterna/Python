def recherche(tab, n):
    if (len(tab) == 1 and tab[0] != n):
        return -1
    i = len(tab)//2
    if (tab[i] == n):
        return i
    elif (tab[i] < n):
        new = recherche(tab[i:], n)
        if (new == -1):
            return -1
        else:
            return new + i
    elif (tab[i] > n):
        new = recherche(tab[:i], n)
        return new



print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7, 8], 5))
