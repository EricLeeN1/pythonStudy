'''
@Author: your name
@Date: 2020-01-14 15:06:13
@LastEditTime : 2020-01-14 15:13:49
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit

@FilePath: \pythonStudy\base\5.高级数据类型\08_格式化字符串.py
'''
# 格式化字符串后面的()本质上就是元祖
info_tuple = ('小明', 18, 1.75)
print('%s 年龄是 %d 身高是 %2.f' % info_tuple)

info_str = '%s 年龄是 %d 身高是 %2.f' % info_tuple
print(info_str)