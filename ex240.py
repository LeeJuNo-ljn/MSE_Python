#!/usr/bin/env python
# coding: utf-8

# In[1]:


def 함수0(num) : 
    return num * 2            #num을 두배한다.

def 함수1(num) :
    return 함수0(num + 2)     #num에 2를 더하고 함수0으로 보낸다.

def 함수2(num) :        
    num = num + 10         #num 에 10을 더한다.
    return 함수1(num)      # 함수1으로 간다.

c = 함수2(2)               #num에 2를 대입한다.
print(c)
#28

