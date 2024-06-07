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
    yes_or_not = 0
    if indices[0] == 0:
        for n in range(indices[1] + 2):
            if tot_tab[1][n] != ".":
                yes_or_not += 1
        if yes_or_not != 0 or tot_tab[0][indices[1] + 1] != ".":
            return num
        else:
            return 0
    elif indices[1] == len(line_elem_tab) - 1:
        for n in range(indices[0] - 1, len(line_elem_tab)):
            if tot_tab[1][n] != ".":
                yes_or_not += 1
        if yes_or_not != 0 or tot_tab[0][indices[0] - 1] != ".":
            return num
        else:
            return 0
    else:
        for n in range(indices[0] - 1, indices[1] + 2):
            if tot_tab[1][n] != ".":
                yes_or_not += 1
        if yes_or_not != 0 or tot_tab[0][indices[0] - 1] != "." or tot_tab[0][indices[1] + 1] != ".":
            return num
        else:
            return 0

def test_last_line(indices, num):
    yes_or_not = 0
    if indices[0] == 0:
        for n in range(indices[1] + 2):
            if tot_tab[len(tot_tab) - 2][n] != ".":
                yes_or_not += 1
        if yes_or_not != 0 or tot_tab[len(tot_tab) - 1][indices[1] + 1] != ".":
            return num
        else:
            return 0
    elif indices[1] == len(line_elem_tab) - 1:
        for n in range(indices[0] - 1, len(line_elem_tab)):
            if tot_tab[len(tot_tab) - 2][n] != ".":
                yes_or_not += 1
        if yes_or_not != 0 or tot_tab[len(tot_tab) - 1][indices[0] - 1] != ".":
            return num
        else:
            return 0
    else:
        for n in range(indices[0] - 1, indices[1] + 2):
            if tot_tab[len(tot_tab) - 2][n] != ".":
                yes_or_not += 1
        if yes_or_not != 0 or tot_tab[len(tot_tab) - 1][indices[0] - 1] != "." or tot_tab[len(tot_tab) - 1][indices[1] + 1] != ".":
            return num
        else:
            return 0

def test_middle_line(line, indices, num):
    yes_or_not = 0
    if indices[0] == 0:
        for n in range(indices[1] + 2):
            if tot_tab[line - 1][n] != "." or tot_tab[line + 1][n] != ".":
                yes_or_not += 1
        if yes_or_not != 0 or tot_tab[line][indices[1] + 1] != ".":
            return num
        else:
            return 0
    elif indices[1] == len(line_elem_tab) - 1:
        for n in range(indices[0] - 1, len(line_elem_tab)):
            if tot_tab[line - 1][n] != "." or tot_tab[line + 1][n] != ".":
                yes_or_not += 1
        if yes_or_not != 0 or tot_tab[line][indices[0] - 1] != ".":
            return num
        else:
            return 0
    else:
        for n in range(indices[0] - 1, indices[1] + 2):
            if tot_tab[line - 1][n] != "." or tot_tab[line + 1][n] != ".":
                yes_or_not += 1
        if yes_or_not != 0 or tot_tab[line][indices[0] - 1] != "." or tot_tab[line][indices[1] + 1] != ".":
            return num
        else:
            return 0

line = 0
while line < len(tot_tab):
    # print(line)
    start = 0
    end = 0
    i = 0
    # print("line", line)
    indices = []
    # numbers = []
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
                    num_tab_ok.append(num)
            elif line == len(tot_tab) - 1:
                if test_last_line(indices, num) != 0:
                    num_tab_ok.append(num)
            else:
                if test_middle_line(line, indices, num) != 0:
                    num_tab_ok.append(num)
            # print(indices)
            # print(num_tab_ok)
            indices = []
        else:
            i += 1
    line += 1

# print(num_tab_ok)
result = 0
for number_ok in num_tab_ok:
    result += int(number_ok)

print(result)

