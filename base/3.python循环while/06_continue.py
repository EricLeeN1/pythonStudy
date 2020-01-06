'''
@Author: your name
@Date: 2020-01-05 15:33:31
@LastEditTime : 2020-01-05 15:35:55
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\3.python循环while\06_continue.py
'''
i = 0

while i < 10:

    if i == 7:
        i += 1
        continue
        print('不会执行的')
    print(i)

    i += 1
