"""第八章第 1 小节：重新认识函数。

对应课程大纲：
    111. 重新认识函数

本节知识点：
    1. 函数也是对象
    2. 函数可以动态添加属性
    3. 函数可以赋值给变量
    4. 函数参数与可变、不可变对象
    5. 函数可以作为参数
    6. 函数可以作为返回值

学习目标：
    理解函数不只是“一段可以调用的代码”，函数本身也是对象，
    因此可以像其他对象一样被保存、传递和返回。
"""


print('=========================== 教程区 ============================')
print('本节主题：重新认识函数——函数本身也是对象')


print('--------------------------- 1. 函数也是对象 ---------------------------')
# Python 中的整数、字符串和列表都是对象，函数同样也是对象。
# 定义函数时，Python 会创建一个函数对象，再让函数名指向这个对象。

a1 = 100
a2 = 'hello'
a3 = [10, 20, 30]


def welcome():
    print('你好啊！')


print('a1 的类型：', type(a1))
print('a2 的类型：', type(a2))
print('a3 的类型：', type(a3))
print('welcome 的类型：', type(welcome))

# 这里写 welcome，得到的是函数对象本身。
# 这里写 welcome()，才表示调用函数并执行函数体。
print('函数对象：', welcome)
print('调用函数：')
welcome()


print('--------------------------- 2. 函数可以动态添加属性 ---------------------------')
# 函数是对象，因此也可以像自定义类的实例一样添加属性。
# 属性只是保存在函数对象身上的附加信息，不会自动执行。

welcome.desc = '这是一个用于打招呼的函数'
welcome.version = 1.0

print('函数说明：', welcome.desc)
print('函数版本：', welcome.version)
print('函数的属性字典：', welcome.__dict__)


print('--------------------------- 3. 函数可以赋值给变量 ---------------------------')
# 赋值时只写函数名，不加小括号，保存的是函数对象。
# welcome 和 say_hello 会指向同一个函数对象。

say_hello = welcome

print('welcome 和 say_hello 是同一个对象：', welcome is say_hello)
print('通过 say_hello 调用函数：')
say_hello()

# 容易混淆的两种写法：
#   say_hello = welcome     保存函数对象，以后还可以调用
#   result = welcome()     立即调用函数，result 保存函数的返回值


print('--------------------------- 4. 不可变参数与可变参数 ---------------------------')
# 调用函数时，形参会引用实参所指向的对象。
# 函数内重新给形参赋值，与修改传入对象的内部内容，是两件不同的事。


def change_number(data):
    print('函数刚收到 data：', data)
    print('重新赋值前 data 的 id：', id(data))
    data = 888
    print('重新赋值后 data：', data)
    print('重新赋值后 data 的 id：', id(data))


number = 666
print('调用前 number：', number)
print('调用前 number 的 id：', id(number))
change_number(number)
print('调用后 number：', number)
print('调用后 number 的 id：', id(number))

# number 指向整数对象 666。
# 函数中的 data = 888 只是让局部变量 data 改为指向另一个整数对象，
# 不会让函数外的 number 跟着改变。


def change_list(data):
    print('函数刚收到 data：', data)
    print('修改前 data 的 id：', id(data))
    data[2] = 99
    print('修改后 data：', data)
    print('修改后 data 的 id：', id(data))


numbers = [10, 20, 30]
print('调用前 numbers：', numbers)
print('调用前 numbers 的 id：', id(numbers))
change_list(numbers)
print('调用后 numbers：', numbers)
print('调用后 numbers 的 id：', id(numbers))

# data[2] = 99 修改的是同一个列表对象的内部内容。
# 函数内外引用的是同一个列表，因此函数外也能看到变化。


print('--------------------------- 5. 函数可以作为参数 ---------------------------')
# 把函数作为参数传递时，传入的是函数对象，不是函数的执行结果。
# 接收函数对象的形参可以使用普通变量名，例如 function。


def caller(function):
    print('caller 准备调用接收到的函数')
    function()
    print('caller 调用结束')


caller(welcome)

# caller(welcome) 传入函数对象。
# caller(welcome()) 会先调用 welcome，再把它的返回值传给 caller，含义不同。


print('--------------------------- 6. 函数可以作为返回值 ---------------------------')
# 函数内部可以定义另一个函数，并把内部函数对象返回出去。
# return show_message 没有小括号，因此返回的是函数对象。


def create_message_function():
    print('外层函数开始执行')

    def show_message(message):
        print('收到的消息：', message)

    return show_message


message_function = create_message_function()
print('返回值的类型：', type(message_function))
message_function('欢迎学习 Python')

# 也可以把“获取函数”和“调用函数”连在一起写：
create_message_function()('函数可以作为返回值')


print('=========================== 知识点整理 ============================')
print('1. 函数由 def 创建，函数名指向创建出来的函数对象。')
print('2. 函数名表示函数对象，函数名加小括号表示调用函数。')
print('3. 函数对象可以动态添加属性，并通过函数名访问这些属性。')
print('4. 函数可以赋值给其他变量，多个名字可以指向同一个函数。')
print('5. 形参会引用传入的对象；重新赋值和修改对象内容不是同一件事。')
print('6. 函数可以作为参数交给其他函数，由其他函数决定何时调用。')
print('7. 函数可以作为返回值，让调用者在之后继续调用。')


print('============================ 小结区 ============================')
print('函数也是对象，这是本节所有知识点的基础。')
print('因为函数是对象，所以它可以拥有属性、赋值给变量、作为参数和返回值。')
print('判断代码含义时，要先看函数名后面有没有小括号：')
print('没有小括号，通常表示取得函数对象；有小括号，表示立即调用函数。')
print('传递普通数据时，还要区分函数内是在重新给形参赋值，还是在修改可变对象。')


print('============================ 练习区 ============================')


print('--------------------------- 练习 1 ---------------------------')
# 定义函数 introduce，打印一句自我介绍。
# 1）打印 introduce 的类型。
# 2）给 introduce 添加 desc 属性并打印。
# 3）把 introduce 赋值给另一个变量，再通过新变量调用函数。


print('--------------------------- 练习 2 ---------------------------')
# 定义两个无参数函数：study_python 和 take_a_break。
# 再定义 execute(function)，在函数内部调用接收到的 function。
# 分别把前两个函数传给 execute，观察执行结果。


print('--------------------------- 练习 3 ---------------------------')
# 定义函数 create_calculator(operator)：
# 1）在内部定义一个接收 a、b 的函数。
# 2）operator 为 '+' 时返回两数之和，为 '-' 时返回两数之差。
# 3）外层函数返回这个内部函数对象。
# 4）分别得到加法函数和减法函数并调用。


print('--------------------------- 练习 4 ---------------------------')
# 准备一个整数和一个列表，分别传入两个函数：
# 1）在第一个函数中给整数形参重新赋值。
# 2）在第二个函数中修改列表中的一个元素。
# 3）调用前后分别打印值和 id。
# 4）用注释说明两种结果为什么不同。

