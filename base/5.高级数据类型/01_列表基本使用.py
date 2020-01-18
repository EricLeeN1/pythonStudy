'''
@Author: your name
@Date: 2020-01-12 09:10:49
@LastEditTime : 2020-01-12 11:36:02
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\高级数据类型\01_列表基本使用.py
'''
name_list = ['张三', '李四', '王五']

# 1、取值与索引
# list index out of range 列表索引超出范围
print(name_list[2])  # 王五

# 知道数据的内容，想确定数据在列表中的位置
print(name_list.index('张三'))  # 0

# 2、修改
name_list[1] = 'lisi'
# list assignment index out of range
# 列表指定的索引超出范围，程序会报错
# name_list[3] = '王小二'
print(name_list)  # ['张三', 'lisi', '王五']

# 3、增加
# append方法可以向列表的末尾追加数据
name_list.append('王小二')
# insert方法可以在列表的指定索引位置插入数据
name_list.insert(1, '李二蛋')
# extend 追加到列表末尾
temp_list = ["孙悟空", "猪八戒", "沙师弟"]
name_list.extend(temp_list)

# 4、删除
# remove 方法可以从列表中指定删除的数据 
name_list.remove('王小二')
# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
# pop 方法可以指定要删除元素的索引
name_list.pop(3)
# clear 方法可以清空列表
name_list.clear()

print(name_list)
