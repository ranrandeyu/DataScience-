import numpy as np
from numpy.linalg import inv,qr
import random
x=np.array([[1.,2.,3.],[4.,5.,6.]])
y=np.array([[6.,23.],[-1.,7.],[8,9]])
#print(x.dot(y))#np.dot(x,y)
#print(np.ones(3))
a=np.random.randn(5,5)
mat=a.T.dot(a)
#print(inv(mat))
'''[[  8.01395061 -18.29825317   2.25172616   6.98629543 -16.80496922]
 [-18.29825317  45.76457786  -4.87049396 -17.14032114  41.3461916 ]
 [  2.25172616  -4.87049396   1.01894499   2.01749784  -4.34507029]
 [  6.98629543 -17.14032114   2.01749784   6.67573385 -15.56961495]
 [-16.80496922  41.3461916   -4.34507029 -15.56961495  37.80976139]]'''
#print(mat.dot(inv(mat)))
q,r=qr(mat)
#print(r)
'''[[-6.70253617  0.85720062 -2.8785142   0.41148489 -0.74245725]
 [ 0.         -4.73962087 -5.37441717  5.24694661  0.83546209]
 [ 0.          0.         -9.43773042  9.96777463  2.04494933]
 [ 0.          0.          0.         -1.35012538  1.12608335]
 [ 0.          0.          0.          0.          0.04985757]]'''

#随机漫步(前100个随机漫步值生成的折线图，从0开始，步长为1和-1，且以相等的概率出现)
position=0
walk=[position]
steps=200
for i in range(steps):
    step=1 if random.randint(0,1) else -1
    position+=step
    walk.append(position)

from matplotlib import pyplot as plt
from pandas import DataFrame
frame=DataFrame(walk)
plt.plot(frame)
#plt.show()
#一次模拟多个随机漫步
nwalkers=3
nsteps=1000
draws=np.random.randint(0,2,size=(nwalkers,nsteps))
steps=np.where(draws>0,1,-1)
walks=steps.cumsum(1)
frame2=DataFrame(walks)
plt.plot(frame2.T)
plt.show()


