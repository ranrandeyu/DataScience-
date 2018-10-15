#PCA实例，该数据集中的数据集沿直线y=2x分布，其中包含一些随机增加的噪声
import numpy as np
from matplotlib import  pyplot as plt

#line y=2*x
#arange 产生的范围
x = np.arange(1,101,1).astype(float)
y=2*np.arange(1,101,1).astype(float)
#add noise ；np.random.normal(mean,stdev,size)给出均值为mean，标准差为stdev的高斯随机数（场），当size赋值时，例如：size=100，表示返回100个高斯随机数
noise=np.random.normal(0,10,100)
y+=noise

fig=plt.figure(figsize=(10,10))
#plot
plt.plot(x,y,'ro')
plt.axis([0,102,-20,220])
plt.quiver(60,100,10-0,20-0,scale_units='xy',scale=1)
plt.arrow(60,100,10-0,20-0,head_width=2.5,head_length=2.5,fc='k',ec='k')
plt.text(70,110,r'$v^l$',fontsize=20)

#save
ax=fig.add_subplot(111)
ax.axis([0,102,-20,220])
ax.set_xlabel('x',fontsize=40)
ax.set_ylabel('y',fontsize=40)
fig.suptitle('2 dimensional dataset',fontsize=40)
fig.savefig('pca_data.png')
