"""第14节，学习数据类型转换"""

"""
1. 数据类型转换就是把一种类型的数据转成另一种类型的数据
2. 用户输入的内容通常都是字符串，若要进行数学运算，往往需要先转换类型
3. 在输出、写入文件或拼接字符串时，常常需要把其他类型转换成字符串
4. 使用 str() 可以把其他类型的数据转换成字符串类型
5. 使用 int() 可以把整数形式的数据转换成整型
6. 浮点数使用 int() 转换时，会直接去掉小数部分，不会四舍五入
7. 使用 float() 可以把整数或数字字符串转换成浮点型
8. 只要字符串内容符合数字格式，int() 和 float() 一般都可以完成转换
9. 字符串两边有空格时，int() 和 float() 通常也可以自动忽略空格
"""


# 使用 str(xxxx) 将xxxx转换成字符串   任何类型都可以转成字符串类型
result_1 = str(18)
result_2 = str(34.56)
print('result_1所指代的数据', result_1, '的数据类型是', type(result_1))
print('result_2所指代的数据', result_2, '的数据类型是', type(result_2))


# 使用 int(xxxx) 将xxxx转换成整型，浮点型数据会直接丢掉小数部分
result_3 = int(45)
result_4 = int(15.6)
result_5 = int('19')
result_6 = int('   70   ')
print('result_3所指代的数据', result_3, '的数据类型是', type(result_3))
print('result_4所指代的数据', result_4, '的数据类型是', type(result_4))
print('result_5所指代的数据', result_5, '的数据类型是', type(result_5))
print('result_6所指代的数据', result_6, '的数据类型是', type(result_6))


# 使用 float(xxxx) 将xxxx转换成浮点型
result_7 = float(45)
result_8 = float(15.6)
result_9 = float('19')
result_10 = float('   70.4   ')
print('result_7所指代的数据', result_7, '的数据类型是', type(result_7))
print('result_8所指代的数据', result_8, '的数据类型是', type(result_8))
print('result_9所指代的数据', result_9, '的数据类型是', type(result_9))
print('result_10所指代的数据', result_10, '的数据类型是', type(result_10))
