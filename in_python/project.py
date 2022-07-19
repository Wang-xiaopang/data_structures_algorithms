#1.编写一个程序,输出‘catdog’组成的所有可能的字符串，每个字母只能用一次
def 可能的字符串():
    a = 'catdog'
    for x in range(len(a)):
        for i in (a[0:x]+a[x+1:]):
            print(i[:x])

# 可能的字符串()


# 2.输入一个大于2的正整数,返回被2整除直到商小于2的次数
def 整除次数(a):
    c = 0
    while True:
        b = a // 2
        c +=1
        if b < 2:
            break
        
        a = b
    return c
# print(整除次数(9))

# 3.纸币硬币找钱系统
def 找钱(支付钱,给的钱):
    """设计元为1，有20，50，100，10，5，1，0.5，0.1"""
    找的钱 = 给的钱-支付钱
    钱币 = [100,50,20,10,5,1,0.5,0.1]
    a = []
    for i in 钱币:
        这个张树 = 找的钱 //i
        剩余钱数 = 找的钱-这个张树*i
        找的钱 = 剩余钱数
        a.append(这个张树)
    一百张数,五十张数,二十张数,十张数,五张数,一张数,五毛张数,一毛张数=a
    print(f'一百张数:{一百张数},五十张数:{五十张数},二十张数:{二十张数},十张数:{十张数},五张数:{五张数},一张数:{一张数},五毛张数:{五毛张数},一毛张数:{一毛张数}')

# 找钱(33.4,100)

# 4.做个计算器
def 计算器():
    while True:
        b = []
        a = input('请输入内容：数字后输入符号')
        try:
            a = int(a)
        except ValueError:
            if a == '+':
                a +=a
            elif a == '-':
                a -= a
            elif a == '*':
                a *= a
            elif a == '/':
                a /= a
            elif a == '=':
                print(a)
                break
            b.append(a)

# 计算器()

# 5.写I will never spam my friends again 写100次，对每个句子计数，有八次随机输入错误
from errno import WSAECONNREFUSED
import random
def 八次错误():
    wrong_times = 0
    str_ = 'I will never spam my friends again'
    for i in range(1,101):
        if i % 8 == 0:
            wrong_times +=1
            if wrong_times <= 8:
                print(f'第{i}次：{str_.join(random.sample(str_,3))}')
            else:
                print(f'第{i}次：{str_}')
        print(f'第{i}次：{str_}')
        

# 八次错误()

# 6.当n大于23，两个人生日相同的可能性大于50%
def 生日悖论(n):
    # 生日为365中的一天，可以表示range(364)反向唯一概率为365/365
    gailv = 1
    for i in range(n):
        唯一 =  (365-i)/365
        gailv *= 唯一
    print( 1-gailv)
# 生日悖论(22)


# 7.输入空格分隔的单词列表，输出列表每个单词的次数
#['abc' 'fsafsa' 'wraw' 'wrwarw' 'abc']
def 次数(list_):
    str_ = list_[0]
    review = []
    for i in range(str_.count(' ')+1):
        words = str_.split(' ',i+1)[i]
        if words not in review:
            print(words,str_.count(words))
        if str_.count(words) >1:
            review.append(words)

# 次数(['I I nevvv faf safsa featge wi will never spam my friends again my'])

        