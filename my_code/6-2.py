# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:11:06 2021

@author: 72721
"""


#实现判断一个数是不是回文数的函数

def palindrome(num):
    reversed_num = 0
    temp = num
    while(num):
        reversed_num = reversed_num*10 + num%10
        num//=10
    if reversed_num == temp:
        return "这个数是一个回文数"
    else:
        return "这个数不是一个回文数"

print(palindrome(1239321))

#Python中，用 def 语句创建函数时，可以用 return 语句指定应该返回的值，
#该返回值可以是任意类型。需要注意的是，return 语句在同一函数中可以出现多次，
#但只要有一个得到执行，就会直接结束函数的执行。