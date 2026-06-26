"""第六节，列表的常用内置函数"""

"""
1. len(列表)           返回列表的元素个数（长度）
2. max(列表)           返回列表中的最大值（元素类型需一致且可比较）
3. min(列表)           返回列表中的最小值
4. sum(列表)           返回列表中所有元素的和（元素必须是数字）
5. sorted(列表)        返回一个新的升序列表，原列表不变
6. sorted(列表, reverse=True)  返回一个新的降序列表，原列表不变
7. list(reversed(列表))        返回一个新的反转列表，原列表不变
8. sorted 与 list.sort() 的区别：sorted 不改变原列表，sort 直接修改原列表
9. reversed 与 list.reverse() 的区别：reversed 不改变原列表，reverse 直接修改原列表
"""


# ── 1. len：获取列表长度 ──────────────────────────────────────
fruits = ['苹果', '香蕉', '橙子', '葡萄', '西瓜']

print('---------- 1. len ----------')
print(len(fruits))   # 5（共 5 个元素）


# ── 2. max：获取最大值 ────────────────────────────────────────
scores = [88, 95, 72, 100, 63]

print('---------- 2. max ----------')
print(max(scores))   # 100


# ── 3. min：获取最小值 ────────────────────────────────────────
print('---------- 3. min ----------')
print(min(scores))   # 63


# ── 4. sum：求和 ──────────────────────────────────────────────
print('---------- 4. sum ----------')
print(sum(scores))   # 418（所有成绩加起来）


# ── 5. sorted：排序（返回新列表，原列表不变）─────────────────
nums = [3, 1, 4, 1, 5, 9, 2, 6]

asc = sorted(nums)               # 升序
desc = sorted(nums, reverse=True)  # 降序

print('---------- 5. sorted ----------')
print('升序：', asc)    # [1, 1, 2, 3, 4, 5, 6, 9]
print('降序：', desc)   # [9, 6, 5, 4, 3, 2, 1, 1]
print('原列表：', nums)  # [3, 1, 4, 1, 5, 9, 2, 6]（不变）


# ── 6. reversed：反转（返回新列表，原列表不变）───────────────
letters = ['a', 'b', 'c', 'd']

new_letters = list(reversed(letters))   # reversed 返回迭代器，用 list() 转成列表

print('---------- 6. reversed ----------')
print('反转后：', new_letters)   # ['d', 'c', 'b', 'a']
print('原列表：', letters)       # ['a', 'b', 'c', 'd']（不变）


# ── 7. sorted vs sort / reversed vs reverse 对比 ─────────────
data = [5, 3, 8, 1]

# sort 直接修改原列表，没有返回值（返回 None）
data.sort()
print('---------- 7. 对比 ----------')
print('sort 后原列表：', data)          # [1, 3, 5, 8]（已被修改）

data2 = [5, 3, 8, 1]
result = sorted(data2)
print('sorted 后原列表：', data2)       # [5, 3, 8, 1]（未被修改）
print('sorted 返回的新列表：', result)  # [1, 3, 5, 8]


# ── 练习 ─────────────────────────────────────────────────────
# 准备列表：grades = [78, 92, 65, 88, 100, 73, 55, 96]
grades = [78, 92, 65, 88, 100, 73, 55, 96]
#
# 1. 用内置函数输出班级人数、最高分、最低分、总分、平均分
print('班级人数：',len(grades))
print('最高分：',max(grades))
print('最低分：',min(grades))
print('总分：',sum(grades))
print('平均分：',sum(grades)/len(grades))
# 2. 用 sorted 获取升序成绩列表，验证原列表 grades 没有被改变
print(sorted(grades))
print(grades)
# 3. 用 sorted(reverse=True) 获取降序成绩列表，打印第一名和最后一名的成绩
list1 = sorted(grades,reverse=True)
print(list1[0],list1[-1])
# 4. 用 list(reversed(...)) 将 grades 反转，验证原列表不变
print(list(reversed(grades)))
print(grades)
