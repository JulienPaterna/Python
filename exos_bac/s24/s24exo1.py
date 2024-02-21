def nbr_occurrences(chaine):
    map = {}
    for char in chaine:
        if char in map :
            map[char] += 1
        else:
            map[char] = 1
    return map


print(nbr_occurrences('Hello world !'))
# {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}
print(nbr_occurrences('coucou'))