"""第8节，学习for循环案例"""

"""
1. for循环案例能够帮助理解遍历操作在实际问题中的应用
2. 本例通过遍历字符串中的每个字符，逐个完成加密和解密处理
3. 在循环中，可以对每个元素进行相同规则的加工后再重新拼接
4. for循环非常适合处理文本、列表等需要逐项操作的数据
5. 通过案例练习，可以掌握for循环与字符串处理的配合用法
"""

# 需要加密的内容
text = input('需要加密的内容')

# 加密过的内容
secret = ''

for n in text:       # 将原文逐个输入
    code = ord(n)    # 将原文文字加密为code
    secret += chr(code + 5) # 将加密过的每个字连起来赋给secret加密文件
print(f'加密后的内容为{secret}')


secret2 = input('需要解密的内容')

text2 = ''
for m in secret2:
    text2 += chr(ord(m) - 5)
print(f'解密后的内容为{text2}')
