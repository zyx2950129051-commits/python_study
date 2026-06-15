#coding=utf-8
"""第七节写数据类型"""

"""
数据类型说明表
-----------------------------------------------
类型名      说明                  例子
-----------------------------------------------
str        字符串类型             '张三'、'hello'
int        整数类型               18、100、-5
float      浮点数类型             65.4、3.14
bool       布尔类型               True、False
-----------------------------------------------
1. 数据类型就是数据的种类
2. 不同的数据，类型可能不一样
3. 可以使用type()函数查看数据的类型
4. 查看类型时，既可以先用变量接收结果，再打印；也可以直接在print()中调用type()
"""

name = '张三'
age = 18
weight = 65.4
is_student = True

print(name)
print(age)
print(weight)
print(is_student)

result = type(name)
print('name的数据类型是：', result)
result = type(age)
print('age的数据类型是：', result)

print('weight的数据类型是：', type(weight))
print('is_student的数据类型是：', type(is_student))
