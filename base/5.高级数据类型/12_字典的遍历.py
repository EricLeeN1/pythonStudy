'''
@Author: your name
@Date: 2020-01-14 15:59:09
@LastEditTime : 2020-01-14 16:01:25
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \pythonStudy\base\5.高级数据类型\12_字典的遍历.py
'''
xiaoming_dict = {
    "name": "小明",
    "height": 180,
    "age": 18
}

for k in xiaoming_dict:
    print('%s的值是%s' % (k, xiaoming_dict[k]))
