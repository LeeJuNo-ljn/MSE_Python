#!/usr/bin/env python
# coding: utf-8

# In[1]:


apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:           #row가 apart에 속해 있다.
    for col in row:         #col이 row에 속해 있다. 즉 col은 apart에 속해 있다. 
        print(col, "호")     #col의 값과 호를 같이 출력한다.
print("-" * 5)              #마지막에 -----를 출력한다.
#101 호
#102 호
#201 호
#202 호
#301 호
#302 호
#-----

