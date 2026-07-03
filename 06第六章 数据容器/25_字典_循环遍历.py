"""第二十五节，字典_循环遍历"""

"""
这一节代码整体在讲：字典的 for 循环遍历。

本节对应课程大纲里的知识点：
1. 直接遍历字典（默认遍历 key）
2. 遍历 keys()
3. 遍历 items()，同时获取 key 和 value

先记一句最重要的话：
- 字典只能用 for 遍历，不能用 while
"""

print('========================== 教程区 ==========================')

# 共用定义
scores = {'张三': 72, '李四': 60, '王五': 85}

print('--------------------- 1. 直接遍历字典 ----------------------')
# 直接 for 遍历字典，默认取出的是 key，再通过 key 取 value

for key in scores:
    print(f'{key} 的成绩是 {scores[key]}')

print('---------------------- 2. 遍历 keys() ----------------------')
# 遍历 keys()，和直接遍历效果一样，但语义更明确

for key in scores.keys():
    print(f'{key} 的成绩是 {scores[key]}')

print('--------------------- 3. 遍历 items() ----------------------')
# 遍历 items()，同时获取 key 和 value，最推荐的方式

for key, value in scores.items():
    print(f'{key} 的成绩是 {value}')

print('=========================== 小结 ===========================')
# 1. 字典只能用 for 遍历，不能用 while
# 2. 三种方式：直接遍历 / keys() / items()
# 3. 最推荐 items()，同时拿到 key 和 value，不需要再取一次

print('========================== 习题区 ==========================')


print('-------------------------- 练习 1 --------------------------')
# 练习 1：
# 有一个字典：
# scores = {'张三': 72, '李四': 60, '王五': 85}
# 请用三种方式分别遍历打印，格式：张三 的成绩是 72
scores = {'张三': 72, '李四': 60, '王五': 85}
for key in scores:
    print(f'{key} 的成绩是 {scores[key]}')
for key in scores.keys():
    print(f'{key} 的成绩是 {scores[key]}')
for key, value in scores.items():
    print(f'{key} 的成绩是 {value}')

print('-------------------------- 练习 2 --------------------------')
# 练习 2：
# 有一个嵌套字典：
# class_scores = {
#     '小明': {'语文': 90, '数学': 95, '英语': 88},
#     '小红': {'语文': 92, '数学': 87, '英语': 94}
# }
# 请用嵌套 for 循环，逐个打印每个学生的每科成绩
# 格式：小明 的 语文 成绩是 90
class_scores = {
    '小明': {'语文': 90, '数学': 95, '英语': 88},
    '小红': {'语文': 92, '数学': 87, '英语': 94}
}
for name,subjects in class_scores.items():
    for subject,score in subjects.items():
        print(f'{name} 的 {subject} 成绩是 {score}')
