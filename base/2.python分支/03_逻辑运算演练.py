# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
# 要求人的年龄在 0-120 之间

age = int(input('请输入您的年龄：'))

if age > 0 and age <= 120:
    print('真人来了')
else:
    print('仙人来了')
