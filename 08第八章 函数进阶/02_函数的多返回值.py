"""第八章第 2 小节：函数的多返回值。

知识点：多个返回值会自动打包成元组，可以整体接收，也可以解包接收。
"""


print('=========================== 教程区 ============================')
print('本节主题：一个函数返回多个结果')


print('--------------------------- 1. 多返回值的写法 ---------------------------')
# return 后可以写多个值，多个值之间使用逗号分隔。
# Python 会把这些值自动打包成一个元组。


def calculate(x, y):
    addition = x + y
    subtraction = x - y
    return addition, subtraction


result = calculate(10, 20)
print('整体接收：', result)
print('返回值类型：', type(result))


print('--------------------------- 2. 解包接收 ---------------------------')
# 左侧可以使用相同数量的变量，分别接收元组中的值。

result1, result2 = calculate(10, 20)
print('加法结果：', result1)
print('减法结果：', result2)


print('--------------------------- 3. 返回值数量要匹配 ---------------------------')
# calculate() 返回两个元素，因此正常解包时左侧也需要两个变量。
# 如果变量数量和元素数量不一致，会产生 ValueError。
# 也可以使用星号变量接收剩余结果。


def get_student_info():
    return '张三', 18, '男', 92


name, age, *other = get_student_info()
print('姓名：', name)
print('年龄：', age)
print('其余信息：', other)


print('=========================== 知识点整理 ============================')
print('1. return 值1, 值2 本质上返回一个元组。')
print('2. 可以使用一个变量整体接收返回的元组。')
print('3. 可以使用多个变量对返回值进行解包。')
print('4. 普通解包时，变量数量必须与元素数量一致。')


print('============================ 小结区 ============================')
print('Python 函数依然只返回一个对象；所谓多返回值，是把多个值打包成元组返回。')
print('整体接收适合保留完整结果，解包接收适合直接使用每一项结果。')


print('============================ 练习区 ============================')
print('--------------------------- 练习 1 ---------------------------')
# 定义 rectangle_info(length, width)，返回面积和周长。
# 分别使用整体接收和解包接收，并打印结果。
def rectangle_info(length, width):
    area = length * width
    perimeter = 2 * length + 2 * width
    return area, perimeter


r1 = rectangle_info(10, 5)
print('整体接收', r1)
t1, t2 = rectangle_info(10, 5)
print('解包接收', '面积', t1, '周长', t2)

print('--------------------------- 练习 2 ---------------------------')
# 定义 analyse_scores(scores)，返回最高分、最低分和平均分。
# 调用函数并使用三个变量接收结果。
def analyse_scores(scores):
    max_score = max(scores)
    min_score = min(scores)
    avg_scores = sum(scores) / len(scores)
    return max_score, min_score, avg_scores


list_scores = [10, 20, 30, 40, 50]
a1, a2, a3 = analyse_scores(list_scores)
print(f'最高分{a1}\n最低分{a2}\n平均分{a3:.1f}')
