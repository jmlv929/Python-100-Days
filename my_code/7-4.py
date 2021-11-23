# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:32:52 2021

@author: 72721
"""



def find_max(mylist):
    m1 , m2 = mylist[0],mylist[1] if mylist[0] > mylist[1] else mylist[1] > mylist[0]
    for index in range(2,len(mylist)):
        if mylist[index] > m1:
            m1 , m2 = mylist[index] , m1
        elif mylist[index] > m2:
            m2 = mylist[index]
    return m1,m2

print(find_max([1,2,3,4,5,6,7,8,8]))