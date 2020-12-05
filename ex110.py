#!/usr/bin/env python
# coding: utf-8

# In[1]:


if True :              #첫번째 if문 Trie라는 조건 
    if False:          #True이기 때문에 1과 2가 출력되지 않는다.
        print("1")
        print("2")
    else:              #False의 반대이기 때문에 3이 작동되어 3이 출력된다.
        print("3")
else:                  #True라는 조건의 반대로 4는 출력되지 않는다.
    print("4")  
print("5")             #if문과는 상관없기 때문에 그냥 5가 출력된다.
#3
#5

