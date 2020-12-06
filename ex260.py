#!/usr/bin/env python
# coding: utf-8

# In[11]:


class OMG :
    def print() :
        print("Oh my god")


mystock = OMG()
mystock.print() #OMG.print(mystock)으로 호출이됨 즉 argument가 없는데 주어진다. = 에러의 원인이 됨.
#---------------------------------------------------------------------------
#TypeError                                 Traceback (most recent call last)
#<ipython-input-8-e5fe01e3b331> in <module>
#      5 
#      6 mystock = OMG()
#----> 7 mystock.print()
#
#TypeError: print() takes 0 positional arguments but 1 was given

