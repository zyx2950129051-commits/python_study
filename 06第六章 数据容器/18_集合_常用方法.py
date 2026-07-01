"""第十八节，集合_常用方法"""

"""
这一节代码整体在讲：集合和集合之间，最常用的 6 个关系方法。

本节对应课程大纲里的知识点：
1. difference()          求差集，返回新集合
2. difference_update()   删除重复部分，直接修改原集合
3. union()               合并两个集合，返回新集合
4. issubset()            判断是否为子集
5. issuperset()          判断是否为超集
6. isdisjoint()          判断是否没有交集

先记一句最重要的话：
- 带 update 的方法，通常更像"直接改原对象"
- 不带 update 的方法，通常更像"算出一个新结果"
"""

print('=========================== 教程区 ============================')

print('-------------------- 1. difference：求差集 ---------------------')
student_a = {'张三', '李四', '王五', '赵六'}
student_b = {'王五', '赵六', '钱七'}

only_in_a = student_a.difference(student_b)

print('A班学生：', student_a)
print('B班学生：', student_b)
print('只在A班、不在B班的学生：', only_in_a)
print()  # 输出空行

print('--------------- 2. difference_update：直接修改原集合 ---------------')
python_students = {'张三', '李四', '王五', '赵六'}
makeup_students = {'王五', '赵六'}

print('修改前：', python_students)
result = python_students.difference_update(makeup_students)
print('返回值：', result)
print('修改后：', python_students)
print()  # 输出空行

print('---------------------- 3. union：合并集合 -----------------------')
weekend_reading = {'Python入门', '数据结构'}
holiday_reading = {'数据结构', '机器学习基础', '爬虫实战'}

all_reading = weekend_reading.union(holiday_reading)

print('周末书单：', weekend_reading)
print('假期书单：', holiday_reading)
print('合并后书单：', all_reading)
print()  # 输出空行

print('------------------- 4. issubset：判断是否为子集 --------------------')
basic_skills = {'变量', '分支', '循环'}
python_skills = {'变量', '分支', '循环', '函数', '列表'}

print('基础技能是否是 Python 技能的一部分：', basic_skills.issubset(python_skills))
print('Python 技能是否是基础技能的一部分：', python_skills.issubset(basic_skills))
print()  # 输出空行

print('------------------ 5. issuperset：判断是否为超集 -------------------')
print('Python 技能是否包含基础技能：', python_skills.issuperset(basic_skills))
print('基础技能是否包含 Python 技能：', basic_skills.issuperset(python_skills))
print()  # 输出空行

print('------------------ 6. isdisjoint：判断是否没有交集 ------------------')
group_1 = {'唱歌', '跳舞'}
group_2 = {'编程', '篮球'}
group_3 = {'编程', '唱歌'}

print('group_1 和 group_2 是否没有交集：', group_1.isdisjoint(group_2))
print('group_1 和 group_3 是否没有交集：', group_1.isdisjoint(group_3))
print()  # 输出空行

print('---------------------------- 小结 ----------------------------')
print('1. difference：A 有、B 没有，返回新集合')
print('2. difference_update：从 A 里删掉和 B 重复的部分，直接改 A')
print('3. union：合并两个集合，自动去重，返回新集合')
print('4. issubset：A 的所有元素是否都在 B 里')
print('5. issuperset：A 是否把 B 的所有元素都包含了')
print('6. isdisjoint：两个集合是否完全没有重复元素')

print('=========================== 习题区 ============================')


print('--------------------------- 练习 1 ---------------------------')
# 练习 1：

print('--------------------------- 练习 2 ---------------------------')
# 练习 2：
# 有两个集合：
# old_users = {'张三', '李四', '王五', '赵六'}
# inactive_users = {'王五', '赵六'}
# 请直接修改 old_users，把 inactive_users 中出现的人删掉

print('--------------------------- 练习 3 ---------------------------')
# 练习 3：
# 有两个集合：
# class_a = {'小明', '小红', '小刚'}
# class_b = {'小红', '小刚', '小美'}
# 请合并这两个集合，并打印合并后的结果

print('--------------------------- 练习 4 ---------------------------')
# 练习 4：
# 有两个集合：
# required_topics = {'变量', '循环'}
# learned_topics = {'变量', '分支', '循环', '函数'}
# 判断：
# 1）required_topics 是否是 learned_topics 的子集
# 2）learned_topics 是否是 required_topics 的超集

print('--------------------------- 练习 5 ---------------------------')
# 练习 5：
# 有两个集合：
# team_a = {'前端', '后端'}
# team_b = {'测试', '运维'}
# team_c = {'前端', '测试'}
# 判断：
# 1）team_a 和 team_b 是否没有交集
# 2）team_a 和 team_c 是否没有交集

print('--------------------------- 练习 6 ---------------------------')

# 练习 6（综合题）：
# 有两个集合：
# boys = {'篮球', '足球', '编程', '围棋'}
# girls = {'绘画', '编程', '舞蹈'}
# 请完成：
# 1）找出只在 boys 中的兴趣
# 2）找出全部兴趣并合并
# 3）判断 girls 是否是 boys 的子集
# 4）判断 boys 和 girls 是否完全没有交集