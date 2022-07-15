# 1.编写一个Python函数is_multiple(n,m)，用来接收两个整数值n和m,如果n是m的倍数，即存在整数i，使得n=mi，那么函数返回True，否则返回False。

from random import randrange


def is_multiple(n, m):
    return (True if n % m == 0 else False)

# print(is_multiple(6,3)) # True
# print(is_multiple(4,3)) # False


# 2.编写一个Python函数is_even(k)，用来接收一个整数k,如果k是偶数返回True，否则返回False。但是不能用乘法、除法或者取余操作
# UP:可以更好用来判断奇数偶数
# 0，1，10，11，100，101，110，111，所以偶数最后一位都是0,奇数都是1，所以0&1等于0

def is_even(k):
    return (True if (k & 1) == 0 else False)
# print(is_even(0),is_even(1),is_even(2),is_even(100)) # True False True True


# 3.编写一个Python函数minmax(data)，用来在数的序列中找出最小数和最大数，并以一个长度为2的元组形式返回，不能用min和max。

def minmax(data):
    a = b = data[0]
    for i in data:
        if i > a:
            max = a = i
        else:
            max = a
        if i > b:
            min = b
        else:
            min = b = i
    return min, max
# print(minmax([1,2,3,0,5,99,7,6,4]))


# 4.编写一个python函数，用来接收正整数n，返回1-n的平方和，不用sum

def pingfang(n):
    a = 0
    for n in range(n+1):
        a += n*n
    return a

# print(pingfang(5))


# 5.基于Python的解析语法和内置函数sum，写一个单独的命令来计算第四题的和

def pingfang_sum(n):
    return sum(n*n for n in range(n+1))

# print(pingfang_sum(5))


# 6.编写一个Python函数,用来接收正整数n，并返回1-n所有奇数的平方和

def jishuhe(n):
    a = 0
    for i in range(n+1):
        if (i & 1) == 1:
            a += i*i
    return a

# print(jishuhe(5))


# 7.用sum写第6题

def jishuhe_sum(n):
    return sum(i*i for i in range(n+1) if (i & 1) == 1)

# print(jishuhe_sum(5))

# 8.一个长度n的字符串s，当索引-n≤k＜0时，元素为s[k]，求一个正整数索引j≥0，s[j] == s[k]


def get_j(s, k):
    j = len(s) + k
    return j

# print(get_j('asagsag',-7))

# 9.用range构造一个值为50，60，70，80的排列


def creat_list():
    return [i for i in range(50, 81, 10)]

# print(creat_list())

# 10.用range构造一个值为8,6,4,2...-8的排列


def creat_fuer():
    return [i for i in range(8, -9, -2)]
# print(creat_fuer())

# 11.用python列表解析语法来产生[1,2,4,8,16,32,64,128,256]


def erdebeishu():
    return [2**i for i in range(9)]


# print(erdebeishu())


# 12.用Random的randrange函数，从非空序列，返回一个随机数


def get_choice(data):
    while True:
        a = randrange(min(data), max(data)+1)
        if a in data:
            return a

# print(get_choice([1, 23, 5352, 87, 23, 2]))
