#!/usr/bin/env python
# coding: utf-8

# In[3]:


def message1():    #
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) : # i가 1, 2, 3일 때 for문이 반복되기 된다.
        message2()       #i가 범위안에 있을때 B를 출력한다.
        print("C")       #C를 출력한다.
    message1()           #for문이 끝나고 나왔을 때 A를 출력한다.

message3()   
#B
#C
#B
#C
#B
#c
#A

