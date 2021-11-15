# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 19:54:42 2021

@author: 72721
"""


a=int(input("请输入第一个正整数："))
b=int(input("请输入第二个正整数："))

if a > b:
    c = a
    a = b
    b = c

#最大公约数
for i in range(a,0,-1):
    if a % i == 0 and b % i == 0:
        max_gongyueshu = i
        break
    else:
        max_gongyueshu = 0
        
#最小公倍数
for i in range(b,a*b+1):
    if i % a == 0 and i % b == 0:
        min_gongbeishu = i
        break
    else:
        min_gongbeishu = 0



print("最大公约数为：%d" % max_gongyueshu)
print("最小公倍数为：%d" % min_gongbeishu)
