"""
综合案例：答题闯关挑战赛

游戏规则：

1. 一共3个关卡（每个关卡只有一道题）
   - 答对进入下一关
   - 3关全部通过则挑战成功

2. 答错可重试
   - 每道题有3次回答机会
   - 若3次均答错，则挑战失败
   - 游戏自动结束

3. 如果用户输入为空
   - 提示重新作答
   - 不浪费回答机会

4. 如果用户输入字母 q
   - 直接退出游戏
"""

'''
下面是原来的代码，先保留：

print('欢迎来到答题挑战赛！')
question1 = '你牛逼吗'
answer1 = 'yes'

question2 = '比我牛逼吗？'
answer2 = 'no'

question3 = '叫爸爸'
answer3 = '爸爸'

# 答题机会
max_chance = 3
# 关卡
max_level = 3
# 游戏状态
game_over = False

for level in range(1, max_level + 1):
    if game_over == True:
         break
    user_tries = 1
    if level == 1:
        print(f'请听第一题,{question1}')
        while user_tries <= max_chance:
            user_answer = input('输入你的答案：(yes/no)')
            if user_answer == answer1:
                print('恭喜您回答正确✅')
                break
            elif user_answer == '':
                print('您输入的是空，请重新输入')
                continue
            elif user_answer == 'q':
                game_over = True
                break
            else:
                print('回答错误❌')
                user_tries += 1
                if max_chance - user_tries < 0:
                    print('您出局了')
                    game_over = True
                    break
                print(f'您还剩{max_chance - user_tries + 1}次机会')

    if level == 2:
        print(f'请听第二题,{question2}')
        while user_tries <= max_chance:
            user_answer = input('请输入你的答案:(yes/no)')
            if user_answer == answer2:
                print('恭喜您回答正确✅')
                break
            elif user_answer == '':
                print('您输入的是空，请重新输入：')
                continue
            elif user_answer == 'q':
                game_over = True
                break
            else:
                print('回答错误❌')
                user_tries += 1
                if max_chance - user_tries < 0:
                    print('您出局了')
                    game_over = True
                    break
                else:
                    print(f'您还剩{max_chance - user_tries + 1}次机会')
    if level == 3:
        print(f'请听第三题,{question3}')
        while user_tries <= max_chance:
            user_answer = input('请输入你的答案:')
            if user_answer == answer3:
                print('好儿子，恭喜你三道题全部答对了✅')
                break
            elif user_answer == '':
                print('您输入的是空，请重新输入：')
                continue
            elif user_answer == 'q':
                game_over = True
                break
            else:
                print('回答错误❌')
                user_tries += 1
                if max_chance - user_tries < 0:
                    print('您出局了')
                    game_over = True
                    break
                else:
                    print(f'您还剩{max_chance - user_tries + 1}次机会')
'''

print('欢迎来到答题挑战赛！')

questions = [
    ('你牛逼吗', 'yes'),
    ('比我牛逼吗？', 'no'),
    ('叫爸爸', '爸爸')
]

max_chance = 3
game_over = False

for level in range(len(questions)):
    question, answer = questions[level]
    print(f'请听第{level + 1}题：{question}')

    user_tries = 1
    while user_tries <= max_chance:
        if level == 0:
            user_answer = input('输入你的答案：(yes/no)')
        elif level == 1:
            user_answer = input('请输入你的答案:(yes/no)')
        else:
            user_answer = input('请输入你的答案:')

        if user_answer == 'q':
            print('游戏已退出')
            game_over = True
            break
        elif user_answer == '':
            print('您输入的是空，请重新输入')
            continue
        elif user_answer == answer:
            if level == len(questions) - 1:
                print('好儿子，恭喜你三道题全部答对了✅')
            else:
                print('恭喜您回答正确✅')
            break
        else:
            print('回答错误❌')
            user_tries += 1
            if user_tries > max_chance:
                print('您出局了')
                game_over = True
                break
            print(f'您还剩{max_chance - user_tries + 1}次机会')

    if game_over:
        break
