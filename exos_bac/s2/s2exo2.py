def positif(pile):
  pile_1 = list(pile)
  pile_2 = []
  while pile_1 != []:
    x = pile_1.pop()
    if x >= 0:
      pile_2.append(x)
  while pile_2 != []:
    x = pile_2.pop()
    pile_1.append(x)
  # print(pile_1)
  return pile_1

# positif([-1, 0, 5, -3, 4, -6, 10, 9, -8])
# positif([-1])