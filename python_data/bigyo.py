import csv
import matplotlib.pyplot as plt

f = open('python_data/csv_data/10.csv','r', encoding = 'utf8')
data = csv.reader(f)
agge = []

for row in data:
    if '양평읍' in row[0]:
        for i in row[3:]:
            agge.append(int(i.replace(',','')))
        break
