# try:

# except:

import sys
test = sys.argv[1]

with open(test) as f:
    fichier = f.read()

fichier = fichier.split("\n")
tot_tab = []
num_tab_ok = []

for line in fichier:
    line_tab = []
    line_tab.append(line)
    line_elem_tab = []
    for elem in line_tab[0]:
        line_elem_tab.append(elem)
    tot_tab.append(line_elem_tab)

# print(len(tot_tab))
# print(len(tot_tab[0]))

def test_first_line(indices, num):
    if indices[0] == 0:
        for n in range(indices[1] + 2):
            if tot_tab[1][n] == "*":
                return [num, [1, n]]
        if tot_tab[0][indices[1] + 1] == "*":
            return [num, [0, indices[1] + 1]]
    elif indices[1] == len(line_elem_tab) - 1:
        for n in range(indices[0] - 1, len(line_elem_tab)):
            if tot_tab[1][n] == "*":
                return [num, [1, n]]
        if tot_tab[0][indices[0] - 1] == "*":
            return [num, [0, indices[0] - 1]]
    else:
        for n in range(indices[0] - 1, indices[1] + 2):
            if tot_tab[1][n] == "*":
                return [num, [1, n]]
        if tot_tab[0][indices[0] - 1] == "*":
            return [num, [0, indices[0] - 1]]
        elif tot_tab[0][indices[1] + 1] == "*":
            return [num, [0, indices[1] + 1]]
    return 0

def test_last_line(indices, num):
    if indices[0] == 0:
        for n in range(indices[1] + 2):
            if tot_tab[len(tot_tab) - 2][n] == "*":
                return [num, [len(tot_tab) - 2, n]]
        if tot_tab[len(tot_tab) - 1][indices[1] + 1] == "*":
            return [num, [len(tot_tab) - 1, indices[1] + 1]]
    elif indices[1] == len(line_elem_tab) - 1:
        for n in range(indices[0] - 1, len(line_elem_tab)):
            if tot_tab[len(tot_tab) - 2][n] == "*":
                return [num, [len(tot_tab) - 2, n]]
        if tot_tab[len(tot_tab) - 1][indices[0] - 1] == "*":
            return [num, [len(tot_tab) - 1, indices[0] - 1]]
    else:
        for n in range(indices[0] - 1, indices[1] + 2):
            if tot_tab[len(tot_tab) - 2][n] == "*":
                return [num, [len(tot_tab) - 2, n]]
        if tot_tab[len(tot_tab) - 1][indices[0] - 1] == "*": 
            return [num, [len(tot_tab) - 1, indices[0] - 1]]
        elif tot_tab[len(tot_tab) - 1][indices[1] + 1] == "*":
            return [num, [len(tot_tab) - 1, indices[1] + 1]]
    return 0

def test_middle_line(line, indices, num):
    if indices[0] == 0:
        for n in range(indices[1] + 2):
            if tot_tab[line - 1][n] == "*":
                return [num, [line - 1, n]]
            elif tot_tab[line + 1][n] == "*":
                return [num, [line + 1, n]]
        if tot_tab[line][indices[1] + 1] == "*":
            return [num, [line, indices[1] + 1]]
    elif indices[1] == len(line_elem_tab) - 1:
        for n in range(indices[0] - 1, len(line_elem_tab)):
            if tot_tab[line - 1][n] == "*":
                return [num, [line - 1, n]]
            elif tot_tab[line + 1][n] == "*":
                return [num, [line + 1, n]]
        if tot_tab[line][indices[0] - 1] == "*":
            return [num, [line, indices[0] - 1]]
    else:
        for n in range(indices[0] - 1, indices[1] + 2):
            if tot_tab[line - 1][n] == "*":
                return [num, [line - 1, n]]
            elif tot_tab[line + 1][n] == "*":
                return [num, [line + 1, n]]
        if tot_tab[line][indices[0] - 1] == "*":
            return [num, [line, indices[0] - 1]]
        elif tot_tab[line][indices[1] + 1] == "*":
            return [num, [line, indices[1] + 1]]
    return 0

line = 0
numbers = []
while line < len(tot_tab):
    # print(line)
    start = 0
    end = 0
    i = 0
    # print("line", line)
    indices = []
    while i < len(tot_tab[line]):
        if tot_tab[line][i].isnumeric():
            num = tot_tab[line][i]
            start = i
            j = i + 1
            if tot_tab[line][j].isnumeric():
                while j < len(tot_tab[line]) and tot_tab[line][j].isnumeric():
                    num += tot_tab[line][j]
                    end = j
                    j += 1
            else:
                end = start
            # print(num)
            i = end
            i += 1
            indices.append(start)
            indices.append(end)
            if line == 0:
                if test_first_line(indices, num) != 0:
                    numbers.append(test_first_line(indices, num))
            elif line == len(tot_tab) - 1:
                if test_last_line(indices, num) != 0:
                    numbers.append(test_last_line(indices, num))
            else:
                if test_middle_line(line, indices, num) != 0:
                    numbers.append(test_middle_line(line, indices, num))
            # print(indices)
            # print(num_tab_ok)
            indices = []
        else:
            i += 1
    line += 1

tot = 0
for i in range(len(numbers) - 1):
    nums = []
    for j in range(i + 1, len(numbers)):
        if numbers[i][1] == numbers[j][1]:
            mult = int(numbers[i][0]) * int(numbers[j][0])
            tot += mult

print(tot)