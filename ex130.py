#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 비트코인의 가격을 딕셔너리로 가져오는 코드이다.

변동폭 = float(btc['max_price']) - float(btc['min_price']) 
#변동폭이기 때문에 최근 24시간 내 최고 거래금액에서 최저 거래 금액을 뺀다.

시가 = float(btc['opening_price'])
#opening_price는 최근 24시간 내 시작한 거래금액이다.

최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:   #최고가가 시가+변동폭보다 작다면, 상승장을 출력한다.
    print("상승장")
else:                        #최고가가 시가+변동폭보다 크다면, 하락장을 출력한다.
    print("하락장")
#상승장

