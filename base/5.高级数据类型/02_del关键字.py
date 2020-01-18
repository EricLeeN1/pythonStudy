'''
@Author: your name
@Date: 2020-01-12 11:37:31
@LastEditTime : 2020-01-12 12:26:25
@LastEditors  : Please set LastEditors
# @Description: In User Settings Edit
@FilePath: \pythonStudy\base\高级数据类型\02_del关键字.py
'''
name_list = ['张三', '李四', '王五']

# (知道)使用 del 关键字(delete)删除列表元素
del name_list[1]

# del 关键字本质上是用来将一个变量从内存中删除的
name = '小明'

del name
# 注意：如果使用 del 关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量了
print(name)  # NameError: name 'name' is not defined

print(name_list)  # ['张三', '王五']
