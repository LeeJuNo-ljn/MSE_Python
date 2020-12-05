#!/usr/bin/env python
# coding: utf-8

# In[7]:


ohIc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
total_profit = 0
for day_price in ohlc[1:]:                 #day_price가 ohIc에 속해있다.
    profit = (day_price[3] - day_price[0]) #(100-100) , (190-200) , (310-300)  
    total_profit += profit                 #(100-100) + (190-200) + (310-300) = 0
print(total_profit)
#0

