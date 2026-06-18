"""第6节，学习while循环案例"""

"""
1. while循环案例可以帮助理解“条件满足就重复执行”的实际用法
2. 在实际案例中，while常用于反复输入、反复判断和持续操作的场景
3. 本例中通过不断比较用户输入和正确答案，决定是否继续循环
4. 当用户输入正确答案时，条件不再成立，循环结束
5. 通过案例练习，可以更好地掌握while循环的执行过程和结束条件
"""

from random import gauss

print('-----系统提示：你现在身处一间密室中，答对问题才可逃出-----')
question = '你是谁的狗?'
answer  = '小周'
guess_answer = ''
while guess_answer != answer:
    print(f'{question}')
    guess_answer = input('请输入答案')
    if guess_answer == answer:
        print('恭喜您，答对了！')
    else:
        print('答案错误')
