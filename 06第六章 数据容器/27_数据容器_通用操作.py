"""第二十四节，数据容器_通用操作"""

"""
这一节代码整体在讲：所有数据容器共用的类型转换函数和成员运算符。

本节对应课程大纲里的知识点：
1. list 函数：定义空列表 / 将可迭代对象转换为列表
2. tuple 函数：定义空元组 / 将可迭代对象转换为元组
3. set 函数：定义空集合 / 将可迭代对象转换为集合
4. str 函数：定义空字符串 / 将任意类型转换为字符串
5. dict 函数：定义空字典 / 将可迭代对象转换为字典
6. 成员运算符 in / not in：判断元素是否在容器中

先记一句最重要的话：
- 这五个函数既能定义空容器，又能把一种容器转换成另一种容器
"""

print('============================ 教程区 ============================')

print('--------------------- 1. list 函数 ------------------------')
# list 函数：1.定义空列表  2.将【可迭代对象】转换为列表

res1 = list(range(8))
res2 = list('欢迎来到尚硅谷')
res3 = list({10, 20, 30, 40, 50})
res4 = list({'张三': 75, '李四': 60, '王五': 85}.items())
print(type(res1), res1)  # 输出：<class 'list'> [0, 1, 2, 3, 4, 5, 6, 7]
print(type(res2), res2)  # 输出：<class 'list'> ['欢', '迎', '来', '到', '尚', '硅', '谷']
print(type(res3), res3)  # 输出：<class 'list'> [10, 20, 30, 40, 50]（顺序可能不同）
print(type(res4), res4)  # 输出：<class 'list'> [('张三', 75), ('李四', 60), ('王五', 85)]
print()

print('--------------------- 2. tuple 函数 -----------------------')
# tuple 函数：1.定义空元组  2.将【可迭代对象】转换为元组

res1 = tuple(range(8))
res2 = tuple('欢迎来到尚硅谷')
res3 = tuple({10, 20, 30, 40, 50})
res4 = tuple({'张三': 75, '李四': 60, '王五': 85})
print(type(res1), res1)  # 输出：<class 'tuple'> (0, 1, 2, 3, 4, 5, 6, 7)
print(type(res2), res2)  # 输出：<class 'tuple'> ('欢', '迎', '来', '到', '尚', '硅', '谷')
print(type(res3), res3)  # 输出：<class 'tuple'> (10, 20, 30, 40, 50)（顺序可能不同）
print(type(res4), res4)  # 输出：<class 'tuple'> ('张三', '李四', '王五')
print()

print('---------------------- 3. set 函数 ------------------------')
# set 函数：1.定义空集合  2.将【可迭代对象】转换为集合

res1 = set(range(8))
res2 = set('欢迎来到尚硅谷')
res3 = set({10, 20, 30, 40, 50})
res4 = set({'张三': 75, '李四': 60, '王五': 85})
print(type(res1), res1)  # 输出：<class 'set'> {0, 1, 2, 3, 4, 5, 6, 7}
print(type(res2), res2)  # 输出：<class 'set'> {'欢', '迎', '来', '到', '尚', '硅', '谷'}
print(type(res3), res3)  # 输出：<class 'set'> {10, 20, 30, 40, 50}
print(type(res4), res4)  # 输出：<class 'set'> {'张三', '李四', '王五'}
print()

print('---------------------- 4. str 函数 ------------------------')
# str 函数：1.定义空字符串  2.将【任意类型】转换为字符串

res1 = str(range(8))
res2 = str({10, 20, 30})
res3 = str({'张三': 75, '李四': 60})
res4 = str(False)
res5 = str(None)
res6 = str(100)
print(type(res1), res1)  # 输出：<class 'str'> range(0, 8)
print(type(res2), res2)  # 输出：<class 'str'> {10, 20, 30}
print(type(res3), res3)  # 输出：<class 'str'> {'张三': 75, '李四': 60}
print(type(res4), res4)  # 输出：<class 'str'> False
print(type(res5), res5)  # 输出：<class 'str'> None
print(type(res6), res6)  # 输出：<class 'str'> 100
print()

print('---------------------- 5. dict 函数 -----------------------')
# dict 函数：1.定义空字典  2.将【可迭代对象】转换为字典
# 注意：交给 dict 的内容必须是键值对，否则会报错

res1 = dict({'张三': 75, '李四': 60, '王五': 85})
res2 = dict([('张三', 75), ('李四', 60), ('王五', 85)])
res3 = dict((('张三', 75), ('李四', 60), ('王五', 85)))
print(type(res1), res1)  # 输出：<class 'dict'> {'张三': 75, '李四': 60, '王五': 85}
print(type(res2), res2)  # 输出：<class 'dict'> {'张三': 75, '李四': 60, '王五': 85}
print(type(res3), res3)  # 输出：<class 'dict'> {'张三': 75, '李四': 60, '王五': 85}
print()

print('------------------- 6. 成员运算符 in / not in -------------------')
# in / not in：判断某个元素是否在容器中

hobby = ['抽烟', '喝酒', '烫头']
nums = (10, 20, 30, 40, 50)
message = 'hello,atgiugu'
citys = {'北京', '天津', '上海', '重庆'}
score = {'张三': 75, '李四': 60, '王五': 85}

print('喝酒' in hobby)       # 输出：True
print(20 not in nums)        # 输出：False
print('hel' in message)      # 输出：True
print('上海' in citys)       # 输出：True
print('李华' not in score)   # 输出：True
print()

print('============================ 小结 ============================')
# 1. list / tuple / set / str / dict 这五个函数：
#    既能定义对应的空容器，又能将【可迭代对象】转换为对应类型
# 2. dict 函数比较特殊，传入的内容必须是键值对形式
# 3. 所有数据容器都支持成员运算符 in / not in
# 4. 字典中用 in 判断的是 key，不是 value

print('=========================== 习题区 ============================')


print('--------------------------- 练习 1 ---------------------------')
# 练习 1：
# 有一个元组 t = (10, 20, 30, 40, 50)
# 请用 list 函数将它转换成列表，再用 set 函数将它转换成集合
# 分别打印类型和结果
t = (10, 20, 30, 40, 50)
list_t = list(t)
print(type(list_t), list_t)
set_t = set(t)
print(type(set_t), set_t)

print('--------------------------- 练习 2 ---------------------------')
# 练习 2：
# 有一个列表 nums = [1, 2, 2, 3, 3, 3, 4, 4, 5]
# 请利用某个函数实现去重，并打印结果
nums = [1, 2, 2, 3, 3, 3, 4, 4, 5]
set_nums = set(nums)
print(set_nums)

print('--------------------------- 练习 3 ---------------------------')
# 练习 3：
# 有一个列表 pairs = [('a', 1), ('b', 2), ('c', 3)]
# 请用 dict 函数将它转换成字典，并打印结果
pairs = [('a', 1), ('b', 2), ('c', 3)]
dict_pairs = dict(pairs)
print(dict_pairs)

print('--------------------------- 练习 4 ---------------------------')
# 练习 4：
# 有一个字典 info = {'name': '小明', 'age': 18, 'city': '北京'}
# 请用 in 运算符判断：
# 1）'name' 是否在字典中
# 2）'小明' 是否在字典中
# 打印结果并思考：in 对字典判断的是 key 还是 value？
info = {'name': '小明', 'age': 18, 'city': '北京'}
print('name' in info)
print('小明' in info)
# in对字典的判断是是key，不是value

print('--------------------------- 练习 5 ---------------------------')
# 练习 5：
# 有一个字符串 s = 'python'
# 请用 tuple 函数将它转换成元组，再用 set 函数将它转换成集合
# 观察两种结果有什么区别
s = 'python'
tuple_s = tuple(s)
print(type(tuple_s), tuple_s)
set_s = set(s)
print(type(set_s), set_s)
#元祖保留了顺序，集合顺序是随机的

print('--------------------------- 练习 6 ---------------------------')
# 练习 6（综合题）：
# 有如下数据：
# students = [('张三', 85), ('李四', 92), ('王五', 78)]
# 请完成：
# 1）将列表转换成字典
# 2）用 in 判断 '李四' 是否在字典的 key 中
# 3）用 in 判断 92 是否在字典的 value 中
# 4）将字典的所有 key 转换成元组
# 5）将字典的所有 value 转换成列表
students = [('张三', 85), ('李四', 92), ('王五', 78)]
students_dict = dict(students)
print(type(students_dict), students_dict)
print('李四' in students_dict)

students_values = students_dict.values()
print( 92 in students_values)

students_keys = students_dict.keys()
students_keys_tuple = tuple(students_keys)
print(type(students_keys_tuple), students_keys_tuple)

students_values = list(students_values)
print(type(students_values), students_values)