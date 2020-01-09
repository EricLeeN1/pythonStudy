'''
@Author: your name
@Date: 2020-01-09 10:36:43
@LastEditTime : 2020-01-09 10:42:45
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\3.python循环while\08_嵌套打印小星星.py
'''
# - 完成 5 行内容的简单输出
# - 2> 分析每行内部的 * 应该如何处理？
#   - 每行显示的星星和当前所在的行数是一致的
#   - 嵌套一个小的循环，专门处理每一行中 列 的星星显示

row = 0
# 开始循环
while row < 5:
    row += 1
    col = 1

    while col <= row:
        print("*", end="")
        col += 1

    print("")
