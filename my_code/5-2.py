# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:55:57 2021

@author: 72721
"""


#公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

a=0 #公鸡
b=0 #母鸡
c=0 #小鸡

for a in range(0,100//3+1):
    for b in range(0,100//1+1):
        for c in range(0,300+1):
            if (a+b+c==100) and (5*a+3*b+c*1/3==100) and (c%3==0):
                print("公鸡有%d个,母鸡有%d个，小鸡有%d个" % (a,b,c))