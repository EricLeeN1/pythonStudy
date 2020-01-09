'''
@Author: your name
@Date: 2020-01-09 10:34:45
@LastEditTime : 2020-01-09 10:35:56
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\3.python循环while\08_print函数的结尾.py
'''
# - 在默认情况下，print 函数输出内容之后，会自动在内容末尾增加换行
# - 如果不希望末尾增加换行，可以在 print 函数输出内容的后面增加 , end=""
# - 其中 "" 中间可以指定 print 函数输出内容之后，继续希望显示的内容
i = 0
while i < 5:
    i += 1
    print('*' * i, end="/")
