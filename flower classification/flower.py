from __future__ import print_function
from sklearn import datasets
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
#调用已经写好的knn
from sklearn.neighbors import KNeighborsClassifier

#通过python加载鸢尾花数据集数据：X 有四个属性，标签y 有 0，1，2 三类
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
#print(iris_X,iris_y)

#内部knn调用测试：predict 测试集的数据，knn训练出来的结果
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
#print(knn.predict(X_test))
#print(y_test)

#画散点，标注类别
X_2,X_1, X_0 = iris_X[iris_y == 2],iris_X[iris_y == 1],iris_X[iris_y == 0]
plt.scatter(X_2[:, 2], X_2[:, 3],marker = 'x',color = 'red', s = 40 ,label = 'Iris-virginica')
plt.scatter(X_1[:, 2], X_1[:, 3], marker = '+', color = 'blue', s = 40, label = 'versicolor')
plt.scatter(X_0[:, 2], X_0[:, 3],  marker = 'o', color = 'green', s = 40, label = 'setosa')
plt.legend(loc = 'best')
plt.show()
