import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2 * x +1
y2 = x ** 2

plt.figure()
line1, = plt.plot(x,y1)
line2, = plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--')

#设置坐标轴的取值范围
plt.xlim((-1,1))
plt.ylim((0,2))

#设置坐标轴的label
plt.xlabel('x axis')
plt.ylabel('y axis')

#设置坐标轴的刻度，把默认的0.25改成0.5
plt.xticks(np.linspace(-1,1,5))
plt.yticks([0,0.5],['$minimum$','normal'])

plt.legend(handles=[line1,line2],labels=['2*x+1','x**2'],loc='best')

plt.show()