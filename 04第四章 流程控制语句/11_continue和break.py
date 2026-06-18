"""第11节，学习continue和break"""

"""
1. continue和break都是循环中的流程控制语句
2. continue用于结束本次循环，直接进入下一次循环
3. break用于立即结束整个当前循环，不再继续执行后续循环
4. 这两个语句常用于在循环中根据条件跳过部分内容或提前终止循环
5. 使用continue和break可以让循环控制更加灵活
"""

for day in '一二三四五六日':
    print(f'今天是周{day}，我要',end = '')
    print('吃饭',end = '')
    print('睡觉',end = '')
    if day == '二'or day == '四'or day == '六':
        print()
        continue
    print('打豆豆')

for date in range (1,11):
    print(f'--------今天是第{date}天--------')
    print('吃饭')
    for food_num in range (1,4):
        print(f'面包{food_num}')
        if date in [2,9,5] and food_num == 2:
            break
        print(f'牛奶{food_num}')
    print('睡觉')
