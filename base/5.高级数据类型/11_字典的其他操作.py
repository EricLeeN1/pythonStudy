'''
@Author: your name
@Date: 2020-01-14 15:51:43
@LastEditTime : 2020-01-14 15:55:53
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\5.高级数据类型\11_字典的其他操作.py
'''
xiaoming_dict = {'name': '小明'}

# 1、统计键值对数量

print(len(xiaoming_dict))  # 1

# 2、合并字典

temp_dict = {
    "height": 1.75,
    "name": "xiaoming"
}
# 注意：如果被合并的字典中包含已经存在的键值对时，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)

# 3、清空字典
xiaoming_dict.clear()

print(xiaoming_dict)
