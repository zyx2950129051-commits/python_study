"""第3节，学习多分支"""

"""
1. 多分支结构用于处理多个条件区间的判断
2. 多分支语句通常由 if、elif 和 else 组成
3. 程序会从上到下依次判断条件，满足哪个条件就执行哪个分支
4. 当前分支执行后，后面的分支不会再继续判断
5. 编写多分支时，要注意条件顺序，通常先写范围更大的高条件或更严格的条件
"""

money = int(input('你的资产有多少万'))
print(f'有{money}万！')
if money >= 100000000:
    print('你是万亿富豪！！！！！')
elif money >= 10000000:
    print('你是千亿富豪！！！！')
elif money >= 1000000:
    print('你是百亿富豪！！！')
elif money >= 100000:
    print('你是十亿富豪！！')
elif money >= 10000:
    print('你是亿元富豪！')
elif money >= 1000:
    print('你是千万富豪')
elif money >= 100:
    print('你是百万富豪')
elif money >= 10:
    print('你是十万富豪')
elif money >= 1:
    print('你是万元富豪')
else:
    print('回家6馍去吧，孩儿')
