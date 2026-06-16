"""第13节，学习字符串_转义字符"""

"""
1. 转义字符是在字符串中具有特殊作用的一类字符，通常以反斜杠开头
2. 当字符串中需要直接输出单引号、双引号或反斜杠时，可以使用转义字符
3. \n 表示换行，可以让一段字符串按多行形式输出
4. \\ 表示输出一个普通的反斜杠
5. \b 表示删除前一个字符，常用来演示退格效果
6. \r 表示让光标回到当前行的开头，后面的内容会覆盖前面的内容
7. \t 表示水平制表符，会让光标跳转到下一个制表位
8. \t 更适合演示制表效果，但中英文混合时视觉上可能出现对不齐的情况
9. 一个汉字在程序里通常算1个字符，但在终端中通常会占2个显示宽度
"""

# 使用\'输出'
print('在python中，可以使用\'包裹一个字符串')

#使用\"输出"
print("在python中，可以使用\"包裹一个字符串")

# 使用\n换行
print('注册会员需要以下信息：\n姓名\n年龄\n手机号')

# 使用\\输出一个\
print('C:\\Users\\你的用户名\\Desktop\\test.py')

# 使用\b删除前一个字符(做一些打字删除重写之类的效果)
print('helloo\b')

# 使用\r使光标回到本行开头，覆盖输出(做一些进度显示)
print('67%\r68%')

# 使用\t让光标跳转到下一个制表位，水平制表符(PyCharm一个制表位由四个位数组成）
print('123412341234')
print('a\tbcd')
print('ab\tcd')
print('abc\td')
print('abcd\ta')
print('我是\t中文')
# 如果想在所有环境让制表位统一组成标准，用.expandtabs(4)加在输出内容后
print('a\tbcd'.expandtabs(4))
print('ab\tcd'.expandtabs(4))
print('abc\td'.expandtabs(4))
print('abcd\ta'.expandtabs(4))
print('123456123456123456123456')
print('姓名12\t性别12\t年龄12\t'.expandtabs(6))
print('李五六\t男\t43\t'.expandtabs(6))
print('张三一\t女\t25\t'.expandtabs(6))
print('王五三\t男\t33\t'.expandtabs(6))
