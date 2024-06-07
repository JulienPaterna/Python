def a_doublon(list):
    result = 0
    n = len(list)
    for i in range(n - 1):
        if list[i + 1] == list[i]: 
            result += 1
    if result != 0: 
        print(True)
    else:
        print(False)

a_doublon([]) 
a_doublon([1]) 
a_doublon([1, 2, 4, 6, 6]) 
a_doublon([2, 5, 7, 7, 7, 9]) 
a_doublon([0, 0, 2, 3])