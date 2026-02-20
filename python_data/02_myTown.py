import csv
import matplotlib.pyplot as plt
f = open('python_data\csv_data\yp2025.csv','r', encoding='utf8')
data = csv.reader(f, delimiter=',')
yp = [] #데이터 불러오기

for row in data:
    yp.append(row)