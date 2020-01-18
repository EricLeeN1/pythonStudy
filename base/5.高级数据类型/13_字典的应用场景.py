'''
@Author: your name
@Date: 2020-01-14 16:05:17
@LastEditTime : 2020-01-14 16:10:58
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\5.高级数据类型\13_字典的应用场景.py
'''
# 使用多个键值对，存储描述一个物体的相关信息 -- 描述更复杂的数据信息
# 将 多个字典 放在一个列表中,再进行遍历

card_list = [
    {"name": "张三",
     "qq": "12312313",
     "phone": "1100"},
    {"name": "李四",
     "qq": "1312312321",
     "phone": "1231321"}]

for card_item in card_list:
    print(card_item)
