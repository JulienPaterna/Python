def recherche (tab, n):
    debut = 0
    fin = len(tab)-1
    indice = -1
    while debut <= fin and indice == -1:
        milieu = (debut+fin)//2
        if tab[milieu] == n:
            indice = milieu
        elif n > tab[milieu]:
            debut = milieu + 1
        else :
            fin = milieu - 1
    return indice


print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7, 8], 5))