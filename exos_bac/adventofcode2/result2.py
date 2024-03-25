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
    tot_power = 0
    for i in range(len(sets)):
        ok = 1
        if len(sets[i]) == 1:
            ok = 0
        else:
            set = sets[i][1].split(";")
            # print(set)
            blue_min = 0
            red_min = 0
            green_min = 0
            for vars in set:
                color_number = vars.split(",")
                for color_informations in color_number:
                    color_informations = color_informations.split(" ")
                    for c in range(len(color_informations)):
                        if color_informations[c] == 'blue':
                            if int(color_informations[c - 1]) > blue_min:
                                blue_min = int(color_informations[c - 1])
                        if color_informations[c] == 'green':
                            if int(color_informations[c - 1]) > green_min:
                                green_min = int(color_informations[c - 1])
                        if color_informations[c] == 'red':
                            if int(color_informations[c - 1]) > red_min:
                                red_min = int(color_informations[c - 1])
            power_of_set = blue_min*red_min*green_min
        tot_power += power_of_set
    print(tot_power)

except: 
    print('0')
