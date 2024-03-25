try :
    import sys
    fichier = sys.argv[1]

    with open(fichier, 'r') as f:
        fichier = f.read()
    fichier = fichier.split("\n")

    sets = []

    for elem in fichier:
        elem = elem.split(":")
        sets.append(elem)

    group_sum = 0
    for i in range(len(sets)):
        ok = 1
        if len(sets[i]) == 1:
            ok = 0
        else:
            set = sets[i][1].split(";")
            for vars in set:
                color_number = vars.split(",")
                for color_informations in color_number:
                    color_informations = color_informations.split(" ")
                    # print(color_informations)
                    for c in range(len(color_informations)):
                        if color_informations[c] == 'blue':
                            if int(color_informations[c - 1]) > 14:
                                ok = 0
                        if color_informations[c] == 'green':
                            if int(color_informations[c - 1]) > 13:
                                ok = 0
                        if color_informations[c] == 'red':
                            if int(color_informations[c - 1]) > 12:
                                ok = 0
        if ok == 1:
            set_indice = i+1
            group_sum += set_indice

    print(group_sum)
except: 
    print('0')
