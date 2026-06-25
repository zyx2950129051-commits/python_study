"""第十二节，函数的递归调用"""

"""
1. 递归调用：函数在内部调用自己
2. 递归必须有终止条件（base case），否则会无限循环导致报错
3. 每次递归调用都要让问题规模变小，逐步靠近终止条件
4. 执行顺序：一层层往下调用，到终止条件后再一层层返回
------------------------------------------------
递归示意（以 3 的阶乘为例）：
  factorial(3)
    → factorial(2)
        → factorial(1)
        ← 返回 1
    ← 返回 2 * 1 = 2
  ← 返回 3 * 2 = 6
------------------------------------------------
"""


# ── 1. 最简单的递归：倒数打印 ─────────────────────────────────
# 终止条件：n == 0 时停止
def countdown(n):
    if n == 0:
        print('发射！')
        return        # 终止条件，不再继续递归
    print(n)
    countdown(n - 1)  # 每次 n 减 1，逐步靠近 0

print('---------- 1. 倒数打印 ----------')
countdown(3)


# ── 2. 经典案例：阶乘 n! ──────────────────────────────────────
# 数学定义：n! = n * (n-1) * (n-2) * ... * 1，且 1! = 1
def factorial(n):
    if n == 1:          # 终止条件
        return 1
    return n * factorial(n - 1)   # 每次规模减小 1

print('---------- 2. 阶乘 ----------')
print('3! =', factorial(3))   # 6
print('5! =', factorial(5))   # 120


# ── 3. 没有终止条件会怎样 ─────────────────────────────────────
# ⚠️ 下面代码会报错：RecursionError: maximum recursion depth exceeded
# def infinite(n):
#     return infinite(n - 1)   # 没有终止条件，永远不会停
# infinite(1)


# ── 4. 累加：1 + 2 + 3 + ... + n ─────────────────────────────
def sum_to(n):
    if n == 1:          # 终止条件
        return 1
    return n + sum_to(n - 1)

print('---------- 4. 累加 ----------')
print('1到5的和 =', sum_to(5))   # 15


# ── 练习 ─────────────────────────────────────────────────────
# 1. 预测 countdown(3) 的完整输出顺序，再运行验证
#
# 回答：程序先看到调用countdown函数，并且n等于3
# 此时将3代入n，到函数定义层级，由于此时n是3不等于0，所以执行打印3，并执行countdown(3-1)
# 此时将2代入n，并读取countdown的定义，依旧不是0，继续打印2并且执行countdown(2-1)
# 1代入n，程序读取countdown定义，不是0，继续打印1，执行countdown=(1-1)
# 0代入n，程序读取函数定义，终于是0了，打印文字发射，返回
#

# 2. 用递归写一个函数 power(base, exp)，计算 base 的 exp 次方
#    例如：power(2, 3) = 8（即 2*2*2）
#    提示：2^3 = 2 * 2^2，终止条件是 exp == 0 时返回 1
#
# 回答：
def power(m,n):
    if n == 1:
        return m
    return m*power(m,n-1)
print('3的4次方是',power(3,4))

# 3. 下面的递归哪里有问题？怎么修？
#    def count_up(n, max):
#        print(n)
#        count_up(n + 1, max)
# 问题在于没有设置终止条件
def count_up(n, max):
    if n > max:
        return
    print(n)
    count_up(n + 1, max)
count_up(1,10)
