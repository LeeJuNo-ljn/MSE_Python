#!/usr/bin/env python
# coding: utf-8

# In[36]:


class stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per  = per
        self.pbr  = pbr
        self.배당수익률 = 배당수익률
# stock클래스를 정의하고 stock클래스의 객체가 생성될 때 생성자(name, code, per, pbr 배당수익률)를 정의하였다.

종목 = []

삼성 = stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = stock("LG전자", "066570", 317.34, 0.69, 1.37)
# 삼성, 현대차, LG전자 각각의 생성자 값을 정해주었다.

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)
#종목에 삼성, 현대차, LG전자 값을 넣어주었다.

for i in 종목:
    print(i.code, i.per)
#005930 15.79
#005380 8.7
#066570 317.34

