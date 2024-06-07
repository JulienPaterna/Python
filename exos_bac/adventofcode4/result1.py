import sys
test = sys.argv[1]

try:
  with open(test, 'r') as fichier:
    fichier = fichier.read()

    cards = fichier.split("\n")

    def get_my_numbers(card):
        my_numbers_tab = []
        my_part = card.split(" | ")
        tab = my_part[0].split(":")
        my_numbers = tab[1]
        my_numbers_split = my_numbers.split(" ")
        for elem in my_numbers_split:
            if elem.isnumeric():
                my_numbers_tab.append(elem)
        return (my_numbers_tab)

    def get_THE_numbers(card):
        the_numbers_tab = []
        the_numbers = card.split(" | ")
        tab = the_numbers[1].split(" ")
        for elem in tab:
            if elem.isnumeric():
                the_numbers_tab.append(elem)
        return (the_numbers_tab)


    def get_similar(card):
        my_numbers = get_my_numbers(card)
        the_numbers = get_THE_numbers(card)
        sim = 0
        for elem in my_numbers:
            if the_numbers.count(elem):
                sim += 1
        return sim

    def calcul_pts(card):
        sim = get_similar(card)
        pts = 0
        if (sim == 1):
            pts = 1
        elif (sim > 1):
            pts = 1
            for n in range(1, sim):
                pts = pts * 2
        return pts

    def total_pts(cards):
        total = 0
        for card in cards:
            total = total + calcul_pts(card)
        return total

    print(total_pts(cards))
except:
  print("Files doesn't exist")
