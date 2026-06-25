"""第五节，列表的常用方法"""

"""
list.sort()               升序排列（直接修改原列表）
list.sort(reverse=True)   降序排列
list.reverse()            反转列表（直接修改原列表）
list.count(元素)           统计某元素出现的次数
list.copy()               复制列表，返回一个新列表
list.clear()              清空列表
list.extend(其他列表)      将其他列表的元素追加到末尾
"""


# ── 1. sort：排序 ─────────────────────────────────────────────
nums = [3, 1, 4, 1, 5, 9, 2, 6]

nums.sort()                  # 升序
print('---------- 1. sort 升序 ----------')
print(nums)   # [1, 1, 2, 3, 4, 5, 6, 9]

nums.sort(reverse=True)      # 降序
print('---------- 1. sort 降序 ----------')
print(nums)   # [9, 6, 5, 4, 3, 2, 1, 1]


# ── 2. reverse：反转 ──────────────────────────────────────────
letters = ['a', 'b', 'c', 'd']
letters.reverse()

print('---------- 2. reverse ----------')
print(letters)   # ['d', 'c', 'b', 'a']


# ── 3. count：统计出现次数 ────────────────────────────────────
scores = [90, 85, 90, 70, 90, 85]

print('---------- 3. count ----------')
print(scores.count(90))   # 3（90 出现了 3 次）
print(scores.count(85))   # 2
print(scores.count(100))  # 0（不存在返回 0，不报错）


# ── 4. copy：复制列表 ─────────────────────────────────────────
original = [1, 2, 3]
copied = original.copy()

copied.append(4)   # 修改复制的列表，不影响原列表

print('---------- 4. copy ----------')
print('原列表：', original)   # [1, 2, 3]
print('复制列表：', copied)   # [1, 2, 3, 4]


# ── 5. clear：清空列表 ────────────────────────────────────────
trash = ['垃圾1', '垃圾2', '垃圾3']
trash.clear()

print('---------- 5. clear ----------')
print(trash)   # []


# ── 6. extend：追加另一个列表的所有元素 ──────────────────────
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)

print('---------- 6. extend ----------')
print(a)   # [1, 2, 3, 4, 5, 6]
print(b)   # [4, 5, 6]（b 不变）


# ── 练习 ─────────────────────────────────────────────────────
# 准备列表：data = [5, 3, 8, 1, 3, 7, 3, 2]
date = [5,3,8,1,3,7,3,2]
#
# 1. 将 data 升序排列，再反转，查看结果
date.sort()
date.reverse()
print('date经过升序后反转得到的是',date)
#
# 2. 统计 3 在 data 中出现了几次
print(date.count(3))
#
# 3. 复制 data 为 data2，在 data2 末尾追加 [9, 10]（用 extend），
date2 = date.copy()
date2.extend([9,10])
#    验证 data 没有被影响
print('date为',date)
print('date2为',date2)
#
# 4. 清空 data2，打印确认是否为空列表
date2.clear()
print(date2)