"""第十一节，函数的嵌套调用"""

"""
1. 嵌套调用：在一个函数内部调用另一个函数
2. 执行顺序：遇到函数调用时，先跳进被调用的函数执行完，再回来继续
3. 嵌套调用可以将复杂逻辑拆分成多个小函数，让代码更清晰
4. 函数可以多层嵌套，但层数太多会降低可读性
------------------------------------------------
调用顺序示意：
  main() 开始
    → 调用 a()
        → 调用 b()
        ← b() 结束
    ← a() 结束
  main() 结束
------------------------------------------------
"""


# ── 1. 基础嵌套：函数 A 调用函数 B ───────────────────────────
def say_hello():
    print('Hello!')

def say_hello_twice():
    say_hello()   # 调用另一个函数
    say_hello()

print('---------- 1. 基础嵌套 ----------')
say_hello_twice()


# ── 2. 执行顺序：先进去执行完，再回来 ────────────────────────
def inner():
    print('inner 开始')
    print('inner 结束')

def outer():
    print('outer 开始')
    inner()            # 跳进 inner，执行完再回来
    print('outer 结束')

print('---------- 2. 执行顺序 ----------')
outer()


# ── 3. 实际应用：用小函数组合成大功能 ────────────────────────
def print_line():
    print('-' * 20)

def print_title(title):
    print_line()
    print(title)
    print_line()

print('---------- 3. 组合小函数 ----------')
print_title('学生信息')
print_title('课程列表')


# ── 4. 多层嵌套 ───────────────────────────────────────────────
def add(a, b):
    return a + b

def double_add(a, b):
    result = add(a, b)   # 先加
    return result * 2    # 再翻倍

def show_result(a, b):
    print(f'{a} 和 {b} 相加再翻倍 =', double_add(a, b))

print('---------- 4. 多层嵌套 ----------')
show_result(3, 4)   # (3+4)*2 = 14


# ── 练习 ─────────────────────────────────────────────────────
# 1. 预测下面代码的输出顺序，再运行验证：
#      def b():
#          print('B')
#      def a():
#          print('A1')
#          b()
#          print('A2')
#      a()
# 答案：先输出A1,再输出B,最后输出A2
#
# 2. 写两个函数：
#      greet(name)   → 打印 "你好，xxx"
#      farewell(name) → 打印 "再见，xxx"
#    再写一个函数 meet(name)，依次调用上面两个函数
def greet(name):
    print('你好', name)
def farewell(name):
    print('再见', name)
def meet(name):
    greet(name)
    farewell(name)

meet('小周')

#
# 3. 写一个函数 calculate(a, b)：
#    内部调用 add(a, b) 和 multiply(a, b) 两个函数，
#    分别打印它们的结果
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def calculate(a,b):
    result_add = add(a,b)
    result_multiply = multiply(a,b)
    print(f'a+b的值是{result_add}，a*b的值是{result_multiply}')
calculate(3,4)
