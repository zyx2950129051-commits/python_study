"""第十节，抽象类"""
from turtle import width

"""
本节对应课程大纲里的知识点：抽象类与抽象方法

┌────────────────┬────────────────────────────────────────────────┐
│ 知识点         │ 说明                                           │
├────────────────┼────────────────────────────────────────────────┤
│ ABC            │ 抽象类基类，来自 abc 模块                      │
│ abstractmethod │ 把方法标记为抽象方法                           │
│ 抽象类          │ 不能直接实例化，通常用来制定规范               │
│ 抽象方法       │ 子类必须实现的方法                             │
│ 作用           │ 约束子类，让一组子类拥有统一的方法名称         │
└────────────────┴────────────────────────────────────────────────┘

先记一句最重要的话：
- 抽象类不是拿来直接创建对象的，而是拿来给子类定规矩的。
"""


from abc import ABC, abstractmethod


print('=========================== 教程区 ============================')

print('--------------------------- 1. 什么是抽象类 ---------------------------')
# 抽象类：不能直接实例化的类。
#
# 它通常只负责定义规范：
#   子类必须具备哪些方法。
#
# 在 Python 中，需要使用 abc 模块：
#   ABC：让一个类变成抽象类的基础父类
#   @abstractmethod：把方法标记为抽象方法


class MustRun(ABC):
    @abstractmethod
    def run(self):
        pass


# 取消下面代码注释会报错：
# obj = MustRun()
# TypeError: Can't instantiate abstract class MustRun with abstract method run

print('MustRun 是抽象类，不能直接创建实例')
print()


print('--------------------------- 2. 子类必须实现抽象方法 ---------------------------')
# 子类继承抽象类后，必须实现所有抽象方法。
# 如果没有实现，子类仍然是抽象类，依然不能创建实例。


class Person(MustRun):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f'{self.name} 正在跑步')


p1 = Person('张三')
p1.run()
# 输出：张三 正在跑步

print()


print('--------------------------- 3. 多个抽象方法 ---------------------------')


class Payment(ABC):
    @abstractmethod
    def pay(self, money):
        pass

    @abstractmethod
    def refund(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print(f'支付宝支付 {money} 元')

    def refund(self, money):
        print(f'支付宝退款 {money} 元')


class WechatPay(Payment):
    def pay(self, money):
        print(f'微信支付 {money} 元')

    def refund(self, money):
        print(f'微信退款 {money} 元')


def checkout(payment, money):
    payment.pay(money)


def return_goods(payment, money):
    payment.refund(money)


ali = Alipay()
wechat = WechatPay()

checkout(ali, 100)
# 输出：支付宝支付 100 元

checkout(wechat, 80)
# 输出：微信支付 80 元

return_goods(ali, 30)
# 输出：支付宝退款 30 元

print()


print('--------------------------- 4. 抽象类和多态的关系 ---------------------------')
# 抽象类经常和多态配合使用：
#   1. 抽象类负责定规范
#   2. 子类负责实现具体行为
#   3. 调用者按统一方法名调用
#
# 这样可以避免不同子类方法名混乱。

payments = [Alipay(), WechatPay()]

for item in payments:
    item.pay(50)

print()


print('============================ 小结 ============================')
# 1. 抽象类需要继承 ABC。
# 2. 抽象方法需要使用 @abstractmethod 装饰。
# 3. 抽象类不能直接实例化。
# 4. 子类必须实现抽象类中的所有抽象方法，否则也不能实例化。
# 5. 抽象类常用于制定规范，配合多态使用效果更好。


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义抽象类 Animal，包含抽象方法 speak。
# 定义 Dog、Cat 继承 Animal，并实现 speak。
# 创建实例并调用 speak。
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return '汪汪汪'
class Cat(Animal):
    def speak(self):
        return '喵喵喵'
def make_sound(sound):
    return sound.speak()
d1 = Dog()
c1 = Cat()
print(make_sound(d1),make_sound(c1))

print('--------------------------- 练习 2 ---------------------------')
# 定义抽象类 Shape，包含抽象方法 area。
# 定义 Rectangle、Circle 继承 Shape，并实现 area。
# 写函数 print_area(shape)，打印 shape.area()。
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius *3.14

def area_shape(shape):
    return shape.area()

r1 = Rectangle(30, 45)
c1 = Circle(25)
print(area_shape(r1),area_shape(c1))

print('--------------------------- 练习 3 ---------------------------')
# 定义抽象类 FileReader，包含抽象方法 read。
# 定义 TxtReader、CsvReader 继承 FileReader，并实现 read。
# 思考：抽象类在这里起到了什么作用？
class FileReader(ABC):
    @abstractmethod
    def read(self):
        pass
class TextReader(FileReader):
    def read(self):
        return '您正在使用文本阅读'
class CsvReader(FileReader):
    def read(self):
        return '您正在使用表格阅读'

def read_file(file):
    return file.read()

t1 = TextReader()
c1 = CsvReader()
print(read_file(t1),read_file(c1))

'''抽象类可以规范子类必须有什么方法'''

print('--------------------------- 练习 4 ---------------------------')
# 故意定义一个子类继承抽象类，但不实现抽象方法。
# 尝试创建实例，观察报错信息。

class Test(ABC):
    @abstractmethod
    def test(self):
        pass
class Test1(Test):
    pass
'''
t1 = Test1()

TypeError: Can't instantiate abstract class Test1 without an implementation for abstract method 'test'
'''