# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:16:56 2021

@author: 72721
"""



a = int(input("请输入行数："))

for i in range(a):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(a):
    for j in range(a):
        if j < a - i -1:
            print(" ",end="")
        else:
            print("*",end="")
    print()
    
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()