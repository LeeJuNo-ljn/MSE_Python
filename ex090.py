#!/usr/bin/env python
# coding: utf-8

# In[3]:


icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500,'메로나': 1000}
icecream['누가바']  #위의 딕셔너리에 '누가바'가 없기 때문에 오류가 발생한다.
#---------------------------------------------------------------------------
#KeyError                                  Traceback (most recent call last)
#<ipython-input-3-34bc19e86151> in <module>
#      1 icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500,'메로나': 1000}
#----> 2 icecream['누가바']  #위의 딕셔너리에 '누가바'가 없기 때문에 오류가 발생한다.
#
#KeyError: '누가바'


# In[7]:


icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500,'메로나': 1000, '누가바': 800}
icecream['누가바']   #위의 딕셔너리에 '누가바'가 생겼기 때문에 누가바의 value값이 출력된다.
#800

