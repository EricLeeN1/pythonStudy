# 计算 0 ~ 100 之间所有数字的累计求和结果
# 0. 定义最终结果的变量
result = 0

# 1. 定义一个整数的变量记录循环的次数
i = 0

while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1


print('0-100偶数相加之和最后结果是result:%d' % result)
