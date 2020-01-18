'''
@Author: your name
@Date: 2020-01-14 17:24:19
@LastEditTime : 2020-01-14 17:39:20
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\5.高级数据类型\16_字符串判断方法.py
'''
# 1、判断空白字符
space_str = ' \t\n\r'

print(space_str.isspace()) 

# 2、判断字符串中是否值包含数字

num_str = "1.1"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())