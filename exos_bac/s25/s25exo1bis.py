def enumere(L):
    result = {}
    for elem in L:
        tab = []
        for j in range(len(L)):
            if L[j] == elem:
                tab.append(j)
        result[elem] = tab
    return result


print(enumere([1, 1, 2, 3, 2, 1]))
# {1: [0, 1, 5], 2: [2, 4], 3: [3]}