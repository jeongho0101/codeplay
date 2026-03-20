import csv
import matplotlib.pyplot as plt

f = open('python_data/csv_data/mf.csv','r', encoding = 'utf8')
data = csv.reader(f)

data2 = []
for i in data:
    data2.append(i)
data = 0
f.close()
m = []#남성 연령대
f = []#여성 연령대
irum = ""
result = []
running = True
go = False


while running:
    irum = input("비교할 지역명 입력(그만하려면 q를 입력하세요)->")
    for row in data2:
        if irum in row[0]:
            go = True
            for i in range(101):
                m.append(-int(row[(i+3)]))
                f.insert(0,int(row[(-(i+1))]))
            break
        elif irum == 'q' or irum == 'Q':
            running = False

    if go:
        plt.style.use('ggplot')
        plt.figure(figsize=(10,5),dpi=150)
        plt.rc('font', family = 'Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title(f"양평군 {irum} 성별분포")
        plt.barh(range(101),m,label = "남성")
        plt.barh(range(101),f,label = "여성")
        plt.legend()
        plt.show()
    else:
        print(f"{irum}지역은 없습니다. 다시 입력해주세요.")

