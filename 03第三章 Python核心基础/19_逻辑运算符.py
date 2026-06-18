"""第19节，学习逻辑运算符"""

"""
1. 逻辑运算符用于连接多个条件，或对条件结果进行取反
2. and 表示“并且”，只有两边都为 True，结果才为 True
3. or 表示“或者”，只要两边有一个为 True，结果就为 True
4. not 表示“非”，作用是将 True 变为 False，将 False 变为 True
5. 逻辑运算符常和关系运算符一起使用，用于条件判断
"""

# and 与：判断两侧的值是否都为 True
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('分割线1------------------')
print(4==2+2 and 4==2+2)
print(4==2+2 and 3>4)
print(3>4 and 4==2+2)
print(3>4 and 3>4)
print('分割线2------------------')

# or 或：判断两侧的值是否至少有一个为 True
print(True or False)
print(False or True)
print(True or True)
print(False or False)
print('分割线3------------------')

# not 非：用于对一个值取反
print(not 2>3)
print(not True)
print(not False)
