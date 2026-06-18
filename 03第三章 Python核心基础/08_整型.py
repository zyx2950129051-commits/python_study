#coding=utf-8
"""第八节写整型"""

"""
1. 整型就是整数类型，没有小数部分
2. 整型可以表示正整数、负整数和0
3. 在Python中，整型使用int表示
4. 可以使用type()函数查看整型的数据类型
5. Python中整数可以写成十进制、二进制、八进制、十六进制
6. 十进制直接写数字，比如18
7. 二进制以0b开头，八进制以0o开头，十六进制以0x开头
8. 为了让大数字更容易阅读，可以在数字中间使用下划线分隔
"""

age = 18
count = 0
money = -100

print(age)
print(count)
print(money)

result = type(age)
print('age的数据类型是：', result)

print('count的数据类型是：', type(count))
print('money的数据类型是：', type(money))

num1 = 0b1010
num2 = 0o12
num3 = 0xA
num4 = 1_000_000

print(num1)
print(num2)
print(num3)
print(num4)
