"""第四节，关键字参数"""

"""
1. 关键字参数：调用时用 形参名=值 的方式传参，顺序可以随意
2. 关键字参数和位置参数可以混用，但位置参数必须在关键字参数前面
3. 使用关键字参数可以让代码更清晰，不容易传错位置
"""


def id (name, gender, age, height, weight):
    print(f'我叫{name},我今年{age}岁了，呃，呃呃。我有{weight}斤重，{height}米高，然后然后，我是{gender}生。')




id('小周','女',18,1.65,110)

id(name='小周',age=18,weight=110,height=1.65,gender='男')

id('小周','女',weight=110,age=18,height=1.65)
