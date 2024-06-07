# def fusion(tab1, tab2):
#     list = tab1 + tab2
#     print(sorted(list))

def fusion(tab1, tab2):
    tab_fus = tab1 + tab2
    # for i in range(len(tab1)):
    #     tab_fus.append(tab1[i])
    # for i in range(len(tab2)):
    #     tab_fus.append(tab2[i])
    # print(tab_fus)
    for i in range(len(tab_fus) - 1):
        for j in range(i + 1, len(tab_fus)):
            if (tab_fus[i] > tab_fus[j]):
                x = tab_fus[i]
                tab_fus[i] = tab_fus[j]
                tab_fus[j] = x
    print(tab_fus)

fusion([3, 5, 7], [-4, 2, 5, 12])
