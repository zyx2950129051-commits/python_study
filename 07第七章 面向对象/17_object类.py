"""第八节，object 类"""

"""
本节对应课程大纲里的知识点：object 顶层父类

┌──────────────┬──────────────────────────────────────────────┐
│ 知识点       │ 说明                                         │
├──────────────┼──────────────────────────────────────────────┤
│ object       │ Python 中所有类的最终父类                    │
│ 默认继承      │ class Person 等价于 class Person(object)      │
│ issubclass   │ 判断一个类是否是另一个类的子类               │
│ isinstance   │ 判断一个对象是否是某个类或其子类的实例       │
│ __class__    │ 查看对象由哪个类创建                         │
│ dir()        │ 查看对象能访问到的属性和方法                 │
└──────────────┴──────────────────────────────────────────────┘

先记一句最重要的话：
- Python 中所有类最终都继承自 object，所以所有对象都有一套最基础的能力。
"""


print('=========================== 教程区 ============================')

print('--------------------------- 1. object 是顶层父类 ---------------------------')
# 本节会用到 isinstance 和 issubclass，它们在第 12 节已经学过。
# 这里用它们来验证一个重要结论：所有类最终都继承自 object。
#
# 在 Python 3 中，下面两种写法含义基本一样：
#
#   class Person:
#       pass
#
#   class Person(object):
#       pass
#
# 即使我们不写 object，Python 也会让这个类默认继承 object。


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(object):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


print(issubclass(Person, object))
# 输出：True

print(issubclass(Student, object))
# 输出：True

print()


print('--------------------------- 2. 内置类型也继承 object ---------------------------')
# Python 的内置类型，例如 int、str、list、dict，也都是类。
# 它们最终也继承自 object。

print(issubclass(int, object))
# 输出：True

print(issubclass(str, object))
# 输出：True

print(issubclass(list, object))
# 输出：True

print(issubclass(dict, object))
# 输出：True

print()


print('--------------------------- 3. 所有对象都是 object 的实例 ---------------------------')
# 因为所有类最终都继承 object，
# 所以所有对象都可以看成 object 的实例。

p1 = Person('张三', 18)

print(isinstance(p1, object))
# 输出：True

print(isinstance(100, object))
# 输出：True

print(isinstance('hello', object))
# 输出：True

print(isinstance([10, 20, 30], object))
# 输出：True

print(isinstance(None, object))
# 输出：True

print()


print('--------------------------- 4. object 提供基础能力 ---------------------------')
# object 提供了很多基础属性和方法。
# 如果我们不重写这些方法，就使用 object 提供的默认版本。

print('__str__' in object.__dict__)
# 输出：True

print('__init__' in object.__dict__)
# 输出：True

print('__eq__' in object.__dict__)
# 输出：True

print()


print('--------------------------- 5. __dict__、dir、__class__ ---------------------------')
# __dict__：
#   查看对象自己身上保存的属性。
#
# dir(对象)：
#   查看对象能访问到的属性和方法，包括自己、类、父类中提供的内容。
#
# 对象.__class__：
#   查看对象由哪个类创建。

print(p1.__dict__)
# 输出：{'name': '张三', 'age': 18}

print(p1.__class__)
# 输出：<class '__main__.Person'>

names = dir(p1)
print('name' in names)
# 输出：True

print('__str__' in names)
# 输出：True

print()


print('--------------------------- 6. 默认 __str__ 与重写 __str__ ---------------------------')


class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'《{self.name}》售价 {self.price} 元'


phone = Phone('华为', 5999)
book = Book('Python入门', 59)

print(phone)
# 输出：<__main__.Phone object at 0x...>
# Phone 没有重写 __str__，所以使用 object 的默认显示方式。

print(book)
# 输出：《Python入门》售价 59 元
# Book 重写了 __str__，所以 print(book) 时显示更友好。

print()


print('============================ 小结 ============================')
# 1. object 是 Python 中所有类的最终父类。
# 2. class Person 默认继承 object。
# 3. 内置类型 int、str、list、dict 等也继承 object。
# 4. 所有对象都可以看成 object 的实例。
# 5. object 提供了 __init__、__str__、__eq__ 等基础能力。
# 6. 子类可以重写 object 提供的方法，让对象表现得更符合业务需求。


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义一个 Cat 类，不显式继承 object。
# 用 issubclass(Cat, object) 验证它是否继承 object。
class Cat:
    pass
print(issubclass(Cat, object))

print('--------------------------- 练习 2 ---------------------------')
# 创建 Cat 实例。
# 用 isinstance(cat, object) 验证它是否是 object 的实例。
cat = Cat()
print(isinstance(cat, object))

print('--------------------------- 练习 3 ---------------------------')
# 打印 cat.__dict__、cat.__class__、dir(cat)。
# 观察三者分别能看到什么信息。
print(cat.__dict__, cat.__class__, dir(cat))

print('--------------------------- 练习 4 ---------------------------')
# 定义一个 Movie 类，先不写 __str__，打印实例观察输出。
# 再重写 __str__，让 print(movie) 输出电影名称和评分。
class Movie:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f'《{self.name}》，评分：{self.score}'

