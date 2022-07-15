# 1.编写一个函数的伪代码描述，该函数用来逆置n个整数的列表，使这些数以相反的顺序输出，并将该方法与可以实现相同功能的python函数比较
def 逆置整数列表(data):
    return [data[-1-i] for i in range(len(data))]


def 逆置整数列表_0(data):
    return data[::-1]
# data = [1,2,3,51,2132,15,12341,521]
# print(逆置整数列表(data))
# print(逆置整数列表_0(data))
# data.reverse
# print(data)


# 2.编写一个python函数，用来接收一个整数序列，并判断该序列是否存在一对乘积是奇数的互不相同的数

def 返回乘积不同数(data):
    a = []
    for i in data:
        for j in data:
            if i != j:
                if i*j & 1 == 1:
                    a.append((i, j))
    if len(a):
        return True
    else:
        return False


# print(返回乘积不同数([2, 4, 1, 5, 10]))
# print(返回乘积不同数([2, 4, 6, 8, 10]))


# 3.编写一个python函数，用来接收一个数字序列，并判断是否所有数字都互不相同
def 返回是否不同(data):
    a = []
    for i in range(len(data)-1):
        for j in data[i+1:]:
            if i == j:
                a.append((i,j))
    if len(a):
        return False
    else:
        return True
# print(返回是否不同([1,2,3.5,6.4,2,5.5]))
# print(返回是否不同([1,2,3.5,6.4,5.5]))

# 4. 用列表解析语法来产生列表[0,2,6,12,20,30,42,56,72,90]
def 返回指定表():
    return [i*(i+1) for i in range(10)]

# print(返回指定表())

# 5.用列表解析法，不输入英文字母的情况下产生列表['a','b'....'z']
def 返回字母():
    return [chr(i) for i in range(97,123)]

# print(返回字母())

# 6. 用randint写一个对列表打乱排序类似shuffle的函数
from random import randint
def 打乱排序(data):
    b = []
    while 1:
        a = data[randint(0,len(data)-1)]
        if a not in b:
            b.append(a)
        if len(data) == len(b):
            break
    return b
# print(打乱排序([1,2,3,4]))


# 7.反复从标准输入读取一行到EOFError，然后以相反的顺序输出这些行，用户可以按ctrl+d 结束， sys.stdin
import sys
def 反向返回标准输入():
    inp = sys.stdin
    mess = inp.read()
    print(mess[::-1])

# 反向返回标准输入()

# 8.编写一个python，接收长度为n的两个整型数组a，b返回a和b的点积，即返回一个长度为n的数组c，c[i] = a[i].b[i]
def 返回点积(a,b):
    return [a[i]* b[i] for i in range(len(a))]
# print(返回点积([1,2,3,4,5],[6,7,8,9,9]))

# 9.超出索引提升 "Dont't try buffer overflow attacks in Python!"
def 超出索引(a):
    try:
        for i in range(len(a)+1):
            a[i] *1
    except IndexError:
        print("Dont't try buffer overflow attacks in Python!")
# 超出索引('fsafsaf')

# 10.计算字符串中元音字母个数
def 计算元音(a):
    z = 0
    for i in a:
        if i in ['a','e','i','o','u']:
            z +=1
    return z
# print(计算元音('safagfqfwqfwqf'))
# print(计算元音('wwwwwwwwwwwwww'))

# 11.删除字符串的符号
def 删除符号(a):
    c= ''
    for i in a:
        if i in ([chr(c) for c in range(97,123)] + [chr(c) for c in range(65,91)]+[chr(32)]):
            c += i
    return(c)
    
# print(删除符号("Let's try, Mike."))

# 12.输入a,b,c，判断a+b=c a=b-c a*b= c 是否有一个成立
def 条件判断():
    a,b,c = int(input()),int(input()),int(input())
    if a+b==c or a==b-c or a*b ==c:
        return True
    else:
        return False
# print(条件判断())

# 13.产生递增的生成器
"""
返回1
100
2
50
4
25
5
20
10

"""
def factor(n):
    k = 1
    while k * k <n:
        if n % k == 0:
            yield k
            yield n//k
            
        k +=1
    if k * k ==n:
        yield k


# for i in factor(100):
#     print(i)

# 14.||v|| = 根号p（v1^p+v2^P....vn^p）
def novm(v,p):
    a=0
    for k in v:
        a +=k **p
    c = a ** (1/p)
    return c

print(novm([3,4],2))
        