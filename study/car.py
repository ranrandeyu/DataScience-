import pandas as pd
import numpy as np

df=pd.read_csv('data_cars.csv',header=None)
#列定义为category，并按我们想要的查看方式设置顺序
for i in range(len(df.columns)):
    df[i]=df[i].astype('category')
df.head()
print(df)
#将特征值转换为分类算法中的数字
map0=dict(zip(df[0].cat.categories,range(len(df[0].cat.categories))))
map1=dict(zip(df[1].cat.categories,range(len(df[1].cat.categories))))
map2=dict(zip(df[2].cat.categories,range(len(df[2].cat.categories))))
map3=dict(zip(df[3].cat.categories,range(len(df[3].cat.categories))))
map4=dict(zip(df[4].cat.categories,range(len(df[4].cat.categories))))
map5=dict(zip(df[5].cat.categories,range(len(df[5].cat.categories))))
map6=dict(zip(df[6].cat.categories,range(len(df[6].cat.categories))))



cat_cols=df.select_dtypes(['category']).columns
df[cat_cols]=df[cat_cols].apply(lambda  x:x.cat.codes)
df=df.iloc[np.random.permutation(len(df))]
print(df.head())

#编写标准函数，将类别标签向量y和特征值x分开
df_f1=pd.DataFrame(columns=['method']+sorted(map6,key=map6.get))
df_prediction=pd.DataFrame(columns=['method']+sorted(map6,key=map6.get))
df_recall=pd.DataFrame(columns=['method']+sorted(map6,key=map6.get))
def calcmeasures(method,y_pred,y_true,df_f1=df_f1,df_precision=df_prediction,df_recall=df_recall):
    df_f1.loc[len(df_f1)]=[method]+list(f1_score(y_pred,y_true,average=None))
    df_prediction.loc[len(df_prediction)]=[method]+list(precision_score(y_pred,y_true,average=None))
    df_recall.loc[len(df_recall)]=[method]+list(recall_score(y_pred,y_true,average=None))
x=df[df.columns[:-1]].values
y=df[df.columns[-1]].values
#print(x)
print(y)
