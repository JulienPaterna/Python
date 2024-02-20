# def max_dico(dico):
#     max = 0
#     for elem in dico:
#         if (dico[elem] > max):
#             max = dico[elem]
#             name = elem
#     print((name, max))      
#     print(dico.items())      

def max_dico(dico):
    max = 0
    for nom, value in dico.items():
        if value > max:
            max = value
            name = nom
    return name, max

print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))