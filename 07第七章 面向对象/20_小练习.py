"""第十一节，小练习：学生成绩管理系统"""

"""
本节对应课程大纲里的知识点：面向对象综合练习

案例目标：完成一个学生成绩管理系统小案例

┌────────────┬──────────────────────────────────────────────┐
│ 类         │ 作用                                         │
├────────────┼──────────────────────────────────────────────┤
│ Person     │ 基类：name、age、gender                      │
│ Student    │ 继承 Person，增加学号、成绩字典、平均分      │
│ Manager    │ 管理学生列表：增删查、录成绩、主菜单         │
└────────────┴──────────────────────────────────────────────┘
"""


from datetime import datetime


print("=========================== 习题区 ============================")


# 定义 Person 类：
# - 实例属性：name、age、gender
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# 定义 Student 类，继承 Person：
# - 类属性 count，用于生成学号（每次创建自动加 1）
# - 用 super() 调用父类 __init__
# - 实例属性：
#     stu_id：格式为 '年份+三位序号'，例如 '2026001'、'2026002'
#     scores：字典，格式为 {'数学': 90, '语文': 80}，初始为空
# - 方法 add_score(subject, score)：给当前学生添加成绩
# - 方法 calcu_avg()：计算并返回平均分，没有成绩时返回 0
# - __str__ 返回格式：'姓名(年龄-性别)，成绩：{...}，平均分：xx.x'
class Student(Person):
    count = 0
    def __init__(self, name, age, gender):
        Student.count += 1
        super().__init__(name,age,gender)
        stu_id = f'{datetime.today().year}{Student.count:03d}' # 设置stu_id的格式
        self.stu_id = stu_id
        scores = {} # 设为空字典
        self.scores = scores

    # 添加科目成绩
    def add_score(self, subject, score):
        self.scores[subject] = score
    # 计算成绩平均值
    def calcu_avg(self):
        # 检查有没有成绩，没有成绩就提示先录入成绩
        if self.scores == {}:
            print('目前没有科目成绩记录，请先录入各科成绩')
            return 0
        else:
            avg_score = sum(self.scores.values())/len(self.scores)
            return avg_score
    def __str__(self): #格式化打印学生信息
        if self.scores:
            return f'{self.stu_id}\n{self.name}({self.age}岁-{self.gender})\n成绩{self.scores}\n平均分：{self.calcu_avg():.1f}\n'
        else:
            return f'{self.stu_id}\n{self.name}({self.age}岁-{self.gender}),成绩暂未录入\n'

# 定义 Manager 类：
# - 实例属性：stu_list（学生列表，初始为空）
# - add_student()：从键盘输入姓名、年龄、性别，创建 Student 并加入列表，打印学号
# - del_student()：输入学号，找到则删除并提示成功，找不到则提示学号有误
# - show_all_student()：遍历打印所有学生信息；列表为空时打印'暂无学生！'
# - set_score()：
#     输入学号找到该学生；
#     输入成绩字符串，格式为：学科-分数，学科-分数（支持中文逗号）；
#     解析后调用 add_score 逐一录入
# - run()：主循环菜单，提供 1.添加 2.删除 3.查看 4.录入成绩 5.退出
class Manager:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_student(self):
        name = input('请输入姓名：')
        age = int(input('请输入年龄'))
        gender = input('请输入性别')
        student = Student(name, age, gender)
        self.stu_list.append(student)
        print(f'您的学号是：{student.stu_id}')

    # 删除学生
    def del_student(self):
        stu_id = input('请输入要删除的学生学号')
        for student in self.stu_list:
            if student.stu_id == stu_id:
                self.stu_list.remove(student)
                print(f'已删除{student.name}信息')
                return
        print('找不到该学生，请重试！')

    # 显示学生信息
    def show_students(self):
        if self.stu_list:
            for student in self.stu_list:
                print(student)
        else:
            print('学生列表为空，请先添加学生!')


    # 录入成绩
    def set_score(self):
        if self.stu_list:
            stu_id = input('请输入学号')
            for student in self.stu_list:
                if student.stu_id == stu_id:
                    subject_score = input('请按格式输入：科目-成绩，科目-成绩....')
                    subject_score = subject_score.replace('，',',')
                    result = subject_score.split(',')
                    for item in result:
                        subject, score = item.split('-')
                        student.add_score(subject, int(score))
                    return
            print('学号不存在')
        else:
            print('学生列表为空，请先添加学生！')


    def run (self):
        while True:
            print('='*25,'欢迎来到学生信息管理系统','='*25,'\n')
            print('1.添加学生')
            print('2.删除学生')
            print('3.查询学生信息')
            print('4.录入学生成绩')
            print('5.退出系统\n')
            choice = input('请输入您要选择的操作(数字)')
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.del_student()
            elif choice == '3':
                self.show_students()
            elif choice == '4':
                self.set_score()
            elif choice == '5':
                print('已退出')
                break
            else:
                print('您输入的内容无效，请输入数字1-5进行操作')

m1 = Manager()
m1.run()


