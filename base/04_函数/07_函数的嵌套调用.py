'''
@Author: your name
@Date: 2020-01-09 16:45:12
@LastEditTime : 2020-01-09 16:48:07
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\04_函数\07_函数的嵌套调用.py
'''


def test1():
    print('*' * 50)


def test2():
    print('-'*50)

    test1()
    print('@'*50)


test2()
