import knn
from numpy import *
#生成数据集和类别标签
dataSet,labels = knn.createDataSet()
#定义一个未知类别的数据
testX = array([5.9, 3.1, 5.1, 1.8])
k=3
#调用分类函数对未知数据分类
outputLabel = knn.kNNClassify(testX, dataSet, labels, 3)
print("Your input is:", testX, " and classified to class:", outputLabel)
