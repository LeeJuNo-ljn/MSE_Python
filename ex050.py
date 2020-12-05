#!/usr/bin/env python
# coding: utf-8

# In[5]:


data  = "    39490     "
data1 = data.rstrip()  #rstrip을 사용할 경우 오른쪽 공백만 지운다.
print(data1)           #오른쪽 공백이 지워진 '    39490'이 출력된다.
#    39490
data2 = data.lstrip()  #lstrip을 사용할 경우 왼쪽 공백만 지운다.
print(data2)           #왼쪽 공백이 지워진 '39490    '이 출력된다.
#39490

