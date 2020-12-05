#!/usr/bin/env python
# coding: utf-8

# In[4]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price)) 
#date와 close_price의 값을 각각 key와 value값으로 하는 딕셔너리로 바꾸어준다.
print(close_table)
#{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

