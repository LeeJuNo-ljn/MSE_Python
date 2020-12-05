#!/usr/bin/env python
# coding: utf-8

# In[10]:


def print_max(a, b, c) :
    max_val = 0           
    if a > max_val :      
        max_val = a         # a b c 중 a가 가장 클때 a 출력
    if b > max_val :     
        max_val = b         # a b c 중 b가 가장 클때 b 출력
    if c > max_val :
        max_val = c         # a b c 중 c가 가장 클때 c 출력
    print(max_val)
    
print_max(150, 100, 30)       # a b c 자리에 임의의 수 150 100 30 대입시 가장 큰 값 150이 출력됨
#150

