"""第五节，基本语法"""

"""
本节对应课程大纲里的知识点：基本语法

┌──────────────┬──────────────────────────────────────────────────────────────┐
│ 知识点       │ 说明                                                         │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ 继承的概念   │ 子类继承父类后，可以直接使用父类已有的属性和方法             │
│ 基本语法     │ class 子类名(父类名):                                        │
│ super()      │ 在子类中调用父类方法，常用于调用父类的 __init__              │
└──────────────┴──────────────────────────────────────────────────────────────┘

先记一句最重要的话：
- 继承不是"复制代码"，而是让子类站在父类已有能力的基础上继续扩展。
"""


print('=========================== 教程区 ============================')

print('----------------------- 1. 继承的基本语法 -----------------------')


class Person:
    """父类：人类，保存学生和老师共有的属性与行为"""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}，今年{self.age}岁，性别{self.gender}，我想说：{msg}')


class Student(Person):
    """子类：学生类，继承 Person，并增加学生独有内容"""

    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

    def study(self, subject):
        print(f'{self.name} 正在学习 {subject}，目标是成为 {self.grade} 年级优秀学生')


s1 = Student('李华', 16, '男', 'S2026001', '初二')

print(s1.__dict__)
# 输出：{'name': '李华', 'age': 16, 'gender': '男', 'stu_id': 'S2026001', 'grade': '初二'}

# speak 方法定义在父类 Person 中，但 Student 继承了 Person，所以学生实例可以直接调用。
s1.speak('你好，欢迎学习 Python 面向对象')
# 输出：我叫李华，今年16岁，性别男，我想说：你好，欢迎学习 Python 面向对象

# study 方法定义在子类 Student 中，是学生独有的行为。
s1.study('数学')
# 输出：李华 正在学习 数学，目标是成为 初二 年级优秀学生

print()


print('----------------------- 2. 子类扩展父类功能 -----------------------')


class Teacher(Person):
    """子类：老师类，继承 Person，并增加老师独有内容"""

    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def teach(self):
        print(f'{self.name} 老师正在讲授 {self.subject}')


t1 = Teacher('王老师', 35, '女', 'Python')

print(t1.__dict__)
# 输出：{'name': '王老师', 'age': 35, 'gender': '女', 'subject': 'Python'}

t1.speak('同学们好')
# 输出：我叫王老师，今年35岁，性别女，我想说：同学们好

t1.teach()
# 输出：王老师 老师正在讲授 Python

print()


print('============================ 小结 ============================')
# 1. 继承解决的是"代码复用和能力扩展"问题。
#    公共属性和公共方法放在父类，子类只补充自己独有的属性和方法。
#
# 2. 子类定义语法：
#       class 子类名(父类名):
#           pass
#
# 3. 子类初始化时，推荐使用：
#       super().__init__(父类需要的参数)


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义父类 Animal：
#   - 属性：name
#   - 方法：eat，打印"xx 正在吃东西"
# 定义子类 Dog 继承 Animal：
#   - 新增方法 bark，打印"xx 汪汪叫"
# 创建 Dog 实例，分别调用 eat 和 bark
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f'{self.name} 正在吃东西')

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def bark(self):
        print(f'{self.name} 正在汪汪叫')
dog1 = Dog('小白')
dog1.eat()
dog1.bark()