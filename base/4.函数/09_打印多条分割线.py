'''
@Author: your name
@Date: 2020-01-09 16:52:43
@LastEditTime : 2020-01-11 09:55:30
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\04_函数\08_打印分割线.py
'''


def print_line(char, time=10):
    print(char*time)


def print_lines(char, time):
    """
    打印多行分割线
    :param char: 分割线使用的分隔字符
    :param time:分割线重复的次数
    """
    row = 0
    while row < 5:
        print_line(char, time)
        row += 1


print_lines('-', 20)
