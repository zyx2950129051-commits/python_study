"""第四节，类方法"""

"""
本节对应课程大纲里的知识点：类方法

┌────────────┬────────────────────────────────────────────────────┐
│ 方法类型   │ 说明                                               │
├────────────┼────────────────────────────────────────────────────┤
│ 类方法     │ 用 @classmethod 装饰，第一个参数是 cls，操作类相关内容│
│ 调用建议   │ 类方法推荐用类名调用                               │
│ 常见场景   │ 修改类属性、工厂方法                               │
└────────────┴────────────────────────────────────────────────────┘

先记一句最重要的话：
- 需要用类本身，就写类方法。
"""

from datetime import datetime


print('=========================== 教程区 ============================')

print('----------------------------- 1. 类方法 -----------------------------')
# 类方法：用 @classmethod 装饰的方法。
#
# 特点：
#   1. 第一个参数是类本身，习惯命名为 cls
#   2. 可以访问和修改类属性
#   3. 可以通过类名或实例调用，推荐通过类名调用
#   4. 常用于修改类级别数据，或写工厂方法


class Worker:
    company = '默认公司'
    max_age = 65

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @classmethod
    def create_by_info(cls, info):
        # 工厂方法：根据字符串创建对象。
        # info 格式："姓名-出生年份"
        name, birth_year = info.split('-')
        return cls(name, int(birth_year))

    def show_info(self):
        age = datetime.now().year - self.birth_year
        print(f'{self.name}，{age} 岁，所在公司：{self.company}')


print(Worker.company)
# 输出：默认公司

Worker.change_company('阳光科技')

print(Worker.company)
# 输出：阳光科技

w1 = Worker.create_by_info('王五-2000')
print(w1.__dict__)
# 输出：{'name': '王五', 'birth_year': 2000}

w1.show_info()
# 输出：王五，26 岁，所在公司：阳光科技   （按 2026 年计算）

print()


print('============================ 小结 ============================')
# 1. 类方法用 @classmethod，第一个参数是 cls，适合处理类属性或工厂方法。
# 2. 调用建议：类名.方法()


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义 Book 类，包含实例属性 name、price。
# 给 Book 类增加类属性 press = '默认出版社'。
# 增加类方法 change_press，用来修改出版社名称。
# 调用 Book.change_press('人民出版社') 后，打印 Book.press。
print('--------------------------- 练习 2 ---------------------------')
# 给 Book 类增加类方法 create_by_text。
# 传入字符串格式："Python入门-59"。
# 方法内部切分字符串，并返回 Book 实例。
# 调用后打印实例的 __dict__。
class Book:
    press = '默认出版社'
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @classmethod
    def change_press(cls, new_press):
        cls.press = new_press


    @classmethod
    def create_by_text(cls, info):
        name, number = info.split('-')
        return cls(name, int(number))

Book.change_press('人民出版社')
print(Book.press)

b1 = Book.create_by_text('Python入门-59')
print(b1.__dict__)






print('--------------------------- 练习 3 ---------------------------')
# 用自己的话回答：
#   cls 表示什么？
'''
谁调用这个方法，cls就是谁
'''
