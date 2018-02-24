import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(-4,5)
x=np.linspace(-np.pi,np.pi,256,endpoint=True)
print(x)
C,S=np.cos(x),np.sin(x)
print(C)
print(S)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.title("正弦余弦演示")
plt.xlabel("x value")
plt.ylabel("cos/sin")
plt.plot(x,C)
plt.plot(x,S)
plt.show()
print(np.pi)