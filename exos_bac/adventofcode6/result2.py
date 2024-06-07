import sys
file = sys.argv[1]

with open(file, 'r') as File:
    fichier = File.read()

race_time_records = fichier.split("\n")
tab1 = race_time_records[0].split(" ")
tab2 = race_time_records[1].split(" ")
racetime = ''
racerecord = ''
for elem in tab1:
    if elem.isnumeric():
        racetime+= elem
race_time = int(racetime)
for elem in tab2:
    if elem.isnumeric():
        racerecord += elem
race_record = int(racerecord)

def distance_by_second(race_time, button_time):
    distance = button_time*(race_time  - button_time)
    return distance

# win = 0
# for i in range(race_time + 1):
#     if distance_by_second(race_time, i) > race_record:
#         win += 1
#     print(i)

# print(win)
def first_i(race_time):
    for i in range(race_time + 1):
        if distance_by_second(race_time, i) > race_record:
            return i

def last_i(race_time):
    for i in reversed(range(race_time + 1)):
        if distance_by_second(race_time, i) > race_record:
            return i
        
print(last_i(race_time) - first_i(race_time) +1)