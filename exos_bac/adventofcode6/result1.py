import sys
file = sys.argv[1]

with open(file, 'r') as File:
    fichier = File.read()

race_time_records = fichier.split("\n")
tab1 = race_time_records[0].split(" ")
tab2 = race_time_records[1].split(" ")
race_time = []
race_record = []
for elem in tab1:
    if elem.isnumeric():
        race_time.append(int(elem))
for elem in tab2:
    if elem.isnumeric():
        race_record.append(int(elem))

def distance_by_second(race_time, button_time):
    distance = button_time*(race_time  - button_time)
    return distance

wins_tab = []
for k in range(len(race_time)):
    win = 0
    for i in range(race_time[k]+1):
        if distance_by_second(race_time[k], i) > race_record[k]:
            win += 1
    wins_tab.append(win)

result = 1
for wins in wins_tab:
    result *= wins

print(result)
