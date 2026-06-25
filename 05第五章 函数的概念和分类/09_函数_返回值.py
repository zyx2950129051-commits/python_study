"""第九节，函数的返回值"""

"""
1. return：将函数的计算结果返回给调用方
2. 用变量接收返回值：result = 函数名()
3. 函数遇到 return 后立即结束，后面的代码不再执行
4. 没有 return 或 return 后不跟值，函数返回 None
5. return 可以返回任意类型的数据
"""


def wow (a,b):
    print(f'我收到了{a},{b}')
    return a+b

result = wow(15, 16)
print(result)
