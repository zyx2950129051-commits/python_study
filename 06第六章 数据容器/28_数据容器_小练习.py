"""第二十五节，数据容器_小练习"""


"""
综合运用所有数据容器的知识点：
- 列表：增删改查、常用方法、内置函数、循环遍历
- 元组：定义、访问、解包
- 字符串：切片、常用方法
- 集合：去重、数学运算、遍历
- 字典：增删改查、keys/values/items、遍历
- 通用操作：类型转换函数、成员运算符 in / not in
"""


print('=========================== 习题区 ============================')


print('--------------------------- 练习 1 ---------------------------')
# 练习 1（列表 + 元组）：
# 有如下成绩数据：
# scores = (90, 85, 78, 92, 88, 76, 95, 83)
# 请完成：
# 1）将元组转换成列表
# 2）在列表末尾追加一个新成绩 80
# 3）用 sorted 获取降序排列的新列表
# 4）打印最高分、最低分、平均分
scores = (90, 85, 78, 92, 88, 76, 95, 83)
list_scores = list(scores)
list_scores.append(80)
list_scores.sort(reverse=True)
print(max(list_scores),min(list_scores),sum(list_scores)/len(list_scores))

print('--------------------------- 练习 2 ---------------------------')
# 练习 2（字符串 + 集合）：
# 有如下字符串：
# text = 'hello world hello python hello world'
# 请完成：
# 1）将字符串按空格拆分成列表
# 2）用集合去重，看看有哪些不重复的单词
# 3）统计一共有多少个不重复的单词
text = 'hello world hello python hello world'

list_text = text.split(' ')
print(list_text)

set_text = set(list_text)
print(set_text)

print(len(set_text))

print('--------------------------- 练习 3 ---------------------------')
# 练习 3（字典 + 通用操作）：
# 有如下字典：
# fruits = {'苹果': 5, '香蕉': 3, '橙子': 4, '葡萄': 8, '西瓜': 6}
# 请完成：
# 1）用 in 判断 '苹果' 是否在字典中
# 2）用 in 判断 5 是否在字典中（思考结果）
# 3）将字典的所有 key 转换成列表
# 4）将字典的所有 value 转换成元组
# 5）用 items 遍历打印每种水果的价格
fruits = {'苹果': 5, '香蕉': 3, '橙子': 4, '葡萄': 8, '西瓜': 6}
'''1'''
print('苹果'in fruits)
'''2'''
print(5 in fruits) # 不在因为in只能判断key不可以判断value，5是value
'''3'''
key_list = list(fruits.keys())
print(key_list,type(key_list))
'''4'''
value_tuple = tuple(fruits.values())
print(value_tuple,type(value_tuple))
'''5'''
for key, value in fruits.items():
    print(f'{key}的价格是{value}元')

print('--------------------------- 练习 4 ---------------------------')
# 练习 4（集合数学运算）：
# 某班有两次点名记录：
# morning = {'张三', '李四', '王五', '赵六', '钱七'}
# afternoon = {'李四', '王五', '孙八', '周九', '赵六'}
# 请用集合运算完成：
# 1）两次都到的人（交集）
# 2）至少到过一次的人（并集）
# 3）只来了早上没来下午的人（差集）
# 4）有一个人两次点名记录不一样（对称差集）
morning = {'张三', '李四', '王五', '赵六', '钱七'}
afternoon = {'李四', '王五', '孙八', '周九', '赵六'}
'''1'''
print(morning & afternoon)
'''2'''
print(morning | afternoon)
'''3'''
print(morning - afternoon)
'''4'''
print(morning ^ afternoon)

print('--------------------------- 练习 5 ---------------------------')
# 练习 5（列表 + 字典 综合）：
# 有如下学生成绩列表：
# students = [
#     {'name': '张三', 'score': 85},
#     {'name': '李四', 'score': 92},
#     {'name': '王五', 'score': 78},
#     {'name': '赵六', 'score': 90},
#     {'name': '钱七', 'score': 60}
# ]
# 请完成：
# 1）打印所有不及格（< 60）的学生姓名
# 2）把所有人的成绩都加 5 分（加分后不超过 100）
# 3）按成绩从高到低排序（提示：可以用列表的 sort 方法，key 参数）
# 4）打印排名前三的学生姓名和成绩
students = [
    {'name': '张三', 'score': 85},
    {'name': '李四', 'score': 92},
    {'name': '王五', 'score': 78},
    {'name': '赵六', 'score': 90},
    {'name': '钱七', 'score': 60}
]
'''1'''
for student in students:
    if student['score'] < 60:
        print(student['name'])
'''2'''
for student in students:
    if student['score'] + 5 <= 100:
        student['score'] += 5
        print(student)
'''3'''
def get_score(student):
    return student['score']
sorted_students = sorted(students, key=get_score, reverse=True)
print(sorted_students)
'''4'''
print(sorted_students[0])
print(sorted_students[1])
print(sorted_students[2])

print('--------------------------- 练习 6 ---------------------------')
# 练习 6（全容器综合）：
# 某图书馆有以下数据：
# 图书字典：books = {1001:'Python入门', 1002:'数据结构', 1003:'算法导论', 1004:'操作系统', 1005:'计算机网络'}
# 借阅状态集合：borrowed = {1002, 1004}
# 请完成：
# 1）用 in 判断 1003 是否被借出
# 2）遍历字典，打印每本书的编号、名称和借阅状态（已借出/在馆）
# 3）将所有在馆的图书编号提取成一个列表

# dict 字典
books = {1001:'Python入门', 1002:'数据结构', 1003:'算法导论', 1004:'操作系统', 1005:'计算机网络'}
# set 集合
borrowed = {1002, 1004}

print(1003 in borrowed)

for num,name in books.items():
    if num in borrowed:
        print(num,name,'已借出')
    else:
        print(num,name,'在馆')

list_books = []
for num in books.keys():
    if num not in borrowed:
        list_books.append(num)
print(list_books)

