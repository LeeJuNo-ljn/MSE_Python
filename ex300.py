#!/usr/bin/env python
# coding: utf-8

# In[3]:


per = ["가", "", "8.00"]

for i in per:
    try:              #코드를 실행한다.
        print(float(i))      #i가 실수일 때만 출력
    except:           #예외 발생시 실행.
        print(0)
    else:             #예외가 발생 안하면 실행.
        print("clean data") 
    finally:          #항상 실행.
        print("변환 완료")
#0
#변환 완료
#0
#변환 완료
#8.0
#clean data
#변환 완료

