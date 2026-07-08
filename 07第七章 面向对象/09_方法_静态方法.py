"""第四节，静态方法"""

"""
本节对应课程大纲里的知识点：静态方法

┌────────────┬────────────────────────────────────────────────────┐
│ 方法类型   │ 说明                                               │
├────────────┼────────────────────────────────────────────────────┤
│ 静态方法   │ 用 @staticmethod 装饰，不需要 self / cls             │
│ 调用建议   │ 静态方法推荐用类名调用                               │
│ 常见场景   │ 工具函数                                           │
└────────────┴────────────────────────────────────────────────────┘

先记一句最重要的话：
- 都不需要对象自己的数据和类本身的数据，就写静态方法。
"""

from datetime import datetime


print('=========================== 教程区 ============================')

print('--------------------------- 1. 静态方法 ---------------------------')
# 静态方法：用 @staticmethod 装饰的方法。
#
# 特点：
#   1. 没有 self
#   2. 没有 cls
#   3. 只是放在类里的普通工具函数
#   4. 推荐通过类名调用
#
# 什么时候用？
#   这个函数和类的主题有关，但不需要访问实例属性，也不需要访问类属性。


class Tool:
    @staticmethod
    def is_adult(birth_year):
        age = datetime.now().year - birth_year
        return age >= 18

    @staticmethod
    def mask_phone(phone):
        return phone[:3] + '****' + phone[-4:]


print(Tool.is_adult(2010))
# 输出：False   （按 2026 年计算，2010 年出生是 16 岁）

print(Tool.mask_phone('13812345678'))
# 输出：138****5678

tool = Tool()
print(tool.mask_phone('15987654321'))
# 输出：159****4321
# 这种写法可以运行，但不推荐。静态方法用类名调用语义更清楚。

print()


print('--------------------------- 2. 对比总结 ---------------------------')


class Example:
    school = '尚硅谷'

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print(f'实例方法拿到 self：{self.name}')

    @classmethod
    def class_method(cls):
        print(f'类方法拿到 cls：{cls.school}')

    @staticmethod
    def static_method():
        print('静态方法没有 self，也没有 cls')


e = Example('小明')
e.instance_method()
# 输出：实例方法拿到 self：小明

Example.class_method()
# 输出：类方法拿到 cls：尚硅谷

Example.static_method()
# 输出：静态方法没有 self，也没有 cls

print()


print('============================ 小结 ============================')
# 1. 静态方法用 @staticmethod，没有 self / cls，适合写和类相关的工具函数。
# 2. 调用建议：类名.方法()


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义 Book 类。
# 给 Book 类增加静态方法 discount_price(price, rate)。
# rate 表示折扣，例如 0.8 表示八折。
# 调用 Book.discount_price(100, 0.7)，打印结果。
class Book:
    @staticmethod
    def discount_price(price, rate):
        return price * rate

result1 = Book.discount_price(100,0.7)
print(result1)

print('--------------------------- 练习 2 ---------------------------')
# 用自己的话回答：
#   静态方法为什么不需要 self 和 cls？
'''因为静态方法只是当做类的辅助工具，本身不需要用类或者实例的参数的时候才会用，所以不需要'''
