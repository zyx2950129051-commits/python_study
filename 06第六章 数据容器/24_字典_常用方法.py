"""第二十四节，字典_常用方法"""

"""
这一节代码整体在讲：字典的三个常用方法 keys、values、items。

本节对应课程大纲里的知识点：
1. keys 方法：获取字典中所有的键
2. values 方法：获取字典中所有的值
3. items 方法：获取字典中所有的键值对

先记一句最重要的话：
- keys/values/items 返回的不是列表，是各自的专属类型，可遍历但不能用下标访问
"""

print('========================== 教程区 ==========================')

# 共用定义
scores = {'张三': 72, '李四': 60, '王五': 85}

print('----------------------- 1. keys 方法 -----------------------')
# keys：获取字典中所有的键，返回类型是 dict_keys

result = scores.keys()
print(result)        # 可能输出：dict_keys(['张三', '李四', '王五'])
print(type(result))  # 输出：<class 'dict_keys'>

# dict_keys 可遍历，但不能用下标访问

for key in result:
    print(key)

# 用 list() 可转换为列表

keys_list = list(result)
print(keys_list)  # 可能输出：['张三', '李四', '王五']

print('---------------------- 2. values 方法 ----------------------')
# values：获取字典中所有的值，返回类型是 dict_values

result = scores.values()
print(result)        # 可能输出：dict_values([72, 60, 85])
print(type(result))  # 输出：<class 'dict_values'>

# 用 list() 同样可转换为列表

values_list = list(result)
print(values_list)  # 可能输出：[72, 60, 85]

print('---------------------- 3. items 方法 -----------------------')
# items：获取所有键值对，每组以元组形式呈现，返回类型是 dict_items

result = scores.items()
print(result)        # 可能输出：dict_items([('张三', 72), ('李四', 60), ('王五', 85)])
print(type(result))  # 输出：<class 'dict_items'>

# 可直接用两个变量接收元组中的 key 和 value

for key, value in result:
    print(f'{key} 的成绩是 {value}')

print('=========================== 小结 ===========================')
# 1. keys()：获取所有键，返回 dict_keys
# 2. values()：获取所有值，返回 dict_values
# 3. items()：获取所有键值对，返回 dict_items
# 4. 三者都可遍历，可用 list() 转换为列表，但不能用下标访问

print('========================== 习题区 ==========================')


print('-------------------------- 练习 1 --------------------------')
# 练习 1：
# 有一个字典：
# fruit_prices = {'苹果': 5, '香蕉': 3, '橙子': 4, '葡萄': 8}
# 请分别打印：
# 1）所有水果名（keys）
# 2）所有价格（values）
fruit_prices = {'苹果': 5, '香蕉': 3, '橙子': 4, '葡萄': 8}
print(fruit_prices.keys())
print(fruit_prices.values())

print('-------------------------- 练习 2 --------------------------')
# 练习 2：
# 有一个字典：
# fruit_prices = {'苹果': 5, '香蕉': 3, '橙子': 4, '葡萄': 8}
# 请用 items 遍历打印 "苹果的价格是 5 元" 的格式
result = fruit_prices.items()
for key, value in result:
    print(f'{key}的价格是 {value} 元')
print('-------------------------- 练习 3 --------------------------')
# 练习 3：
# 有一个字典：
# scores = {'张三': 72, '李四': 60, '王五': 85}
# 请用 list() 分别将 keys() 和 values() 的结果转换成列表，并打印
scores = {'张三': 72, '李四': 60, '王五': 85}
result_key = scores.keys()
print(list(result_key))
result_value = scores.values()
print(list(result_value))