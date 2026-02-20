import csv
import matplotlib.pyplot as plt

# plt.title('codingssam minam')
# plt.plot([10,20,30,40])

# plt.title('two graph')
# plt.plot([10,20,30,40], label='up')
# plt.plot([40,30,20,10], label='down')
# plt.legend() #legend: 범례

# plt.title('color')
# plt.plot([10,20,30,40],color = 'skyblue',label = 'skyblue')
# plt.plot([40,30,20,10],label = 'magenta', color= 'indigo')
# plt.legend()

# plt.title('linestyle')
# plt.plot([10,20,30,40],color = 'r',linestyle ='solid',label='dashed')
# plt.plot([40,30,20,10],color = 'g',ls=':', label = 'dotted')
# plt.legend()

plt.title('marker')
plt.plot([10,20,30,40],'r.', ls='--',label='circle')
plt.plot([10,30,20,40],color = 'black',ls = 'solid',label='triangle up')
plt.plot([40,30,20,10],'g^',label = 'triangle up')
plt.legend()
plt.show()