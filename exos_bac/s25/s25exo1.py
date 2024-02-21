def enumere(L):
    result = {}
    i = 0
    for elem in L:
        if elem not in result:
            result[elem] = [i]
        else:
            result[elem].append(i)
        i += 1
    return result



print(enumere([1, 1, 2, 3, 2, 1]))
print(enumere([1, 1, 5, 2, 3, 2, 1, 2]))
# {1: [0, 1, 5], 2: [2, 4], 3: [3]}
