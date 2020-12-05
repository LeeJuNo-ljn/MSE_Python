#!/usr/bin/env python
# coding: utf-8

# In[3]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])  #high_prices와 low_prices에 있는 같은 자리에 위치한 원소끼리 뺀다.
print(volatility)   #변동폭이 volatility에 저장된다.
#[50, 100, 30, 80, 0]

