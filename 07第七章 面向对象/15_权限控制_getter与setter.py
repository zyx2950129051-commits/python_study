"""第六节，getter 与 setter"""

"""
本节对应课程大纲里的知识点：getter 与 setter

┌──────────────┬────────────────────────────────────────────────────┐
│ 知识点       │ 说明                                               │
├──────────────┼────────────────────────────────────────────────────┤
│ getter       │ 读取属性时执行的方法                             │
│ setter       │ 修改属性时执行的方法                             │
│ @property    │ 把方法伪装成属性，让读取和赋值更自然               │
└──────────────┴────────────────────────────────────────────────────┘
"""


print('=========================== 教程区 ============================')

print('----------------------- 1. getter 与 setter -----------------------')
# 有些属性不希望外部直接访问或直接修改。
# 但我们又希望外部可以用一种简单的方式读取或设置。
#
# 这时可以使用：
#   @property       定义 getter，控制读取
#   @属性名.setter  定义 setter，控制赋值


class BankAccount:
    def __init__(self, account_holder, balance, password):
        self.account_holder = account_holder
        self._balance = balance
        self.__password = password

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print('余额不能为负数，已自动设置为 0')
            self._balance = 0

    @property
    def password(self):
        return '******'

    @password.setter
    def password(self, value):
        print('密码不允许通过普通赋值方式修改，请走安全验证流程')

    def check_password(self, password):
        return password == self.__password


account = BankAccount('王五', 1000, '123456')

print(account.account_holder)
# 输出：王五

print(account.balance)
# 输出：1000

account.balance = 800
print(account.balance)
# 输出：800

account.balance = -50
# 输出：余额不能为负数，已自动设置为 0

print(account.balance)
# 输出：0

print(account.password)
# 输出：******

account.password = '000000'
# 输出：密码不允许通过普通赋值方式修改，请走安全验证流程

print(account.check_password('123456'))
# 输出：True

print()


print('----------------------- 2. property 的好处 -----------------------')
# property 的好处：
#   1. 外部使用时像访问普通属性一样简单
#   2. 类内部可以控制读取时返回什么
#   3. 类内部可以控制赋值是否合法
#   4. 可以保护敏感数据，避免外部乱改


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        # 注意：这里的 self.celsius = celsius 并不是直接创建普通属性，
        # 而是触发了下面 @celsius.setter 中的逻辑，
        # 最终数据保存在 self._celsius 中。

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print('摄氏温度不能低于绝对零度，已设置为 -273.15')
            self._celsius = -273.15
        else:
            self._celsius = value


    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9


temp = Temperature(25)

print(temp.celsius)
# 输出：25

print(temp.fahrenheit)
# 输出：77.0

temp.fahrenheit = 212
print(temp.celsius)
# 输出：100.0

temp.celsius = -300
# 输出：摄氏温度不能低于绝对零度，已设置为 -273.15

print(temp.celsius)
# 输出：-273.15

print()


print('============================ 小结 ============================')
# 1. @property 可以把方法当属性使用，常用于控制读取和赋值。


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义 Product 类：
#   - name 公有属性
#   - _price 受保护属性
# 使用 @property 定义 price：
#   - getter 返回 _price
#   - setter 要求 price 不能小于 0，否则提示并设置为 0
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            print('您的价格不能小于0')
            self._price = 0
        else:
            self._price = value

print('--------------------------- 练习 2 ---------------------------')
# 定义 MyTemperature 类，内部用 _celsius 保存摄氏温度。
# 使用 @property 提供：
#   - celsius 属性，可读可写
#   - fahrenheit 属性，可读可写
# 要求：
#   读取 fahrenheit 时返回 摄氏 * 9 / 5 + 32
#   设置 fahrenheit 时，自动转换成摄氏温度保存

class MyTemperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print('您的温度低于绝对零度，请重新设置')
            self._celsius = -273.15
        else:
            self._celsius = value
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9
