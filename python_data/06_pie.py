import matplotlib.pyplot as plt

# plt.pie([10,20])

# size = [2441, 2312, 1031, 1233]
# plt.axis('equal')
# plt.pie(size)

# plt.rc('font', family = 'Malgun Gothic')
# size = [2441, 2312, 1031, 1233, 555]
# label =['A형','B형','AB형','O형','우리형']
# plt.axis('equal')
# plt.pie(size, labels = label)

plt.rc('font', family = 'Gulim')
blood = [1125,2312,1031,2733]
label = ['A형','B형','AB형','O형']
color = ['darkmagenta','deeppink','hotpink','pink']
ddi = [1,2,3,4,5,6,7,8,9,10,11,12]
label2 = ["쥐","소","호랑이","토깽이","드래곤","뱀","말","양","원숭이","닭","개","돼지"]
fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(10,8))

axes[0].pie(blood, explode=(0,0,0,0.1),labels=label, autopct='%.1f%%')
axes[0].set_title('비율')
axes[1].pie(ddi, explode=(0,0,0,0,0.1,0,0,0,0,0,0,0),labels=label2, autopct='%.1f%%')
axes[1].set_title('돌출')

# plt.axis('equal')
# plt.pie(size, labels=label, autopct='%.1f%%')
# plt.legend()

# plt.axis('equal')
# plt.pie(size, explode=(0,0,0,0,2),labels=label, autopct='%.1f%%',colors=color)
# plt.legend()

plt.show()
