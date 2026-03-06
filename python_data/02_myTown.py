import csv
import matplotlib.pyplot as plt
f = open('python_data\csv_data\yp2025.csv','r', encoding='utf8')
data = csv.reader(f, delimiter=',')
yp = [] #데이터 불러오기

for row in data:
    yp.append(row)

for i in yp:
    for j in range(3,len(i)):
        if ',' in i[j]:
            i[j] = i[j].replace(',','')
        i[j] = int(i[j])

running = True
while running:
    yp_select = []
    yp_names = []
    for bigyo in range(2):
        area = input("지역명 입력:")
        if area == "끝":
            running = False
            break
        yp_names.append(area)
        for local in yp:
            if area in local[0]:
                yp_select.append(local[3:])

    if len(yp_names)==2:
        plt.rc('font', family = 'Malgun Gothic')
        plt.title("양평군 인구분포도")
        plt.style.use('ggplot')

        area1 = f'{yp_names[0]} (총 인구수 : {sum(yp_select[0])})'
        area2 = f'{yp_names[1]} (총 인구수 : {sum(yp_select[1])})'

        plt.plot(yp_select[0], label = area1)
        plt.plot(yp_select[1], label = area2)
        plt.legend()
        plt.show()

print("잘가가가가가가가가가가가가가가가가가가가가가가가가가가가")