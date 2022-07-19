"""
UML图
类：信用卡
域：_customer,_balance,_bank,_limit,_account
行为:get_customer() get_bank() get_account() make_payment(amount) get_balance() get_limit() charge(price)
"""
class CreatCard:
    """ 创建一张银行卡的信息"""
    def __init__(self,customer,limit,bank,account):
        """ 创建一个卡的实例
        customer：顾客的名字
        balance：默认为0
        limit：转账额度最大值
        bank：银行名称
        account：银行卡号
        """
        self._customer = customer
        self._limit = limit
        self._bank = bank
        self._account =account
        self._balance = 0
    def get_customer(self):
        """ 返回顾客的名字"""
        return self._customer

    def get_bank(self):
        """返回银行的名称"""
        return self._bank

    def get_account(self):
        """返回银行卡号"""
        return self._account

    def get_balance(self):
        """返回账户余额"""
        return self._balance

    def get_limit(self):
        """返回转账额度"""
        return self._limit
    def charge(self,price):
        """存钱"""
        self._balance += price
        return self._balance

    def make_payment(self,amount):
        """付钱"""
        limit_ = self.get_limit()
        balance_ = self.get_balance()
        if amount > limit_:
            print(f'大于限制转帐的最大额度{limit_}')
        if balance_ < amount:
            print(f'没钱了')
        else:
            self._balance = balance_-amount


if __name__ == '__main__':
    card_1 = CreatCard('wangjun_1',2000,'china bank','9264586')
    card_2 = CreatCard('wangjun_2',2000,'china bank','9264587')
    card_3 = CreatCard('wangjun_3',2000,'china bank','9264588')
    wallet = [card_1,card_2,card_3]
    for i in range(1,20):
        wallet[0].charge(i)
        wallet[1].charge(2*i)
        wallet[2].charge(3*i)

    for card in wallet:
        print(
        f'姓名是:{card.get_customer()}'
        f'银行是:{card.get_bank()}'
        f'卡号是:{card.get_account()}'
    )
        if card.get_balance() >100:
            card.make_payment(99)
            print(f'还剩{card.get_balance()}元钱')


