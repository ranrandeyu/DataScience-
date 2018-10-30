import pandas as pd
import numpy as np
import json
import csv
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as plt
#使用csv的格式读取文件
'''with open("ttt.csv", "rt", encoding="utf-8") as vsvfile:
  reader = csv.reader(vsvfile)
  hypertension = [row[1] for row in reader]
  hypertension_result=json.dumps(hypertension)
  low = [row[2] for row in reader]
  low_result=json.dumps(low)
  sleep=[row[3] for row in reader]
  sleep_result=json.dumps(sleep)
  wine=[row[4] for row in reader]
  wine_result=json.dumps(wine)
  id=[row[0] for row in reader]'''
#用pd来读取文件
reader=pd.read_csv('ttt.csv',header=None)
print(reader)
hypertension=DataFrame(reader[0])
low=DataFrame(reader[1])
sleep=DataFrame(reader[2])
wine=DataFrame(reader[3])
#获得行数【0】，列数为【1】
nrows=reader.shape[0]-1
#获取记录
record=reader[1:]
print(record)
#删去含有NAN的项
clean_all=record.dropna()
cl_all_nrows=clean_all.shape[1]
#print(cl_all_nrows)
#print(clean_all)
print(sleep)
y_axis=[1,5,10,15]
#p1 = plt.bar(left=0,bottom=low , width=y, color='yellow',height=0.5, orientation='horizontal')
x_axis = tuple(sleep.keys())
plt.bar(x_axis, y_axis, color='rgb')
plt.show()                                                                                                      
low=low.replace([0,1,2,3],['b0','b1','b2','b3'])
hypertension=hypertension.replace([0,1,2],['a0','a1','a2'] )
sleep=sleep.replace([0,1,2,3,4],['c0','c1','c2','c3','c4'] )
wine=wine.replace([0,1,2,3],['d0','d1','d2','d3'] )


