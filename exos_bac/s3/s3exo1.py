def moyenne(array_of_tupl):
    # sum = 0
    # num = 0
    # denom = 0
    # for i in range(len(tupl)):
    #     sum += tupl[i][1]
    # if sum == 0:
    #     print(None)
    # else:
    #     for i in range(len(tupl)):
    #         num += tupl[i][0] * tupl[i][1]
    #         denom += tupl[i][1]
    num = 0
    denom = 0
    for elem in array_of_tupl:
        num += (elem[0] * elem[1])
        denom += elem[1]
    if denom == 0:
        print(None)
    else:
        print(num/denom)

moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
