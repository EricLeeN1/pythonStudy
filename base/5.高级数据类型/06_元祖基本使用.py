'''
@Author: your name
@Date: 2020-01-14 14:27:16
@LastEditTime : 2020-01-14 14:31:31
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\5.高级数据类型\06_元祖基本使用.py
'''
info_tuple = ['张三', 18, 1, 75]


# 1、取值和取索引。
print(info_tuple[0])
# 张三
print(info_tuple.index('张三'))
# 0

# 2、统计计数
print(info_tuple.count(18))
# 1
