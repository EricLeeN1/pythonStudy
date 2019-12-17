# 1、输入苹果的单价
price_str = input("苹果的单价：")
# 2、输入苹果的重量
weight_str = input("苹果的重量：")

# 将价格转换为小数
price = float(price_str)
# 将重量转换为小数
weight = float(weight_str)
# 用两个小数来计算最终的金额
money = price * weight

print(money)