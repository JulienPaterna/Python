from random import randint

def lancer(n):
    result = []
    for i in range(n):
        result.append(randint(1,6))
    print(result)
    return(result)

def paire_6(tab):
    nb_6 = 0
    for i in range(len(tab)):
        if tab[i] == 6:
            nb_6 += 1
    if nb_6 >= 2:
        print(True)
    else: 
        print(False)

paire_6(lancer(25))