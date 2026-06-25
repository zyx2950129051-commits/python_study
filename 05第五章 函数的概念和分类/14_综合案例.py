"""第十四节，综合案例：健身挑战赛"""

"""
需求：完成一个健身挑战赛程序
- 用户输入运动项目和挑战天数
- 每天录入完成数量
- 最终输出总数、平均值，判断是否挑战成功
"""


# ── 计算总数 ───────────────────────────────────────────────────
def calc_total(*counts):
    """计算所有天数的总数量"""
    total = 0
    for count in counts:
        total += count
    return total


# ── 计算平均值 ─────────────────────────────────────────────────
def calc_average(total, days, /):
    """根据总数和天数计算平均值（仅限位置参数）"""
    return total / days


# ── 判断是否挑战成功 ───────────────────────────────────────────
def is_success(average, /, goal=30):
    """平均值达到目标即为挑战成功，目标默认 30"""
    return average >= goal


# ── 打印总结报告（嵌套调用上面三个函数）──────────────────────
def print_summary(exercise, days, /, *counts):
    """打印健身总结，内部嵌套调用 calc_total、calc_average、is_success"""
    total = calc_total(*counts)
    average = calc_average(total, days)
    success = is_success(average)

    print(f'【{exercise}】【{days}天】健身总结')
    print(f'总数：{total}，平均值：{average:.1f}')
    if success:
        print('✅ 恭喜！挑战成功！')
    else:
        print('❌ 挑战失败，继续加油！')


# ── 主程序 ─────────────────────────────────────────────────────
exercise = input('请输入运动项目：')
days = int(input('请输入挑战天数：'))

print(f'【{exercise}】【{days}天】🥊 挑战赛（请输入每天的数量）')

counts = []
for i in range(1, days + 1):
    count = int(input(f'第{i}天：'))
    counts.append(count)

print_summary(exercise, days, *counts)