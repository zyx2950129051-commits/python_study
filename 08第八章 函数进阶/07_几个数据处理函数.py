"""第八章第 7 小节：几个数据处理函数。

知识点：map 加工、filter 筛选、sorted 排序、reduce 归并。
"""


from functools import reduce


print('=========================== 教程区 ============================')
print('本节主题：对一组数据进行加工、筛选、排序和归并')


print('--------------------------- 1. map：逐个加工 ---------------------------')
# map(操作函数, 可迭代对象)
# map 不修改原数据，返回一个迭代器对象。

numbers = [10, 20, 30, 40]
mapped = map(lambda number: number * 2, numbers)

print('map 返回值类型：', type(mapped))
print('加工结果：', list(mapped))
print('原列表：', numbers)

# 迭代器遍历一次后会被耗尽。
mapped_again = map(lambda number: number + 1, numbers)
print('第一次转换：', list(mapped_again))
print('第二次转换：', list(mapped_again))


print('--------------------------- 2. filter：按条件筛选 ---------------------------')
# filter(判断函数, 可迭代对象)
# 判断函数返回真值的元素会被保留，元素数量可能减少。

filtered = filter(lambda number: number > 25, numbers)
print('大于 25：', list(filtered))

data = [0, 1, '', 'hello', [], (), 5]
print('过滤假值：', list(filter(None, data)))


print('--------------------------- 3. sorted：生成排序后的新列表 ---------------------------')
# sorted(可迭代对象, key=排序依据, reverse=False)
# sorted 不修改原数据，而是返回一个新列表。
# reverse=True 表示降序，key 用来指定排序依据。
# 如果要原地排序，列表还有 sort() 方法：list.sort(key=排序依据, reverse=False)

unsorted_numbers = [30, 40, 20, 10]
print('数字降序：', sorted(unsorted_numbers, reverse=True))
print('原列表不变：', unsorted_numbers)

names = ['python', 'sql', 'javascript', 'java']
print('按长度排序：', sorted(names, key=len))

persons = [
    {'name': '张三', 'age': 15},
    {'name': '李四', 'age': 19},
    {'name': '王五', 'age': 17}
]
print('按年龄降序：', sorted(persons, key=lambda person: person['age'], reverse=True))
print('年龄最大：', max(persons, key=lambda person: person['age']))
print('年龄最小：', min(persons, key=lambda person: person['age']))


print('--------------------------- 4. reduce：逐步归并 ---------------------------')
# reduce(合并函数, 可迭代对象, 初始值)
# 它把前一次结果和下一个元素继续合并，最终得到一个结果。

values = [1, 2, 3, 4, 5]
print('没有初始值：', reduce(lambda a, b: a + b, values))
print('初始值为 10：', reduce(lambda a, b: a + b, values, 10))

text_list = ['ab', 'cd', 'ef']
print('拼接字符串：', reduce(lambda a, b: a + b, text_list))


print('=========================== 知识点整理 ============================')
print('1. map 对每个元素执行同一种加工，通常不改变元素数量。')
print('2. filter 保留符合条件的元素，结果数量可能减少。')
print('3. map 和 filter 返回迭代器，使用后可能被耗尽。')
print('4. sorted 返回新的排序列表，key 指定依据，reverse 指定方向。')
print('5. reduce 把一组数据连续合并为一个最终结果。')


print('============================ 小结区 ============================')
print('map 负责加工，filter 负责筛选，sorted 负责排序，reduce 负责归并。')
print('选择函数时先判断目标：是逐项变化、减少元素、调整顺序，还是汇总成一个值。')


print('============================ 练习区 ============================')
print('--------------------------- 练习 1 ---------------------------')
# 题目：使用 map，把字符串列表中的每个元素转换为整数。
# 输入：['10', '20', '30']
# 目标结果：[10, 20, 30]
# 标准格式：map(加工函数, 可迭代对象)
list1 = ['10', '20', '30']
mapped_list = map(int, list1)
print(list(mapped_list))

print('--------------------------- 练习 2 ---------------------------')
# 题目：使用 filter，从学生字典列表中筛选出成绩大于等于 60 分的学生。
# 注意：每个元素是字典，成绩保存在元素['score'] 中，不是直接比较整个字典。
# 目标：保留张三、赵六、李四，过滤掉周七、王五。
scores = [
    {'name': '张三', 'age': 17, 'gender': '男', 'score': 88},
    {'name': '周七', 'age': 18, 'gender': '女', 'score': 56},
    {'name': '赵六', 'age': 16, 'gender': '女', 'score': 74},
    {'name': '王五', 'age': 17, 'gender': '男', 'score': 46},
    {'name': '李四', 'age': 18, 'gender': '男', 'score': 97},
]
filtered_scores = list(filter(lambda score: score['score'] >= 60, scores))
print(filtered_scores)

print('--------------------------- 练习 3 ---------------------------')
# 题目：使用 sorted，按照学生字典中的 score 字段，将学生成绩从高到低排序。
# 注意：sorted 会返回新列表，原来的 scores 列表不变。
# 标准格式：sorted(可迭代对象, key=排序依据, reverse=True)
sorted_scores = sorted(scores, key=lambda score: score['score'], reverse=True)

print(sorted_scores)
print('--------------------------- 练习 4 ---------------------------')
# 题目：使用 reduce，把列表中的数字依次相乘，计算最终乘积。
# 输入：[1, 2, 3, 4, 5]
# 目标结果：120
# 标准格式：reduce(合并函数, 可迭代对象)
num = [1, 2, 3, 4, 5]
reduced_num = reduce(lambda a, b: a * b, num)
print(reduced_num)
