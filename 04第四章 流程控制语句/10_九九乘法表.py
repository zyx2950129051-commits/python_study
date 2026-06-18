"""第10节，学习九九乘法表"""

"""
1. 九九乘法表是嵌套循环的经典练习案例
2. 外层循环通常用来控制行数，内层循环用来控制每一行打印的列数
3. 每一行输出完成后，需要使用print()换行，保证格式整齐
4. 本例分别使用for循环和while循环实现了九九乘法表
5. 通过这个案例，可以进一步熟悉嵌套循环和格式输出的写法
"""


for row in range(1, 10):
     for item in range(1, row + 1):
         print(f'{row}x{item}={row*item} ', end = '\t')
     print(' ')

row1 = 1
while row1 < 10:
    item1 = 1
    while item1 <= row1:
        print(f'{row1}*{item1}={row1 * item1}',end = '\t')
        item1 += 1
    print('')
    row1 += 1
