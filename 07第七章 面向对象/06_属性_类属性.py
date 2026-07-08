"""第三节，类属性"""

"""
本节对应课程大纲里的知识点：类属性

┌────────────┬────────────────────────────────────────────────────┐
│ 属性类型   │ 说明                                                 │
├────────────┼────────────────────────────────────────────────────┤
│ 类属性     │ 保存在类身上，所有实例默认共享同一份                      │
│ 访问顺序   │ 实例.属性 会先找实例自己，再找类                         │
│ 赋值特点   │ 实例.属性 = 值 只会修改或新增实例自己的属性                │
│ 适用场景   │ 公共数据用类属性                                       │
└────────────┴────────────────────────────────────────────────────┘

先记一句最重要的话：
- 类属性属于整个类。
"""


print('=========================== 教程区 ============================')

print('----------------------------- 1. 类属性 -----------------------------')
# 类属性：直接写在类里面、方法外面的变量。
#
# 特点：
#   1. 保存在类身上
#   2. 可以通过类访问
#   3. 实例也可以访问到
#   4. 适合保存所有实例共享的数据


class Animal:
    planet = '地球'
    max_age = 120

    def __init__(self, name, age):
        self.name = name
        if age <= Animal.max_age:
            self.age = age
        else:
            print(f'年龄超出范围，已设置为最大值 {Animal.max_age}')
            self.age = Animal.max_age


print(Animal.planet)
# 输出：地球

print(Animal.max_age)
# 输出：120

a1 = Animal('小猫', 3)
a2 = Animal('老牛', 200)
# 输出：年龄超出范围，已设置为最大值 120

print(a1.planet)
# 输出：地球

print(a2.__dict__)
# 输出：{'name': '老牛', 'age': 120}

print()


print('----------------------- 2. 属性查找顺序 -----------------------')
# 当执行 实例.属性名 时：
#   1. 先找实例自己身上有没有这个属性
#   2. 如果实例没有，再去类身上找
#   3. 如果类也没有，就报 AttributeError

print(a1.name)
# 输出：小猫      name 是实例属性，来自 a1 自己

print(a1.planet)
# 输出：地球      planet 是类属性，来自 Animal 类

# 取消下面代码的注释会报错：
# print(a1.color)
# 报错：AttributeError: 'Animal' object has no attribute 'color'

print()


print('------------------- 3. 实例赋值不影响类属性 -------------------')
# 重点：
#   实例.属性名 = 值
#
# 这句代码永远优先操作实例自己：
#   1. 实例自己有这个属性，就修改实例属性
#   2. 实例自己没有这个属性，就新增实例属性
#
# 即使类里有同名类属性，也不会直接修改类属性。

print(Animal.planet)
# 输出：地球

a1.planet = '火星'

print(a1.__dict__)
# 输出：{'name': '小猫', 'age': 3, 'planet': '火星'}

print(a1.planet)
# 输出：火星

print(a2.planet)
# 输出：地球

print(Animal.planet)
# 输出：地球

print()


print('----------------------- 4. 修改类属性 -----------------------')
# 如果确实要修改类属性，推荐通过类名修改。

Animal.planet = '蓝色星球'

print(Animal.planet)
# 输出：蓝色星球

print(a2.planet)
# 输出：蓝色星球

print(a1.planet)
# 输出：火星
#
# 注意：a1 自己身上已经有 planet 实例属性，
# 所以 a1.planet 会先找到自己的 '火星'，不会再去类里找。

print()


print('============================ 小结 ============================')
# 1. 类属性写在类身上，通常用于所有对象共享的数据。
# 2. 读取 实例.属性 时，先找实例，再找类。
# 3. 修改类属性时，推荐写：类名.类属性 = 新值。


print('=========================== 习题区 ============================')

print('--------------------------- 练习 1 ---------------------------')
# 定义 Dog 类：
#   - 实例属性：name、age
#   - 类属性：species = '犬科'
# 创建两个 Dog 实例，并打印它们各自的 name、age、species。
class Dog:
    species = '犬科'
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1 = Dog('大黄',5)
dog2 = Dog('笨笨',3)
print(f'{dog1.name}的年龄是{dog1.age}岁，属于{dog1.species}')
print(f'{dog2.name}的年龄是{dog2.age}岁，属于{dog2.species}')

print('--------------------------- 练习 2 ---------------------------')
# 分别通过 Dog.species 和 dog1.species 访问类属性。
# 思考：这两种访问方式拿到的是不是同一个值？
print(Dog.species)
print(dog1.species)
'''是同一个值'''

print('--------------------------- 练习 3 ---------------------------')
# 给 dog1 单独设置 dog1.species = '猫科'。
# 再分别打印：
#   Dog.species
#   dog1.species
#   dog2.species
# 观察三者是否相同，并解释原因。
dog1.species = ('猫科')
print(dog1.species)
print(dog2.species)
print(Dog.species)
'''
当执行  dog1.species = '猫科'时，其实并没有修改到类属性
而是给实例  dog1  新建了一个名为  species 的实例属性（造成了属性屏蔽）
因此， dog1.species 拿到的是它的实例属性 '猫科' 
而 dog2.species  与  Dog.species 依然指向类属性 '犬科'，三者便不再相同
'''
print('--------------------------- 练习 4 ---------------------------')
# 定义 Counter 类，类属性 count = 0。
# 每创建一个实例，就让 Counter.count 加 1。
# 连续创建 3 个实例后，打印 Counter.count。
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count)

print('--------------------------- 练习 5 ---------------------------')
# 预测下面代码的输出：
#   class T:
#       x = 10
#
#   t = T()
#   t.x = 20
#   print(T.x)
#   print(t.x)
#
# 请解释：t.x = 20 修改的是类属性，还是实例属性？
'''
T.x是10
t.x是20
t.x = 20 修改的是实例属性
'''
