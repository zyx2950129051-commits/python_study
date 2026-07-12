"""第八章第 4 小节：高阶函数。

知识点：参数是函数或返回值是函数的函数，称为高阶函数。
"""


print('=========================== 教程区 ============================')
print('本节主题：使用函数组织和组合行为')


print('--------------------------- 1. 参数是函数 ---------------------------')


def welcome():
    print('你好啊！')


def caller(function):
    print('caller 开始调用')
    function()
    print('caller 调用结束')


caller(welcome)


print('--------------------------- 2. 返回值是函数 ---------------------------')


def outer():
    print('outer 已执行')

    def inner():
        print('inner 已执行')

    return inner


returned_function = outer()
returned_function()


print('--------------------------- 3. 高阶函数的实际意义 ---------------------------')
# 高阶函数可以把固定流程与变化的行为分开。
# log 负责统一输出流程，info、warn、error 负责不同的文本加工方式。


def info(message):
    return '[提示]' + message


def warn(message):
    return '[警告]' + message


def error(message):
    return '[错误]' + message


def log(formatter, text):
    print(formatter(text))


log(info, '文件保存成功！')
log(warn, '磁盘空间不足！')
log(error, '该用户不存在！')


print('=========================== 知识点整理 ============================')
print('1. 接收函数对象作为参数的函数是高阶函数。')
print('2. 返回函数对象的函数也是高阶函数。')
print('3. 传递函数对象时只写函数名，不加调用小括号。')
print('4. 高阶函数能把通用流程和具体行为分离，提高复用性。')
print('5. 高阶函数是闭包和装饰器的重要基础。')


print('============================ 小结区 ============================')
print('判断高阶函数时，只需看它是否接收函数或返回函数。')
print('高阶函数的价值不是写法更复杂，而是让行为能够被替换和组合。')


print('============================ 练习区 ============================')
print('--------------------------- 练习 1 ---------------------------')
# 定义 upper_text 和 lower_text，再定义 process(function, text)。
# 让 process 使用传入的函数处理文本并返回结果。
def upper_text(text):
    return text.upper()
def lower_text(text):
    return text.lower()
def process (function, text):
    return (function(text))
print(process(upper_text,'nihao'))
print(process(lower_text,'HELLO'))

print('--------------------------- 练习 2 ---------------------------')
# 定义 choose_operation(name)，根据 name 返回加法函数或减法函数。
# 获取返回的函数后再进行计算。
def choose_operation(name):
    def plus(a, b):
        return a + b
    def minus(a, b):
        return a - b
    if name == 'plus':
        return plus
    elif name == 'minus':
        return minus
    else:
        return '只能是plus或者minus'

operation = choose_operation('plus')
print(operation(10, 3))

operation = choose_operation('minus')
print(operation(10, 3))



