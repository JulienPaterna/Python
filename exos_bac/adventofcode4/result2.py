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

    card_sim = []
    for card in cards:
        card_sim.append(get_similar(card))

    tot = [1 for n in range(len(card_sim))]
    # print(card_sim)
    # print(tot)
    i = 0
    while i < len(card_sim) - 1: 
        j = i + 1
        n = 1
        while n <= card_sim[i] and j < len(card_sim):
            tot[j] += tot[i]
            j += 1
            n += 1
        i += 1
    # print(tot)
    sum_tot = 0
    for elem in tot:
        sum_tot += elem
    print(sum_tot)

except:
  print("Files doesn't exist")
