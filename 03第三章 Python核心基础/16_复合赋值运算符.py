"""第16节，学习复合赋值运算符"""

"""
1. 复合赋值运算符就是把算术运算和赋值运算合并在一起写
2. 使用复合赋值运算符可以让代码写起来更简洁
3. += 表示先做加法运算，再把结果赋值给原变量
4. -= 表示先做减法运算，再把结果赋值给原变量
5. *= 表示先做乘法运算，再把结果赋值给原变量
6. /= 表示先做除法运算，再把结果赋值给原变量
7. //= 表示先做整除运算，再把结果赋值给原变量
8. %= 表示先做取余运算，再把结果赋值给原变量
9. **= 表示先做幂运算，再把结果赋值给原变量
"""

# = 赋值运算符
age = 18

# += 加法赋值运算符
age1 = 18
age1 += 1  #等价于age1 = age1 + 1
print(age1)

# -=减法赋值运算符
age2 = 18
age2 -= 1  #等价于age2 = age2 - 1
print(age2)

# *= 乘法赋值运算符
price = 25
amount = 5
price *= amount  #等价于price = price * amount
print(price)

# /= 除法赋值运算符
price = 100
people_num1 = 4
price /= people_num1  #等价于price = price / people_num1
print(price)

# //= 取整赋值运算符
apple_amount = 46
people_num2 = 10
apple_amount //= people_num2  #等价于apple_amount = apple_amount // people_num2
print(apple_amount)

# %= 取余赋值运算符
banana_amount = 56
people_num3 = 18
banana_amount %= people_num3  #等价于banana_amount = banana_amount % people num3
print(banana_amount)

# **= 指数赋值运算符
a = 2
b = 3
a **= b  #等价于a = a ** b
print(a)
