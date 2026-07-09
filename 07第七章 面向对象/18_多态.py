"""第九节，多态"""

"""
本节对应课程大纲里的知识点：标准多态与鸭子多态

┌────────────┬────────────────────────────────────────────────────┐
│ 知识点     │ 说明                                               │
├────────────┼────────────────────────────────────────────────────┤
│ 多态       │ 同一个方法名，在不同对象上表现出不同的行为         │
│ 标准多态   │ 基于继承实现，子类重写父类方法                     │
│ 鸭子多态   │ 不关心继承关系，只关心对象有没有需要的方法         │
│ 方法重写   │ 子类定义与父类同名的方法                           │
│ 统一调用   │ 同一个函数接收不同对象，调用同一个方法名           │
└────────────┴────────────────────────────────────────────────────┘

先记一句最重要的话：
- 多态让我们用同一套调用方式，处理不同类型对象的不同行为。
"""


print('=========================== 教程区 ============================')

print('--------------------------- 1. 什么是多态 ---------------------------')
# 多态：多种形态。
#
# 在代码中，多态通常表现为：
#   不同对象都有同名方法；
#   调用同一个方法名时，执行结果各不相同。
#
# 例如：
#   狗 speak：汪汪汪
#   猫 speak：喵喵喵
#   鸭子 speak：嘎嘎嘎


class Animal:
    def speak(self):
        print('动物正在发出声音')


class Dog(Animal):
    def speak(self):
        print('汪汪汪')


class Cat(Animal):
    def speak(self):
        print('喵喵喵')


def make_sound(animal: Animal):
    animal.speak()


make_sound(Animal())
# 输出：动物正在发出声音

make_sound(Dog())
# 输出：汪汪汪

make_sound(Cat())
# 输出：喵喵喵

print()


print('--------------------------- 2. 标准多态 ---------------------------')
# 标准多态：
#   1. 有一个父类
#   2. 多个子类继承父类
#   3. 子类重写父类的同名方法
#   4. 使用父类类型的思路统一调用
#
# Python 不会强制检查类型，但我们仍然可以按标准多态的方式设计代码。


class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


def print_area(shape):
    print(f'面积：{shape.area()}')


rect = Rectangle(10, 5)
circle = Circle(3)

print_area(rect)
# 输出：面积：50

print_area(circle)
# 输出：面积：28.26

print(isinstance(rect, Shape))
# 输出：True

print(isinstance(circle, Shape))
# 输出：True

print()


print('--------------------------- 3. 鸭子多态 ---------------------------')
# 鸭子多态，也叫鸭子类型。
#
# 核心思想：
#   如果一个对象看起来像鸭子，叫起来也像鸭子，那它就可以当鸭子使用。
#
# 换成代码就是：
#   不关心对象是不是某个类的子类；
#   只关心它有没有我们要调用的方法。


class Pig:
    def speak(self):
        print('哼哼哼')


class Robot:
    def speak(self):
        print('机器人正在播放语音')


# Pig 和 Robot 没有继承 Animal，
# 但它们都有 speak 方法，所以 make_sound 仍然可以调用。
make_sound(Pig())
# 输出：哼哼哼

make_sound(Robot())
# 输出：机器人正在播放语音

print()


print('--------------------------- 4. 多态的价值 ---------------------------')
# 多态的好处：
#   调用者不需要关心对象内部怎么实现，
#   只要对象能提供约定好的方法，就可以统一处理。
#
# 反例：如果不用多态，代码可能写成这样：
#
#   def make_sound_ugly(obj):
#       if isinstance(obj, Dog):
#           print('汪汪汪')
#       elif isinstance(obj, Cat):
#           print('喵喵喵')
#       elif isinstance(obj, Pig):
#           print('哼哼哼')
#       ...
#
# 每新增一种动物，就要多写一个 elif，既麻烦又容易遗漏。
# 而多态让我们只需要 animal.speak()，一行搞定。

animals = [Dog(), Cat(), Pig(), Robot()]

for item in animals:
    make_sound(item)

print()


print('============================ 小结 ============================')
# 1. 多态指同一个方法名，在不同对象上表现出不同的行为。
# 2. 标准多态通常基于继承和方法重写。
# 3. 鸭子多态不要求继承，只要求对象有对应方法。
# 4. Python 更常用鸭子类型的思路：先调用，关注对象能不能完成任务。
# 5. 多态能让代码更灵活，减少大量 if 类型判断。


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义父类 Payment，包含 pay 方法。
# 定义子类 Alipay、WechatPay、BankCardPay，分别重写 pay 方法。
# 写函数 checkout(payment)，内部调用 payment.pay()。
class Payment:
    def pay(self):
        return

class Alipay(Payment):
    def pay(self):
        return '您正在使用支付宝支付'

class WechatPay(Payment):
    def pay(self):
        return '您正在使用微信支付'

class BankCardPay(Payment):
    def pay(self):
        return '您正在使用银行卡支付'

def checkout(payment):
    print(payment.pay())

checkout(Alipay())
checkout(WechatPay())
checkout(BankCardPay())


print('--------------------------- 练习 2 ---------------------------')
# 定义父类 Vehicle，包含 move 方法。
# 定义 Car、Bike、Train 三个子类，分别重写 move 方法。
# 把它们放进列表中，循环调用 move。
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return '汽车在行驶'
class Bike(Vehicle):
    def move(self):
        return '自行车在骑行'
class Train(Vehicle):
    def move(self):
        return '火车在开'

vehicle = [Car(), Bike(), Train()]

for item in vehicle:
    print(item.move())

print('--------------------------- 练习 3 ---------------------------')
# 不使用继承，定义 Bird、Plane、Kite 三个类。
# 它们都提供 fly 方法。
# 写函数 let_it_fly(obj)，内部调用 obj.fly()。
# 观察这是否属于鸭子多态。
class Bird:
    def fly(self):
        return '鸟在飞'
class Plane:
    def fly(self):
        return '飞机在飞'
class Kite:
    def fly(self):
        return '风筝在飞'

def let_it_fly(obj):
    return obj.fly()

print(let_it_fly(Bird()), let_it_fly(Plane()), let_it_fly(Kite()))

print('--------------------------- 练习 4 ---------------------------')
# 思考题：
# 标准多态和鸭子多态有什么区别？
'''答：标准多态涉及到父类子类之间相同方法的调用，需要方法重写。
鸭子多态不需要，不用涉及父类子类，只要对象有对应方法即可'''
# Python 中为什么经常使用鸭子多态？
'''因为更灵活，不用写一堆判断条件，只要类有方法，就能用'''
