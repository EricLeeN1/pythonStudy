# 1、输入苹果单价
price = float(input('请输入苹果价格：'))
# 2、输入苹果重量
weight = float(input('请输入苹果重量：'))
# 3、计算金额
money = price * weight
# 4、打印金额
print("苹果单价%.02f元，购买了%.02f斤，总共%.02f 元钱" % (price, weight, money))
12.5