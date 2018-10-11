from numpy import *
import flower

# 创建一个数据集
def createDataSet():
    # 生成一个矩阵，每行表示一个样本
    group=flower.iris_X
    #group = array([[5.1, 3.5,1.4 ,0.2]，[4.9 ,3,1.4 ,0.2],[6.5 ,3. ,5.2, 2. ],[6.2, 3.4, 5.4, 2.3]])
    # 4个样本分别所属的类别
    labels=flower.iris_y
    #labels = ['0', '0', '2', '2']
    return group, labels

# KNN分类算法函数定义
def kNNClassify(newInput, dataSet, labels, k):
    numSamples = dataSet.shape[0]   # shape[0]表示行数
    # # step 1: 计算距离
    diff = tile(newInput, (numSamples, 1)) - dataSet  # 按元素求差值
    squaredDiff = diff ** 2  # 将差值平方
    squaredDist = sum(squaredDiff, axis = 1)   # 按行（axis=1）累加
    distance = squaredDist ** 0.5  # 将差值平方和求开方，即得距离

    # # step 2: 对距离排序
    # argsort() 返回排序后的索引值
    sortedDistIndices = argsort(distance)
    classCount = {} # define a dictionary (can be append element)
    for i in range(k):

        # # step 3: 选择k个最近邻
        voteLabel = labels[sortedDistIndices[i]]

        # # step 4: 计算k个最近邻中各类别出现的次数
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    # # step 5: 返回出现次数最多的类别标签
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex

