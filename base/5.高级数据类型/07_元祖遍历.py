'''
@Author: your name
@Date: 2020-01-14 14:51:15
@LastEditTime : 2020-01-14 14:54:31
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\5.高级数据类型\07_元祖遍历.py
'''
info_tuple = ('张三', 18, 1, 75)

# 使用迭代遍历元祖

for my_info in info_tuple:
    # 使用格式字符串拼接 my_info 这个变量不方便
    # 因为元祖中通常保存的数据类型是不同的
    print(my_info)
