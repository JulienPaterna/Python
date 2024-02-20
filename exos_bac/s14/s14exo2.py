def insere(a, tab):
    """ Insère l'élément a (int) dans le tableau tab (list) trié par ordre croissant à sa place et renvoie le nouveau tableau. """
    l = list(tab) #l contient les memes elements que tab
    l.append(a)
    i = len(tab) - 1
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l


print(insere(3, [1, 2, 4, 5]))
print(insere(30, [1, 2, 7, 12, 14, 25]))
print(insere(1, [2, 3, 4]))
print(insere(1, []))