"""第18节，学习布尔类型"""

"""
1. 布尔类型只有两个值，分别是 True 和 False
2. 布尔类型通常用来表示条件是否成立
3. 布尔值可以直接定义，也可以通过比较运算得到
4. 比较表达式成立时结果为 True，不成立时结果为 False
5. 在 Python 中，布尔类型本质上是整数类型的子类型
6. True 在底层通常可以看作 1，False 在底层通常可以看作 0
7. 因此布尔值可以参与算术运算
8. 使用 bool() 可以把其他类型的数据转换成布尔类型
9. 一般情况下，数字 0 和空字符串转换为 False，其他大多数值转换为 True
"""

# 自己定义的布尔值
a = True
b = False

# 程序执行得到的布尔值
c = 5 > 3
d = 6 < 2

print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)

# 布尔类型是int的子类型，底层本质是用1表示Ture，用0表示False
print(int(True))
print(int(False))

print(9 + True)
print(5 ** False)

# 使用 bool(x) 将x转换为布尔类型
print(bool(1))
print(bool(0))

# Python中除0外的任何数，转换为布尔类型都为Ture
print(bool(-74.2983))

# Python中除了空字符外的任何字符，转换为布尔类型都为Ture
print(bool('wow'))
print(bool(''))

