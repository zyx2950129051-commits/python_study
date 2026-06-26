"""第十一节，函数_解包列表或元组传参"""

"""
1. 解包（unpacking）：用 * 将列表或元组拆散，逐个传给函数的位置参数
2. 语法：函数名(*列表) 或 函数名(*元组)
3. 解包传参要求：列表/元组的元素个数必须与函数参数个数一致
4. 普通传参 vs 解包传参：
   普通传参 → 把整个列表作为一个参数传入
   解包传参 → 把列表的每个元素分别传给对应参数
"""


# ── 1. 普通传参 vs 解包传参 ───────────────────────────────────
def add(a, b, c):
    print(a + b + c)

nums = [10, 20, 30]

print('---------- 1. 普通传参 vs 解包传参 ----------')
# add(nums)           # ❌ 报错：传入的是整个列表，不是三个参数
add(*nums)            # ✓ 解包：相当于 add(10, 20, 30)  → 60


# ── 2. 解包元组 ───────────────────────────────────────────────
def greet(name, age, city):
    print(f'{name}，{age}岁，来自{city}')

info = ('张三', 18, '北京')

print('---------- 2. 解包元组 ----------')
greet(*info)          # 相当于 greet('张三', 18, '北京')


# ── 3. 解包传参与普通传参混用 ─────────────────────────────────
def introduce(greeting, name, age):
    print(f'{greeting}，我是{name}，今年{age}岁')

person = ('李四', 20)

print('---------- 3. 混用 ----------')
introduce('你好', *person)    # 普通参数 + 解包，相当于 introduce('你好', '李四', 20)


# ── 练习 ─────────────────────────────────────────────────────
# 1. 定义函数 rectangle(width, height)，打印长方形的面积
#    准备列表 size = [5, 8]，用解包方式调用函数
def rectangle(width, height):
    """
    计算长方形面积
    :param wideth:宽
    :param height: 高
    :return: 面积
    """
    print(width*height)
    return width*height

size = [5,8]
rectangle(*size)

# 2. 定义函数 info(name, score, grade)，打印学生信息
#    准备元组 student = ('王五', 95, 'A')，用解包方式调用函数
def info(name, score, grade):
    print(f'我的名字是{name}，分数是{score}分，等级是{grade}。')
student = ('王五',95,'A')
info(*student)

# 3. 准备列表 nums = [3, 7, 1, 9, 4]
#    用解包方式传给 max() 和 min()，打印最大值和最小值
#    提示：max(*nums) 和 max(nums) 效果相同，理解为什么

nums = [3,7,1,9,4]
print(max(nums))    # → 9
print(min(nums))    # → 1
print(max(*nums))   # → 9，相当于 max(3, 7, 1, 9, 4)
print(min(*nums))   # → 1

# 为什么效果相同？
# max(nums)  → 传入列表，max 把它当可迭代对象，内部自己遍历找最大值
# max(*nums) → 解包成多个位置参数 max(3, 7, 1, 9, 4)，逐个比较
# max/min 是内置函数，两种方式都支持，所以结果一样
# 普通函数不行：add(nums) ≠ add(*nums)，普通函数不会自动遍历列表