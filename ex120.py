#!/usr/bin/env python
# coding: utf-8

# In[2]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
# 좋아하는 과일을 딸기, 토마토, 사과라 하였을 때 fruit에 포함되어 있기 때문에 "정답이니다" 가 출력된다.
# 딸기, 토마토, 사과 외의 답을 입력하였을 때는 "오답입니다" 가 출력된다.

#좋아하는 과일은?딸기
#정답입니다.

#좋아하는 과일은?포도
#오답입니다.

