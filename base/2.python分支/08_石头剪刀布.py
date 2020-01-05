# 导入随机工具包
import random

# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input('请输入您要出的拳： 石头（1）/ 剪刀（2）/ 布（3）'))

# 电脑 随机 出拳 - 假定电脑永远出石头
computer = random.randint(1, 3)

print('玩家选择的拳头 %d - 电脑出的拳是 %d' % (player, computer))

# 比较胜负
# 如果条件判断的内容太长，可以在最外侧的条件增加一对大括号
# 再在每一个条件之间，使用回车，PyCharm 可以自动增加 8 个空格

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print('选手赢了')
elif player == computer:
    print('平手')
else:
    print('电脑赢了')
