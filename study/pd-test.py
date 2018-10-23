import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

#索引在左边，值在右边
obj=Series([4,7,-5,3],index=['d','b','a','c'])
#print(obj)
'''d    4
b    7
a   -5
c    3
dtype: int64'''
#print(obj.index)
'''Index(['d', 'b', 'a', 'c'], dtype='object')'''
#通过Series来创建字典
sdata={'first':1,'second':2,'third':3}
obj1=Series(sdata)
obj1.name='test'
obj1.index.name='state'
#print(obj1)
'''state
first     1
second    2
third     3
Name: test, dtype: int64'''
obj2={'state':['ohio','ohio','nev','now'],'year':[2000,2001,2002,2003],'pop':[1.2,1.4,2.3,4.2]}
frame=DataFrame(obj2)
#print(frame)
'''  state  year  pop
0  ohio  2000  1.2
1  ohio  2001  1.4
2   nev  2002  2.3
3   now  2003  4.2'''
frame2=DataFrame(obj2,columns=['year','state','pop','debt'],index=['one','two','three','four'])
frame2['debt']=np.arange(4.)
#print(frame2)
#ffill可以实现向数字大的填充
obj3=Series(['blue','purple','yellow'],index=[0,1,4])
#print(obj3.reindex(range(6),method='pad'))
'''0      blue
1    purple
2    purple
3    purple
4    yellow
5    yellow
dtype: object'''

df1=pd.DataFrame(np.arange(12).reshape((3,4)),columns=list('abcd'))
df2=pd.DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'))
#print(df1+df2)#算术运算和数据对齐df1+df2
'''      a     b     c     d   e
0   0.0   2.0   4.0   6.0 NaN
1   9.0  11.0  13.0  15.0 NaN
2  18.0  20.0  22.0  24.0 NaN
3   NaN   NaN   NaN   NaN NaN'''
#print(df1.sub(df2,fill_value=0))#df1.sub(df2,fill_value=0)
''' a     b     c     d     e
0   0.0   0.0   0.0   0.0  -4.0
1  -1.0  -1.0  -1.0  -1.0  -9.0
2  -2.0  -2.0  -2.0  -2.0 -14.0
3 -15.0 -16.0 -17.0 -18.0 -19.0'''

#映射
df = pd.DataFrame(np.random.randint(0,10,(4, 3)), columns=list('bde'), index=range(4))
f =lambda x : x.max()-x.min()
df.apply(f)
format=lambda x:'%.2f'%x
#print(df.applymap(format))
'''      b     d     e
0  1.00  9.00  4.00
1  6.00  6.00  1.00
2  8.00  6.00  0.00
3  1.00  1.00  5.00'''
#print(df['b'].map(format))
'''0    8.00
1    6.00
2    7.00
3    6.00
Name: b, dtype: object'''
#唯一值和值计数
obj4=Series(['c','a','a','s','q'])
uniques=obj4.unique()
#print(uniques)
#print(obj4.value_counts())
'''['c' 'a' 's' 'q']'''

#滤掉缺失数据
from numpy import nan as NA
data=Series([1,NA,3.4,NA,7])
#print(data.dropna())&&data[data.notnull()]
'''
0    1.0
2    3.4
4    7.0
dtype: float64
'''
#pd.DataFrame可以实现删去不显示的效果，Series不能显示出来
data1=pd.DataFrame([[1,NA,3,4,NA,7],[NA,NA,NA,NA,NA,NA],[0,3,45,66,2,4]])
#data1=Series([[1.,NA,34.,NA,7.],[NA,NA,NA,NA,NA],[0.,3.,45.,66.,2.,4.]])
#舍去包含NA的行
clean=data1.dropna()
'''(pd.DataFrame)     
0    1     2     3    4    5
2  0.0  3.0  45.0  66.0  2.0  4.0
(Series)
0        [1, nan, 3.4, nan, 7]
1    [nan, nan, nan, nan, nan]
2         [0, 3, 45, 66, 2, 4]
'''
#舍去全部是NA的行
data1.dropna(how='all')

#填充缺失数据(中位数)
data1.fillna(data1.mean())
#层次化索引
data3=Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])
data3[:,2]
'''
a   -0.385473
b   -0.355493
c   -1.002782
d    2.110874'''
data3.unstack()

