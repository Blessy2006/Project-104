import csv
from collections import Counter

with open("SOCR-HeightWeight.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

newData = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    newData.append(float(n_num))

data = Counter(newData)
mode = {
            "75-85":0,
            "85-95":0,
            "95-105":0
            }   

for height, occurencee in data.items():
    if 75 < float(height) < 85:
        mode["75-85"] += occurencee
    elif 85 < float(height) < 95:
        mode["85-95"] += occurencee 
    elif 95 < float(height) < 105:
        mode["95-105"] += occurencee  

mode_range, mode_occurence = 0,0

for range, occurencee in mode.items():
    if occurencee > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurencee

Mode = float((mode_range[0] + mode_range[1])/2)   
print("Mode is " + str(mode))     