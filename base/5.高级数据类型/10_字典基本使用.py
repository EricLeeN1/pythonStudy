'''
@Author: your name
@Date: 2020-01-14 15:41:45
@LastEditTime : 2020-01-14 15:48:03
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\5.高级数据类型\10_字典基本使用.py
'''
xiaoming_dict = {'name': '小明'}

# 取值
print(xiaoming_dict['name'])

# 2、增加/修改
xiaoming_dict['age'] = 18
xiaoming_dict['name'] = '小明明'

# 3、 删除
xiaoming_dict.pop('name')
print(xiaoming_dict)