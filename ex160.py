#!/usr/bin/env python
# coding: utf-8

# In[6]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
  split = i.split(".")  #.을 기준으로 나눈다
  if (split[1] == "h") or (split[1] == "c"):#.뒤에 h 와 c가 오는 경우만 출력한다.
    print(i)
#intra.h
#intra.c
#define.h

