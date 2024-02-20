def maxliste(list):
    max = list[0]
    for elem in list:
        if elem > max:
            max = elem
    print(max)



maxliste([98, 12, 104, 23, 131, 9])
maxliste([-27, -24, -3, -15])