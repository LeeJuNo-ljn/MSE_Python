#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


class Account:           #account의 클래스를 정의해준다.
    # class variable
    account_count = 0

    def __init__(self, name, balance):  #account의 객체가 생성될때 생성자를 정의해주었다.
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15   :  이자 지금
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:       #출금 금액을 출력한다.
            print(amount)                       #index를 나타내고 싶을때

    def deposit_history(self):
        for amount in self.deposit_log:        #입금 금액을 출력한다.
            print(amount)


k = Account("Kim", 1000)
k.deposit(100)                #100, 200, 300원 씩 빠져나감.
k.deposit(200)
k.deposit(300)
k.deposit_history()           #빠져나간 금액 기록을 출력해줌

k.withdraw(100)               #100, 200원 씩 입금됨
k.withdraw(200)
k.withdraw_history()          #들어온 금액 기록을 출력해줌
#100
#200
#300
#100
#200

