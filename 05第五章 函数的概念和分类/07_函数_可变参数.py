"""第七节，函数的可变参数"""

"""
1. *args：可变位置参数，接收任意数量的位置参数，打包成元组
2. **kwargs：可变关键字参数，接收任意数量的关键字参数，打包成字典
3. *args 和 **kwargs 可以同时使用，*args 必须在 **kwargs 前面
4. 有默认值的参数可以和可变参数混用，**kwargs 必须放最后
"""


# 定义函数：可变位置参数 *args 去接收,args就是元组
def test1 (*args):
    print(args)
test1(1,55.4,3,'你好')

# 可变关键字参数：
# 定义函数时，在形参名前加 ** 可以接收任意数量的关键字参数，并打包成一个字典。
def test2 (**kwargs):
    print(kwargs)
test2(a='wow',b= 'QAQ',c= '哈哈哈haha')

# 可变位置参数和可变关键字参数可以同时写，但是可变位置参数必须在前面
# 可变位置参数和可变关键字参数可以与其他参数一起写，可变关键字必须放最后
def test3 (c1,*args,c2='大家好',**kwargs):
    print(args)
    print(kwargs)
    print(c1) 
    print(c2)
test3(1,2,3,c2='啦啦啦',num=4)

