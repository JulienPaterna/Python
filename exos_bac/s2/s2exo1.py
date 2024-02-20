def indices_maxi(tab):
    liste = []
    index = 0
    max = tab[0]
    # for elem in tab:
    #     if elem >= max:
    #         max = elem
    # for elem in tab:
    #     if elem == max:
    #         liste.append(index)
    #     index += 1
    # result = (max, liste)
    # print(result)
    for i in range(1, len(tab)):
        if tab[i] > max:
            max = tab[i]
    for i in range(len(tab)):
        if tab[i] == max:
            liste.append(i)
    print((max, liste))

indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
indices_maxi([7])
