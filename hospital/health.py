import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import xlrd
import json
import importlib
importlib.reload(sys)

# 设置编码格式
importlib.reload(sys)

# 1. 从Excel文件中读取出Book对象
data = xlrd.open_workbook('test.xlsx')
# print type(data)

# 2. 获取sheet页对象
sheet1 = data.sheet_by_index(0)


# 2.2 通过sheet名称获取
sheet2 = data.sheet_by_name(u'Sheet1')

# 3. 获取sheet页的行数和列数
nrows = sheet1.nrows
ncols = sheet1.ncols


# 4. 获取第0行的值（是一个列表）
row_data = sheet1.row_values(0)



# 5. 获取第0列的值（是一个列表）
col_data = sheet1.col_values(0)


# 6. 使用行列索引（从0开始）获取单元格的数据
cell_A1 = sheet1.cell(0,0)


# 7. 应用：将Excel文件中的数据转换成json数组
# 索引（即表头）
idx = sheet1.row_values(0)
# 最终的数据列表
data = []
# 从第1行开始遍历循环所有行，获取每行的数据
for i in range(1,nrows):
    row_data = sheet1.row_values(i)
    # 组建每一行数据的字典
    row_data_dict = {}
    # 遍历行数据的每一项，赋值进行数据字典
    for j in range(len(row_data)):
        item = row_data[j]
        row_data_dict[idx[j]] = item
        # 将年份字段转成整形
        row_data_dict['ID'] = int(row_data_dict['ID'])
    # 将行数据字典加入到data列表中
    data.append(row_data_dict)

print (json.dumps(data,indent = 4))
