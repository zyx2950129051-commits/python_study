"""第八节，列表小练习"""

"""
综合运用列表的所有知识点：
- 定义列表、下标访问
- 增删改查（append / insert / remove / pop / del）
- 常用方法（sort / reverse / count / copy / clear / extend）
- 常用内置函数（len / max / min / sum / sorted / reversed）
- 循环遍历（for / while / enumerate）
"""


# ── 综合练习 ──────────────────────────────────────────────────
# 场景：管理一个班级的成绩单

# 初始成绩列表
grades = [85, 92, 78, 90, 65, 88, 73, 95, 60, 82]

# 1. 打印班级总人数、最高分、最低分、总分、平均分
print(len(grades))
print(max(grades))
print(min(grades))
print(sum(grades))
print(sum(grades)/len(grades))
# 2. 有一位同学补考成绩为 70，追加到列表末尾
grades.append(70)
# 3. 发现第 3 个成绩（78）录入有误，改为 80
grades[2] = 80
# 4. 用 for + enumerate 打印所有同学的编号和成绩，格式：「第1位同学：85分」
for index,grade in enumerate(grades):
    print(f'第{index+1}位同学：{grade}分')
# 5. 用 sorted 获取升序成绩列表，打印排名最后一名（最低分）的成绩，验证原列表不变
sorted_grades = sorted(grades,reverse=True)
print(sorted_grades[-1])
print(grades)
# 6. 统计成绩中 90 出现了几次
print(grades.count(90))
# 7. 用 while 循环只打印下标为偶数的成绩
i = 0
while i < len(grades):
    print(grades[i])
    i += 2
# 8. 60 分的同学未通过，将其从列表中删除
for grade in grades:
    if grade == 60:
        grades.remove(grade)
print(grades)