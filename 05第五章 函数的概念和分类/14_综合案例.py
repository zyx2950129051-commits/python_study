"""第十四节，综合案例：健身挑战赛"""

"""
需求：完成一个健身挑战赛程序
- 用户输入运动项目和挑战天数
- 每天录入完成数量
- 最终输出总数、平均值，判断是否挑战成功
"""

def calc_total(*exercise):
    """
    用来计算总运动量
    :param exercise:每天的运动量
    :return: 总运动量
    """
    return sum(exercise)

def calc_avg(total,days=7):
    """
    用来计算平均每天运动量
    :param total: 总运动量
    :param days: 运动天数
    :return: 平均运动量
    """
    return total / days

def check_success(total,goal=120):
    """
    判断挑战是否成功
    :param total:总运动量
    :param goal: 目标运动量
    :return: 成功为Ture,失败为False
    """
    if total > goal:
        return True
    else:return False

def main(sport):
    print(f'欢迎来到【{sport}】挑战赛，这次比赛持续7天')
    num1 = int(input('第一天：'))
    num2 = int(input('第二天：'))
    num3 = int(input('第三天：'))
    num4 = int(input('第四天：'))
    num5 = int(input('第五天：'))
    num6 = int(input('第六天：'))
    num7 = int(input('第七天：'))
    total = calc_total(num1,num2,num3,num4,num5,num6,num7)
    print('----------------------------------------------')
    print(f'您的总运动量是{total}')
    avg = calc_avg(total)

    print('----------------------------------------------')
    print(f'您的平均运动量是{avg:.2f}')

    result = check_success(total)
    print('----------------------------------------------')

    if result:
        print('恭喜您🎉挑战成功')
    else:
        print('很遗憾☹️挑战失败')

sport = input('请选择您的运动项目：')
main(sport)

