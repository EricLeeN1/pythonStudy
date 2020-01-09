'''
@Author: your name
@Date: 2020-01-09 16:52:43
@LastEditTime : 2020-01-09 17:08:23
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\04_函数\08_打印分割线.py
'''


def print_line(char, time=10):
    print(char*time)


def print_lines(row):
    row = 0
    while row < 5:
        print_line('-', row * 10)
        row += 1
