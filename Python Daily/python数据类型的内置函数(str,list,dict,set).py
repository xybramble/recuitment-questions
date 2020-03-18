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

# 部分切片和完整切片的区别
I = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
I1 = I[:6]
print(id(I))
print(id(I1))
I2 = I[:]
print(id(I))
print(id(I2))
# 非字符串列表可用下标替换元素
I[3] = 666
print(I)
'''
output:
82357064
89342664
82357064
80656328
[1, 2, 3, 666, 5, 6, 7, 8, 9, 100]
'''

s = "i LOVE Python"
print(s.capitalize()) # 该函数将首字母大写，其余字母小写，返回字符串

s = "i love pYTHON" # 该函数将首字母大写，返回字符串
