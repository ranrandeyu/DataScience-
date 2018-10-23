import pandas as pd
import json
result=pd.read_csv('housing.csv',header=None)
#python转化为json格式
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
result=json.dumps(data)
#print("Python 原始数据：",repr(result))
#print("Json 对象:",result)
#json转换为python格式
data2=json.loads(result)

#读取excel文件
#xls=pd.ExcelFile('data.xls')

#API的调用
import requests
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
resp=requests.get(url)
#print("status",resp.status_code)获取状态码
response_dict=resp.json()
print(response_dict)
#print("Total repositories",response_dict['total_count'])#将API响应存储在一个变量中，这个API返回JSON格式的信息，使用方法json把这些信息转换为一个python字典
