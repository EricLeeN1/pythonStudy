# 在控制台连续输出五行 *，每一行星号的数量依次递增
# 定义一个计数器变量，从数字1开始，循环会比较方便，但一般循环都从0开始
i = 0
# 开始循环
while i < 5:
    i += 1
    print('*' * i, end="")
