"""第五节，isinstance 和 issubclass"""

"""
本节对应课程大纲里的知识点：isinstance() 和 issubclass()

┌──────────────┬──────────────────────────────────────────────────────────────┐
│ 知识点       │ 说明                                                         │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ 类型判断     │ isinstance() 判断对象类型；issubclass() 判断类之间的继承关系 │
└──────────────┴──────────────────────────────────────────────────────────────┘
"""


print('=========================== 教程区 ============================')

class Person:
    pass

class Student(Person):
    pass

class CollegeStudent(Student):
    pass


print('------------------- 1. isinstance 与 issubclass --------------------')

p1 = Person()
s2 = Student()

print(isinstance(p1, Person))
# 输出：True    p1 是 Person 创建出来的实例

print(isinstance(s2, Student))
# 输出：True    s2 是 Student 创建出来的实例

print(isinstance(s2, Person))
# 输出：True    Student 继承 Person，所以学生也是人

print(isinstance(p1, Student))
# 输出：False   Person 没有继承 Student，所以普通人不一定是学生

print(issubclass(Student, Person))
# 输出：True    Student 是 Person 的子类

print(issubclass(Person, Student))
# 输出：False   Person 不是 Student 的子类

print(issubclass(CollegeStudent, Person))
# 输出：True    CollegeStudent -> Student -> Person，间接继承也算

print()


print('============================ 小结 ============================')
# 1. isinstance(对象, 类)：判断对象是不是这个类或其子类的实例。
# 2. issubclass(子类, 父类)：判断一个类是否继承自另一个类。


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 创建 Animal 实例和 Dog 实例，分别判断：
#   - Dog 实例是否是 Dog 的实例
#   - Dog 实例是否是 Animal 的实例
#   - Animal 实例是否是 Dog 的实例
#   - Dog 是否是 Animal 的子类
# 先预测 True / False，再用 isinstance 和 issubclass 验证。

class Animal:
    pass
class Dog(Animal):
    pass

a1 = Animal()
d1 = Dog()
'''
Dog 实例是否是 Dog 的实例?
答案：是的
Dog 实例是否是 Animal 的实例？
答案：是的
Animal 实例是否是 Dog 的实例
答案：不是
Dog 是否是 Animal 的子类
答案：是的
'''
print(isinstance(d1, Dog))
print(isinstance(d1, Animal))
print(isinstance(a1, Dog))
print(issubclass(Dog, Animal))