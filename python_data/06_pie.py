import matplotlib.pyplot as plt

plt.pie([10,20])

# size = [2441, 2312, 1031, 1233]
# plt.axis('equal')
# plt.pie(size)

# plt.rc('font', family = 'Malgun Gothic')
# size = [2441, 2312, 1031, 1233, 555]
# label =['A형','B형','AB형','O형','우리형']
# plt.axis('equal')
# plt.pie(size, labels = label)

# plt.rc('font', family = 'Gulim')
# size = [1125,2312,1031,2733]
# label = ['A형','B형','AB형','O형']
# color = ['darkmagenta','deeppinlk','hotpink','pink']

# fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(10,8))


# axes[0].pie(size, labels=label, autopct='%.1f%%')
# axes[0].set_title('비율')

# axes[1].pie(size, explode=(0,0,0,0,2),labels=label, autopct='%.1f%%',colors=color)
# axes[1].set_title('돌출')

# plt.axis('equal')
# plt.pie(size, labels=label, autopct='%.1f%%')
# plt.legend()

# plt.axis('equal')
# plt.pie(size, explode=(0,0,0,0,2),labels=label, autopct='%.1f%%',colors=color)
# plt.legend()

plt.show()
