def tri(tab):
    # i est le premier indice de la zone non triée,
    # j est le dernier indice de cette zone non triée. 
    # Au debut, la zone non triée est le tableau complet.
    i= 0
    j= len(tab) - 1
    while i != j :
        if tab[i] == 0:
            i= i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j - 1
    return tab
    

print(tri([0, 1, 0, 1, 0, 1, 0, 1, 0]))
#[0, 0, 0, 0, 0, 1, 1, 1, 1]