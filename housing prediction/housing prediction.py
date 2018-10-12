import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 把数据转化成pandas的形式，在列尾加上房价PRICE
boston_dataset = datasets.load_boston()
#print(boston_dataset)
data = pd.DataFrame(boston_dataset.data)
#print(data)
data.columns = boston_dataset.feature_names
#print(data.columns)
data['PRICE'] = boston_dataset.target

# 距离高速公路的便利指数和房价并转化成矩阵形式
x = data.loc[:, 'RAD'].as_matrix(columns=None)
y = data.loc[:, 'PRICE'].as_matrix(columns=None)


# 进行矩阵的转置
x = np.array([x]).T
y = np.array([y]).T

# 训练线性模型
l = LinearRegression()
l.fit(x, y)

# 画图显示
#font = FontProperties(fname=r"c:\windows\fonts\Arial.ttc", size=14)
plt.scatter(x, y, s=10, alpha=0.5, c='green')
plt.plot(x, l.predict(x), c='blue', linewidth='1')
plt.xlabel("RAD")
plt.ylabel("Price")
plt.show()
