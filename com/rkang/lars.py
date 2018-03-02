"""
加载糖尿病患者数据：AGE、SEX、BMI、map（平均血压）、TC总胆固醇、LDL低密度脂蛋白、HDL高密度脂蛋白、TCH总胆固醇、LTG甘油三酯、GLU血糖、第2年血糖
共442个样例数据，10个变量，预测第2年的血糖
AGE	SEX  BMI	 BP	 TC	 LDL	HDL	TCH  LTG	GLU	 Y
59	2	32.1	101	157	93.2	38	4	4.8598	87	151
48	1	21.6	87	183	103.2	70	3	3.8918	69	75
72	2	30.5	93	156	93.6	41	4	4.6728	85	141
24	1	25.3	84	198	131.4	40	5	4.8903	89	206
"""
import numpy as np
from sklearn import preprocessing
from sklearn import linear_model
#加载数据，去掉表头
diabetes = np.loadtxt("e:/diabetes.npy")
#加载变量数据
data = diabetes[:, :-1]
#加载目标数据（第二年血糖值）
target = diabetes[..., -1]
#对数据进行中心化和标准化
X_scaled = preprocessing.scale(diabetes)
# print(X_scaled.mean(axis=0)) # 平均值
# print(X_scaled.std(axis=0))  # 方差

#计算相关系数
coef = np.corrcoef(X_scaled.T)
#各个变量针对Y（第2年血糖）值的相关系统
coef_y = coef[..., -1]
print("各个因子对第二年血糖的相关系数")
titles = ['年龄-X1','性别-X2','BMI-X3','平均血压-X4','TC总胆固醇-X5','LDL低密度脂蛋白-X6','HDL高密度脂蛋白-X7','TCH总胆固醇-X8','LTG甘油三酯-X9','GLU血糖-X10','第二年血糖']
for key,value in zip(titles,coef_y):
    print(key,':',"{0:.7f}".format(value))


print(X_scaled)
X_data = X_scaled[:,[2,8,3,6,9]]
y_data = target

print(X_data)
print(y_data)

reg = linear_model.LinearRegression(fit_intercept=True)
reg.fit(X_data,y_data)
print('线性回归方程对应的系数:',reg.coef_)
print('线性回归方程对应的截距:',reg.intercept_)

y_pre = reg.predict(X_data)

print(y_pre[-10:])
print(y_data[-10:])











