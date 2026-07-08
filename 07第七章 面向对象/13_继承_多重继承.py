"""第五节，多重继承"""

"""
本节对应课程大纲里的知识点：多重继承

┌──────────────┬──────────────────────────────────────────────────────────────┐
│ 知识点       │ 说明                                                         │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ 多重继承     │ 一个子类可以同时继承多个父类，查找顺序由 __mro__ 决定        │
└──────────────┴──────────────────────────────────────────────────────────────┘
"""


print('=========================== 教程区 ============================')

print('--------------------------- 1. 多重继承 ---------------------------')
# 什么是 MRO？
# MRO 全称 Method Resolution Order，翻译过来就是"方法查找顺序"。
# 当你调用一个方法时，Python 会按 MRO 的顺序依次往上找：
#   自己 → 第一个父类 → 第二个父类 → ... → object
# 谁先找到就用谁的。
#
# 你可以通过 类名.__mro__ 或 类名.mro() 来查看这个顺序。


class Flyer:
    def fly(self):
        print('我可以在天空中飞')

    def move(self):
        print('飞行移动')


class Swimmer:
    def swim(self):
        print('我可以在水里游')

    def move(self):
        print('游泳移动')


class Duck(Flyer, Swimmer):
    pass


duck = Duck()
duck.fly()
# 输出：我可以在天空中飞

duck.swim()
# 输出：我可以在水里游

# Flyer 和 Swimmer 中都有 move 方法。
# Duck(Flyer, Swimmer) 表示先找 Flyer，再找 Swimmer。
duck.move()
# 输出：飞行移动

print(Duck.__mro__)
# 输出：(<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>)

print()


print('----------------------- 2. 多重继承中的初始化 -----------------------')


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}，今年{self.age}岁，性别{self.gender}，我想说：{msg}')


class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

    def study(self, subject):
        print(f'{self.name} 正在学习 {subject}，目标是成为 {self.grade} 年级优秀学生')


class Worker:
    def __init__(self, company):
        self.company = company

    def work(self):
        print(f'我在 {self.company} 工作')


class PartTimeStudent(Student, Worker):
    def __init__(self, name, age, gender, stu_id, grade, company):
        # 为什么这里不用 super().__init__？
        # 因为 Student 和 Worker 的 __init__ 参数完全不同，
        # super() 只会按 MRO 调用下一个类的 __init__，
        # 无法同时传递不同参数给两个不同的父类。
        # 所以这里选择直接用"类名.__init__(self, ...)"的方式分别调用。
        Student.__init__(self, name, age, gender, stu_id, grade)
        Worker.__init__(self, company)


pts = PartTimeStudent('陈晨', 19, '男', 'S2026003', '高三', '阳光书店')

print(pts.__dict__)
# 输出：{'name': '陈晨', 'age': 19, 'gender': '男', 'stu_id': 'S2026003', 'grade': '高三', 'company': '阳光书店'}

pts.speak('我一边学习，一边兼职')
# 输出：我叫陈晨，今年19岁，性别男，我想说：我一边学习，一边兼职

pts.study('英语')
# 输出：陈晨 正在学习 英语，目标是成为 高三 年级优秀学生

pts.work()
# 输出：我在 阳光书店 工作

print(PartTimeStudent.__mro__)
# 输出：(<class '__main__.PartTimeStudent'>, <class '__main__.Student'>, <class '__main__.Person'>, <class '__main__.Worker'>, <class 'object'>)

print()


print('============================ 小结 ============================')
# 1. 多重继承：
#    class Duck(Flyer, Swimmer) 表示 Duck 同时继承 Flyer 和 Swimmer。
#    如果多个父类有同名方法，Python 会按照 类.__mro__ 中的顺序查找。


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义两个父类：
#   - Flyer：有 fly 方法，打印"在飞"
#   - Swimmer：有 swim 方法，打印"在游"
# 定义子类 Duck 同时继承 Flyer 和 Swimmer。
# 创建 Duck 实例，分别调用 fly 和 swim。
# 最后打印 Duck.__mro__，观察查找顺序。
class Flyer:
    def fly(self):
        print('在飞')
    def move(self):
        print('飞行移动')
class Swimmer:
    def swim(self):
        print('在游')
    def move(self):
        print('游泳移动')
class Duck(Flyer, Swimmer):
    pass

print(Duck.__mro__)
d1 = Duck()
Duck.move(d1)

print('--------------------------- 练习 2 ---------------------------')
# 思考题：
# 如果 Flyer 和 Swimmer 中都定义了同名方法 move，
# Duck(Flyer, Swimmer) 调用 move 时，会执行哪一个？
'''回答：先执行Flyer，再执行Swimmer'''
# Duck(Swimmer, Flyer) 调用 move 时，结果会不会变化？
'''回答：会'''
# 请写代码验证，并用 __mro__ 解释原因。
'''因为Duck(Swimmer，Flyer)中Swimmer在前
多重继承的顺序是严格按照括号里“从左到右”的顺序来查找的
___mro___查找的顺序中Swimmer在Flyer前面，所以先找到Swimmer就用Swimmer中的move'''
