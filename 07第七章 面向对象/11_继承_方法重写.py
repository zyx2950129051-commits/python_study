"""第五节，方法重写"""

"""
本节对应课程大纲里的知识点：方法重写

┌──────────────┬──────────────────────────────────────────────────────────────┐
│ 知识点       │ 说明                                                         │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ 方法重写     │ 子类定义与父类同名的方法，会优先执行子类自己的方法           │
└──────────────┴──────────────────────────────────────────────────────────────┘
"""


print('=========================== 教程区 ============================')

class Person:
    """父类：人类"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}，今年{self.age}岁，性别{self.gender}，我想说：{msg}')

class Student(Person):
    """子类：学生类"""
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

print('--------------------------- 1. 方法重写 ---------------------------')


class PrimaryStudent(Student):
    """小学生类：继承 Student，并重写 speak 方法"""

    def speak(self, msg):
        print(f'我是小学生 {self.name}，我想说：{msg}')


class CollegeStudent(Student):
    """大学生类：继承 Student，并在父类 speak 的基础上扩展"""

    def __init__(self, name, age, gender, stu_id, grade, major):
        super().__init__(name, age, gender, stu_id, grade)
        self.major = major

    def speak(self, msg):
        # 先执行父类 Person 中的 speak 逻辑
        super().speak(msg)
        # 再扩展大学生自己的介绍
        print(f'我的学号是 {self.stu_id}，专业是 {self.major}')


ps = PrimaryStudent('小明', 10, '男', 'P2026001', '五')
ps.speak('我喜欢编程')
# 输出：我是小学生 小明，我想说：我喜欢编程

cs = CollegeStudent('赵敏', 20, '女', 'C2026001', '大二', '计算机科学')
cs.speak('我正在学习继承')
# 输出：我叫赵敏，今年20岁，性别女，我想说：我正在学习继承
# 输出：我的学号是 C2026001，专业是 计算机科学

print()


print('============================ 小结 ============================')
# 1. 方法重写：
#    子类和父类有同名方法时，优先执行子类的方法。
#    如果既想保留父类逻辑，又想增加新逻辑，就在子类方法里调用 super().同名方法(...)。


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 先准备好上一节的 Animal 和 Dog（如果已经写过，可以直接复制过来）：
#
#   class Animal:
#       def __init__(self, name):
#           self.name = name
#       def eat(self):
#           print(f'{self.name} 正在吃东西')
#
#   class Dog(Animal):
#       def bark(self):
#           print(f'{self.name} 汪汪叫')
#
# 给 Dog 新增 color 属性。
# 重写 eat 方法：
#   - 先调用 super().eat()
#   - 再打印"xx 边吃边摇尾巴"
# 创建实例并调用 eat，观察输出顺序。
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f'{self.name} 正在吃东西')

class Dog(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def eat(self):
        super().eat()
        print(f'{self.name} 边吃边摇尾巴')

    def bark(self):
        print(f'{self.name} 正在汪汪叫')


dog1 = Dog('小白', '白色')
dog1.eat()
