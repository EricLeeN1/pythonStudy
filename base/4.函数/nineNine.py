'''
@Author: eric
@Date: 2020-01-09 15:33:10
@LastEditTime : 2020-01-09 15:42:09
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\04_函数\01_九九乘法表.py
'''
# 九九乘法表
# coding:utf-8

def multiple_table():

    row = 0
    while row < 9:
        row += 1
        col = 0

        while col < row:
            col += 1
            # end = ""，表示输出结束后，不换行
            # "\t" 可以在控制台输出一个制表符，协助在输出文本时对齐
            print('%d * %d = %d' % (col, row, row*col), end='\t')
        print('')
