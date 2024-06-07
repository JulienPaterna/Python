def dichotomie(tab, x):
    """
        tab : tableau trié dans l'ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab == []:
        return False, 1
    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or x > tab[len(tab) - 1]:
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        mil = (debut + fin) // 2
        if x == tab[mil]:
            return True
        elif x < tab[mil]:
            fin = mil - 1
        else:
            debut = mil + 1
    return False, 3


print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
#True
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))
#(False, 3)
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1))
#(False, 2)
print(dichotomie([], 28))
#(False, 1)

