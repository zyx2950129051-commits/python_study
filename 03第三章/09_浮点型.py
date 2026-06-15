#coding=utf-8
"""第九节写浮点型"""

"""
1. 浮点型就是带有小数部分的数字类型
2. 在Python中，浮点型使用float表示
3. 浮点数可以表示正数、负数和0.0
4. 可以使用type()函数查看浮点型的数据类型
5. 常见的浮点数有3.14、65.4、-2.5、0.0
6. 浮点数还可以使用科学计数法表示，比如3.14e2
7. 3.14e2表示3.14乘以10的2次方
8. 浮点数在计算机中有时候不能做到绝对精确
"""

height = 175.5
weight = 65.4
temperature = -2.5
price = 0.0

print(height)
print(weight)
print(temperature)
print(price)

result = type(height)
print('height的数据类型是：', result)

print('weight的数据类型是：', type(weight))
print('temperature的数据类型是：', type(temperature))
print('price的数据类型是：', type(price))

num = 3.14e2
print(num)
