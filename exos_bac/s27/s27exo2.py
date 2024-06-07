def separe(tab):

    gauche = 0
    droite = len(tab) - 1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = gauche + 1
        else :
            tab[gauche], tab[droite] = tab[droite], 1
            droite = droite - 1
    return tab
    # result = []
    # for i in range(len(tab)):
    #     if (tab[i]== 0):
    #         result.append(tab[i])
    # for i in range(len(tab) - len(result)):
    #     result.append(1)
    # return result

print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
#[0, 0, 0, 0, 1, 1, 1, 1]
print(separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]))
#[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]