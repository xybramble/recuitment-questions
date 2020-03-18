# python数据类型：str（字符串）, list（列表）, dict（字典）, set（集合）

# 字符串连接操作
s1 = "i love"
s2 = "python"
s3 = s1 + s2
print(s3)
print(s1 + "" + s2)
'''
output:
i lovepython
i lovepython
'''

# 字符串的乘法
s = "i love python"
s2 = s * 10
print(s2)
'''
output:
i love python i love python i love python i love python i love python
i love python i love python i love python i love python i love python
'''

# 字符串当成列表
s = "i love python"
print(s[1])
print(s[-1])
'''
output:
i
n
'''

s = "123456"
print(s[2:6])
print(s[:])
'''
output:
3456
123456
'''

# 如果切片去一部分，则返回全新字符串
# 如果取完整切片，可能返回内容指向同一个字符串
s1 = s[:]
s2 = s[2:6]
print(s2)
print(id(s))
print(id(s1))
print(id(s2))
if s == s1:
    print("true")
if s == s2:
    print("true")
else:
    print("false")
'''
output:
love
89274192
89274192
89252656
true
fasle
'''

# 不能直接对字符串进行下标元素赋值，否则会导致错误
s1[1] = 'A'
print(s)
print(s1)
'''
TyprError: 'str' object does not support item assignment
'''

# 部分
