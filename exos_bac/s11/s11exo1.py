def convertir(tab):
    result = 0
    i = 1
    for elem in tab:
        if (elem == 1):
            result += 2**(len(tab) - i)
        i += 1
    print(result)


convertir([1, 0, 1, 0, 0, 1, 1])
convertir([1, 0, 0, 0, 0, 0, 1, 0])
convertir([1, 1, 1, 1, 1, 1, 1, 1])
