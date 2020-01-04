# 1. 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True
# 2. 定义整型变量 knife_length 表示刀的长度，单位：厘米
knife_length = 20
# 3. 首先检查是否有车票，如果有，才允许进行 安检
if has_ticket:
    # 4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
    print('有车票,可以开始安检...')
# - 如果超过 20 厘米，提示刀的长度，不允许上车
    if knife_length >= 20:
        print('不允许携带 %d 厘米长的刀上车' % knife_length)
# - 如果不超过 20 厘米，安检通过
    else:
        print('安检通过，祝您旅途愉快......')
# 5. 如果没有车票，不允许进门
else:
    print('大哥，您得买票吧')
