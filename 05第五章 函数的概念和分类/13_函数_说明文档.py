"""第十三节，函数的说明文档"""

"""
1. 说明文档（docstring）：写在函数内部第一行的三引号字符串，用于解释函数的用途
2. 格式：def 函数名():  →  第一行写三引号字符串
3. 可以用 help(函数名) 查看函数的说明文档
4. 说明文档通常包含：函数功能、参数说明、返回值说明
5. 好的说明文档让别人（和未来的自己）快速看懂函数的用途
"""


# ── 1. 基本写法 ───────────────────────────────────────────────
def say_hello():
    """打招呼函数，打印 Hello"""
    print('Hello!')

print('---------- 1. 基本写法 ----------')
say_hello()
help(say_hello)   # 查看说明文档


# ── 2. 带参数和返回值的说明文档 ───────────────────────────────
def add(a, b):
    """
    计算两个数的和

    参数：
        a：第一个数
        b：第二个数
    返回值：
        a 和 b 的和
    """
    return a + b

print('---------- 2. 带参数说明 ----------')
help(add)


# ── 3. 有说明文档 vs 没有说明文档 ────────────────────────────
def calc_no_doc(x, y):
    return x ** y   # 不看代码根本不知道这是干什么的

def calc_with_doc(x, y):
    """计算 x 的 y 次方，返回结果"""
    return x ** y

print('---------- 3. 对比 ----------')
help(calc_no_doc)    # 没有文档，只显示函数名
help(calc_with_doc)  # 有文档，一目了然


# ── 练习 ─────────────────────────────────────────────────────
# 1. 给下面的函数补全说明文档：
def greet(name):
    """
    输入名字name，给你打招呼
    """
    return '你好，' + name
#
# 2. 写一个函数 rectangle_area(width, height)，计算矩形面积，
#    并加上完整的说明文档（功能、参数、返回值）
def rectangle_area(width, height):
    """
    输入矩形的宽和高，计算矩形的面积
    :param width: 宽
    :param height: 高
    :return: 面积
    """
    return width * height
#
# 3. 用 help() 查看 Python 内置函数 print 的说明文档，看看官方是怎么写的：
help(print)
# print(*args, sep=' ', end='\n', file=None, flush=False)
    # Prints the values to a stream, or to sys.stdout by default.
    #
    # sep
      # string inserted between values, default a space.
    # end
      # string appended after the last value, default a newline.
    # file
      # a file-like object (stream); defaults to the current sys.stdout.
    # flush
      # whether to forcibly flush the stream.
