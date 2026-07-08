"""第七节，魔法方法"""

"""
本节对应课程大纲里的知识点：常用魔法方法

┌──────────────┬──────────────────────────────────────────────┐
│ 魔法方法     │ 自动调用时机                                 │
├──────────────┼──────────────────────────────────────────────┤
│ __str__      │ print(对象) 或 str(对象) 时                   │
│ __len__      │ len(对象) 时                                  │
│ __lt__       │ 对象1 < 对象2 时                              │
│ __gt__       │ 对象1 > 对象2 时                              │
│ __eq__       │ 对象1 == 对象2 时                             │
│ __getattr__  │ 访问对象不存在的属性时                       │
└──────────────┴──────────────────────────────────────────────┘

先记一句最重要的话：
- 魔法方法不用我们手动调用，Python 会在对应语法出现时自动调用。
"""


print('=========================== 教程区 ============================')

print('--------------------------- 1. 什么是魔法方法 ---------------------------')
# 魔法方法：以双下划线开头、双下划线结尾的方法。
#
# 例如：
#   __init__
#   __str__
#   __len__
#   __eq__
#
# 它们看起来像普通方法，但调用时机比较特殊：
#   不是我们直接写 对象.__str__()
#   而是 Python 在 print(对象)、len(对象)、对象比较等场景中自动调用。


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'姓名：{self.name}，年龄：{self.age}，性别：{self.gender}'

    def __len__(self):
        return len(self.__dict__)

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __getattr__(self, item):
        return f'您访问的 {item} 属性不存在'


p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')
p3 = Person('张三', 18, '男')

print()


print('--------------------------- 2. __str__ 方法 ---------------------------')
# __str__ 的调用时机：
#   print(对象)
#   str(对象)
#
# 如果不写 __str__，打印对象时通常只能看到内存地址样式的内容。
# 写了 __str__ 后，可以决定对象被打印时显示什么。
#
# 补充：还有一个类似的方法叫 __repr__，调用时机是：
#   在交互式终端直接输入对象名回车时
#   repr(对象)
#   如果没有定义 __str__，Python 也会退而求其次使用 __repr__。
# 一般来说：__str__ 面向用户，__repr__ 面向开发者。

print(p1)
# 输出：姓名：张三，年龄：18，性别：男

print(str(p2))
# 输出：姓名：李四，年龄：22，性别：女

print()


print('--------------------------- 3. __len__ 方法 ---------------------------')
# __len__ 的调用时机：
#   len(对象)
#
# 注意：
#   __len__ 必须返回整数。

print(len(p1))
# 输出：3
# 因为 p1.__dict__ 中有 name、age、gender 三个属性。

print()


print('--------------------------- 4. 比较相关魔法方法 ---------------------------')
# __lt__：less than，小于
# __gt__：greater than，大于
# __eq__：equal，等于
#
# 这些方法让自定义对象也能使用 <、>、== 进行比较。

print(p1 < p2)
# 输出：True    本例按年龄比较，18 < 22

print(p1 > p2)
# 输出：False

print(p1 == p3)
# 输出：True    本例按 __dict__ 比较，属性和值都相同

print(p1 == p2)
# 输出：False

print()


print('--------------------------- 5. __getattr__ 方法 ---------------------------')
# __getattr__ 的调用时机：
#   访问对象不存在的属性时自动执行。
#
# 注意：
#   如果属性本来存在，就不会执行 __getattr__。

print(p1.name)
# 输出：张三

print(p1.address)
# 输出：您访问的 address 属性不存在

print()


print('============================ 小结 ============================')
# 1. 魔法方法是 __xxx__ 形式的特殊方法。
# 2. 魔法方法不需要手动调用，Python 会在特定语法场景下自动调用。
# 3. __str__ 决定对象被 print 或 str 时的显示内容。
# 4. __len__ 决定 len(对象) 的结果，必须返回整数。
# 5. __lt__、__gt__、__eq__ 可以让自定义对象支持比较。
# 6. __getattr__ 会在访问不存在的属性时触发。


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义 Book 类，包含 name、price。
# 重写 __str__，让 print(book) 输出："《书名》售价 xx 元"。

print('--------------------------- 练习 2 ---------------------------')
# 给 Book 类重写 __lt__ 和 __gt__。
# 让两个 Book 对象可以按 price 比较大小。

print('--------------------------- 练习 3 ---------------------------')
# 给 Book 类重写 __eq__。
# 要求：书名和价格都相同，才认为两本书相等。

class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f'“《{self.name}》售价{self.price}元。”'

    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

print('--------------------------- 练习 4 ---------------------------')
# 定义 Student 类，包含 name 和 scores 字典。
# 重写 __len__，让 len(student) 返回这个学生已经录入了几门成绩。

print('--------------------------- 练习 5 ---------------------------')
# 给 Student 类重写 __getattr__。
# 当访问不存在的属性时，返回"该属性不存在，请检查属性名"。
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def __len__(self):
        return len(self.scores)
    def __getattr__(self, item):
        return f'{item}不存在，请检查属性名'
