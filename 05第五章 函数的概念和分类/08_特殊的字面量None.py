"""第八节，特殊的字面量 None"""

"""
1. None 是一个特殊的字面量，表示空值、无值、无意义
2. None 的类型是 NoneType
3. None 转为布尔值是 False，可以用 if not 来判断
4. None 不能参与数学运算，也不能与字符串拼接
5. 函数没有 return 语句时，默认返回 None
"""


# None 是一个特殊的字面量，表示空值、无值、无意义。
msg = None
print(msg)

# None 的类型是 NoneType。
print(type(msg))

# None 转为布尔值是 False。
print(bool(msg))
if not msg:
    print('hello world')

# None 不能参与数学运算，也不能与字符串拼接。
'''
print(msg + 1)。              错误
print(msg + 'hello world')    错误
'''

# 函数如果没有设置返回值，会默认返回 None。
