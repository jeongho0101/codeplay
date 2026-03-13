import csv
import matplotlib.pyplot as plt

#plt.bar([0,1,2,4,6,10],[1,2,3,5,6,7])#표시할 위치/막대 그래프 높이
# plt.barh(range(6),[1,2,3,5,6,7])#range함수로 위치설정 가능능
# plt.show()

f = open('python_data/csv_data/yp2025.csv','r', encoding = 'utf8')
data = csv.reader(f)
result = []
for row in data:
    if '양평읍' in row[0]:
        for i in row[3:]:
            result.append(int(i))
plt.bar(range(101), result)
plt.barh(range(101), result)
plt.show()