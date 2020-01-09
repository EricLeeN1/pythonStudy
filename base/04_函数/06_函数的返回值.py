'''
@Author: your name
@Date: 2020-01-09 16:32:49
@LastEditTime : 2020-01-09 16:42:15
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\04_函数\05_函数参数.py
'''


def sum_2_num(num1, num2):
    """对两个数字的求和"""
    result = num1 + num2

    # 可以使用返回值，告诉调用函数一方计算的结果
    return result


# sum_2_num(1, 2)

result = sum_2_num(1, 2)

print(result)
