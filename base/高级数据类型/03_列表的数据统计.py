'''
@Author: your name
@Date: 2020-01-12 12:26:46
@LastEditTime : 2020-01-12 20:08:22
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\高级数据类型\03_列表的数据统计.py
'''
name_list = ['张三', '李四', '王五', '王小二', '张三']

#  len(length 长度) 函数可以统计列表中元素的总数
list_len = len(name_list)
print('%s 中包含 %d 个元素' % (name_list, list_len))

# count 方法可以统计列表中某一个数据出现的次数
count = name_list.count('张三')
print('张三这个变量出现了 %d 次' % count)

# 从列表中删除数据第一次出现的数据，如果数据不存在，程序会报错
name_list.remove('张三')

print(name_list)
