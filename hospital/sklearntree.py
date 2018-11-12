# -*- coding: UTF-8 -*-
from sklearn.preprocessing import LabelEncoder
from sklearn.externals.six import StringIO
from sklearn import tree
import pandas as pd
import pydotplus
from sklearn.model_selection import train_test_split
from math import log

if __name__ == '__main__':
	with open('tree.txt','r') as fr:
		# strip移除字符串头尾指定的空格
		reader=[tree.strip().split('\t') for tree in fr.readlines()]
		#print(reader)
	#存放trip的可能性
	trip_target =[]
	for each in reader:
		trip_target.append(each[3])
	#print(trip_target)

	#条件标签
	triplables=['walk','blood','chro']
	#特诊标签
	triplist=[]
	#保存reader数据的临时列表
	tripdict={}
	for each_lable in triplables:
		for each in reader:
			#for in range()中，item属于int类型,而非list类型
			triplist.append(each[triplables.index(each_lable)])
			#标签下面的参数赋给字典中对应的值
		tripdict[each_lable]=triplist
			#print(each_lable)
			#print(triplist)
		triplist=[]
			#print(tripdict)

	trip_pd=pd.DataFrame(tripdict)
	#print(trip_pd)

	#秩序化
	re=LabelEncoder()
	for i in trip_pd.columns:
		trip_pd[i]=re.fit_transform(trip_pd[i])
	#print(trip_pd)

	trees=tree.DecisionTreeClassifier(max_depth=6)
	trees=trees.fit(trip_pd.values.tolist(),trip_target)
	#print(trees)
	'''DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=4,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best')'''
	#StringIO模块主要用于在内存缓冲区中读写数据。模块是用类编写的，只有一个StringIO类
	data=StringIO()
  #print(data)
	tree.export_graphviz(trees,out_file=data,
						 feature_names=trip_pd.keys(),
						 class_names=trees.classes_,
						 filled=None,rounded=True,
						 special_characters=True)
	#data.gatvalue返回data中的所有数据
	graph=pydotplus.graph_from_dot_data(data.getvalue())
	graph.write_pdf('trip9.pdf')
