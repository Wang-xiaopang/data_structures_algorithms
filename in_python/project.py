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

# 找钱(1.3,150)

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

计算器()

