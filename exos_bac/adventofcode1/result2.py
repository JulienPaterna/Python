import sys
import re

with open(sys.argv[1]) as f:
    fichier = f.read()

def as_int_start(string):
    tab_number_letter = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tab_number = ["1","2","3","4","5","6","7","8","9"]
    for number in tab_number_letter:
        if string[0] == number[0]:
            i = 1
            while i < len(number):
                try:
                    if string[i] == number[i]:
                        i += 1
                    else:
                        i += 10
                except:
                    i += 10
            if i == len(number):
                string = tab_number[tab_number_letter.index(number)]
                return string                    
    return False
    
def as_int_end(string):
    tab_number_letter = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tab_number = ["1","2","3","4","5","6","7","8","9"]
    for number in tab_number_letter:
        if len(string) > 0:
            if string[len(string) - 1] == number[len(number) - 1]:
                i = - 2
                while i >= -len(number):
                    try:
                        if string[len(string) + i] == number[len(number) + i]:
                            i -= 1
                        else:
                            i -= 10
                    except:
                        i -= 10
                if i == -len(number) - 1:
                    string = tab_number[tab_number_letter.index(number)]
                    return string    
        else:
            return False                
    return False

def adding(fichier):
    tab = fichier.split("\n")
    tot_sum = 0
    for line in tab:
        sum = ""
        i = 0
        stop = False
        l = len(line)
        while i < len(line) and stop == False:
            string = as_int_start(line[i:])
            if line[i].isnumeric() == True:
                sum += line[i]
                try:
                    line = line[i+1:]
                except:
                    line = []
                stop = True
            elif string != False:
                sum += string
                line = line[i+1:]
                stop = True
            else:
                i += 1
        if i == l:
            sum = "0"
        stop = False
        string = as_int_end(line)
        while len(line) >= 1 and stop == False:
            string = as_int_end(line)
            if line[len(line) - 1].isnumeric() == True:
                sum += line[len(line) - 1]
                stop = True
            elif string != False:
                sum += string
                stop = True
            else:
                try:
                    line = line[:len(line) - 1]
                except:
                    line = []
        if line == "":
            sum += sum
        tot_sum += int(sum)
    return tot_sum

print(adding(fichier))


