"""第八章第 8 小节：列表推导式。

知识点：列表推导式、条件筛选、字典推导式、集合推导式、生成器表达式。
"""


print('=========================== 教程区 ============================')
print('本节主题：用简洁语法从可迭代对象生成新容器')


print('--------------------------- 1. 列表推导式基本语法 ---------------------------')
print('语法：[表达式 for 变量 in 可迭代对象]')

numbers = [10, 20, 30, 40]

result_by_loop = []
for number in numbers:
    result_by_loop.append(number * 2)

result_by_comprehension = [number * 2 for number in numbers]

print('for + append：', result_by_loop)
print('列表推导式：', result_by_comprehension)
print('原列表：', numbers)


print('--------------------------- 2. 带条件的列表推导式 ---------------------------')
print('语法：[表达式 for 变量 in 可迭代对象 if 条件]')
# if 写在 for 后面，只保留满足条件的元素。

filtered_result = [number * 2 for number in numbers if number > 20]
print('只处理大于 20 的数字：', filtered_result)


print('--------------------------- 3. 字典推导式 ---------------------------')
print('语法：{键表达式: 值表达式 for 变量 in 可迭代对象}')
names = ['张三', '李四', '王五']
scores = [60, 70, 80]

score_dict = {names[index]: scores[index] for index in range(len(names))}
print('成绩字典：', score_dict)


print('--------------------------- 4. 集合推导式 ---------------------------')
print('语法：{表达式 for 变量 in 可迭代对象}')
words = ['python', 'java', 'python', 'sql']
upper_words = {word.upper() for word in words}
print('转大写并去重：', upper_words)


print('--------------------------- 5. 圆括号不是元组推导式 ---------------------------')
print('语法：(表达式 for 变量 in 可迭代对象)')
# Python 没有元组推导式。
# 圆括号中的推导写法会创建生成器对象，生成器将在后续章节详细学习。

generator = (name + '！' for name in names)
print('圆括号推导的类型：', type(generator))
print('转换为元组：', tuple(generator))


print('=========================== 知识点整理 ============================')
print('1. 列表推导式是 for + append 的简洁写法。')
print('2. for 后可以添加 if 条件，决定哪些元素参与生成。')
print('3. 字典推导式生成键值对，集合推导式生成集合并自动去重。')
print('4. 圆括号推导产生生成器，不是元组。')
print('5. 逻辑过于复杂时应改用普通循环，优先保证可读性。')


print('============================ 小结区 ============================')
print('推导式用于根据旧数据生成新容器，不会自动修改原容器。')
print('简单转换和筛选适合推导式，多层复杂逻辑更适合普通循环。')


print('============================ 练习区 ============================')
print('--------------------------- 练习 1 ---------------------------')
# 使用列表推导式生成 1 到 10 的平方列表。
squares = [num ** 2 for num in range(1, 11)]
print(squares)

print('--------------------------- 练习 2 ---------------------------')
# 从 1 到 20 中筛选偶数，并生成这些偶数的平方列表。
num_double = [num ** 2 for num in range(1, 21) if num %2 == 0]
print(num_double)
print('--------------------------- 练习 3 ---------------------------')
# 根据姓名列表和成绩列表生成姓名到成绩的字典。
list_names = ['张三', '李四', '王五']
list_scores = [100, 78, 84]

dict_names_and_scores = {list_names[i]: list_scores[i] for i in range(len(list_names))}
print(dict_names_and_scores)

