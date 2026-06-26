"""第七节，列表的循环遍历"""

"""
1. for 循环遍历：逐个取出列表中的每个元素，语法简洁
2. while 循环遍历：通过下标访问元素，可在循环中修改下标
3. enumerate(列表)：同时获取下标和元素，返回 (下标, 元素) 的元组
4. for vs while：
   - for 更简洁，适合只需要元素值的场景
   - while 更灵活，适合需要精确控制下标的场景
"""


# ── 1. for 循环遍历 ───────────────────────────────────────────
fruits = ['苹果', '香蕉', '橙子', '葡萄']

print('---------- 1. for 遍历 ----------')
for fruit in fruits:
    print(fruit)


# ── 2. while 循环遍历 ─────────────────────────────────────────
scores = [88, 95, 72, 100, 63]

print('---------- 2. while 遍历 ----------')
i = 0
while i < len(scores):
    print(scores[i])
    i += 1


# ── 3. enumerate：同时获取下标和元素 ──────────────────────────
colors = ['红', '绿', '蓝', '黄']

print('---------- 3. enumerate ----------')
for index, color in enumerate(colors):
    print(f'下标 {index}：{color}')

# enumerate 可以指定起始下标（默认从 0 开始）
print('--- 从 1 开始编号 ---')
for index, color in enumerate(colors, start=1):
    print(f'第 {index} 个：{color}')


# ── 4. for vs while 对比 ─────────────────────────────────────
nums = [10, 20, 30, 40, 50]

print('---------- 4. for vs while ----------')
# for：只需要元素值，写法更简洁
print('for 遍历：')
for n in nums:
    print(n, end=' ')   # 10 20 30 40 50
print()

# while：需要用到下标时更灵活（比如只遍历偶数下标的元素）
print('while 只取偶数下标的元素：')
i = 0
while i < len(nums):
    print(nums[i], end=' ')   # 10 30 50
    i += 2
print()


# ── 练习 ─────────────────────────────────────────────────────
# 准备列表：students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

# 1. 用 for 循环逐行打印每位同学的名字
for name in students:
    print(name)

# 2. 用 while 循环打印每位同学的名字，同时打印对应的下标
i = 0
while i < len(students):
    print(i,students[i])
    i += 1
# 3. 用 enumerate 打印格式为 "第1位同学：Alice" 的编号名单（从 1 开始）
for index,name in enumerate(students):
    print(f'第{index+1}位同学：{name}')
# 4. 用 while 循环只打印下标为奇数的同学（Bob、Diana）
i = 1
while i < len(students):
    print(students[i])
    i += 2