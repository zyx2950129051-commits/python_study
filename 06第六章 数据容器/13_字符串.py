"""第十三节，字符串"""

"""
字符串作为数据容器：
1. 有序、不可变、允许重复
2. 每个字符都有下标，支持正负索引和切片
3. 可以用 for 循环遍历每个字符
4. 常用方法：
   【查找】
   s.index(x, start, end)  查找 x 第一次出现的下标，找不到报错（start/end 可选）
   s.find(x, start, end)   同 index，找不到返回 -1 不报错
   s.count(x, start, end)  统计 x 出现的次数（start/end 可选）
   x in s                  判断子串 x 是否在 s 中，返回布尔值
   【修改（返回新字符串，原串不变）】
   s.replace(old, new)     将 old 替换为 new
   s.upper()               转大写
   s.lower()               转小写
   s.strip()               去掉两端空白（lstrip 去左端 / rstrip 去右端）
   【拆分与拼接】
   s.split(sep)            按 sep 切割，返回列表；可链式直接取元素：s.split(',')[1]
   sep.join(iterable)      把列表元素用 sep 拼接成字符串（split 的逆操作）
   【判断】
   s.startswith(x)         是否以 x 开头，返回布尔值
   s.endswith(x)           是否以 x 结尾，返回布尔值
   【其他】
   len(s)                  字符串长度
"""


# ── 1. 字符串的下标访问 ────────────────────────────────────────
s = 'Hello, Python!'

print('---------- 1. 下标访问 ----------')
print(s[0])       # H
print(s[-1])      # !
print(s[7:13])    # Python（切片，左闭右开）


# ── 2. index / count / len ────────────────────────────────────
print('---------- 2. index / count / len ----------')
print(s.index('P'))      # 7
print(s.count('l'))      # 2
print(len(s))            # 14


# ── 3. replace ────────────────────────────────────────────────
print('---------- 3. replace ----------')
s2 = s.replace('Python', 'World')
print(s2)    # Hello, World!
print(s)     # Hello, Python!（原字符串不变）


# ── 4. split ──────────────────────────────────────────────────
print('---------- 4. split ----------')
words = 'apple,banana,orange'
result = words.split(',')
print(result)           # ['apple', 'banana', 'orange']
print(result[1])        # 'banana'（对列表取下标）
print(words.split(',')[1])  # 'banana'（链式：split 返回列表，直接取下标，省掉中间变量）


# ── 5. strip ──────────────────────────────────────────────────
print('---------- 5. strip ----------')
s3 = '  hello world  '
print(s3.strip())     # 'hello world'（去两端空格）
print(s3.lstrip())    # 'hello world  '（去左端）
print(s3.rstrip())    # '  hello world'（去右端）


# ── 6. upper / lower ──────────────────────────────────────────
print('---------- 6. upper / lower ----------')
print('hello'.upper())    # HELLO
print('WORLD'.lower())    # world


# ── 7. startswith / endswith ──────────────────────────────────
print('---------- 7. startswith / endswith ----------')
filename = 'report_2024.pdf'
print(filename.endswith('.pdf'))      # True
print(filename.startswith('report'))  # True


# ── 8. find ───────────────────────────────────────────────────
print('---------- 8. find ----------')
s4 = 'hello world'
print(s4.find('o'))        # 4
print(s4.find('o', 5))     # 7（从下标5之后再找）
print(s4.find('xyz'))      # -1（找不到，不报错）
# print(s4.index('xyz'))   # ❌ 报错：找不到时 index 会抛出 ValueError


# ── 9. join ───────────────────────────────────────────────────
print('---------- 9. join ----------')
words = ['apple', 'banana', 'orange']
print(','.join(words))     # apple,banana,orange
print(' | '.join(words))   # apple | banana | orange
print(''.join(words))      # applebananaorange（无分隔符拼接）


# ── 10. in 运算符 ─────────────────────────────────────────────
print('---------- 10. in ----------')
s5 = 'Hello, Python!'
print('Python' in s5)      # True
print('Java' in s5)        # False
print('Java' not in s5)    # True


# ── 11. 遍历字符串 ────────────────────────────────────────────
print('---------- 11. 遍历 ----------')
for char in 'Python':
    print(char, end=' ')    # P y t h o n
print()


# ── 练习 ─────────────────────────────────────────────────────
# 准备字符串：sentence = 'the quick brown fox jumps over the lazy dog'
sentence = 'the quick brown fox jumps over the lazy dog'
# 1. 打印字符串长度
print(len(sentence))
# 2. 统计字母 'o' 出现的次数
print(sentence.count('o'))
# 3. 将字符串全部转为大写
print(sentence.upper())
# 4. 按空格切割，打印切割后的列表（得到每个单词）
print(sentence.split(' '))
# 5. 判断字符串是否以 'the' 开头
print(sentence.startswith('the'))