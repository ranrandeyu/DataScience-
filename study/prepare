import numpy as np
import time
import matplotlib.pyplot as plt

#numpy计算求和速度快
def sum_numpy():
    start=time.time()
    x=np.arange(100000)
    y=np.arange(100000)
    z=x+y
    print(z)
    return time.time()-start
print(sum_numpy())

#random随机选取元素创建数组，将创建的数组的长度作为permutation、函数的参数传入
print(np.random.permutation(3))
#参数为0的正态分布均值，1为标准差，5为个数
print(np.random.normal(0,1,5))

#二位列表元素的表示
matrix=np.array([[4.,5.,6.],[2,3,6]],float)
print(matrix[1,1])
arr=np.array([[4. ,5. ,6.,8.],[2. ,3. ,6. ,7.]],float)
#第0列加第1列的第1个元素
print(arr[0:2,1:2])

#transpose可以互换维度,T转置
print(arr.transpose())
print(arr.T)

#concatenate用于连接，axis=0列
arr1=np.array([[11,12],[22,44]],float)
arr2=np.array([[23,55],[21,77]],float)
print(np.concatenate((arr1,arr2),axis=0))
'''[[11. 12.]
 [22. 44.]
 [23. 55.]
 [21. 77.]]'''
print(np.concatenate((arr1,arr2),axis=1))
'''[[11. 12. 23. 55.]
 [22. 44. 21. 77.]]'''

#数组支持按条件查询
print(arr1[arr1>12])
#构造目标索引
arr3=np.array([0,1,1,1],int)
print(arr1[arr3])

#matplotlib折线图
#(0,9),(1,0),(2,2),(3,5)
plt.plot([9,0,2,5],color='green',label='line 1', linewidth=5)
plt.ylabel('y',fontsize=40)
plt.xlabel('x',fontsize=40)
#x轴的范围[0,3],y轴范围[0,15]
plt.axis([0,3, 0,15])
plt.show()

#散点图
colors = ['b', 'c', 'y', 'm', 'r']
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.scatter(np.random.random(10), np.random.random(10), marker='x', color=colors[0])
p1 = ax.scatter(np.random.random(10), np.random.random(10), marker='x', color=colors[0],s=50)
p2 = ax.scatter(np.random.random(10), np.random.random(10), marker='o', color=colors[1],s=50)
p3 = ax.scatter(np.random.random(10), np.random.random(10), marker='o', color=colors[2],s=50)
ax.legend((p1,p2,p3),('points 1','points 2','points 3'),fontsize=20)
ax.set_xlabel('x',fontsize=40)
ax.set_ylabel('y',fontsize=40)
fig.savefig('figure_scatterplot.png')
plt.show()
