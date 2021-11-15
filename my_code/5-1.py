# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:38:10 2021

@author: 72721
"""


"""水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，
例如：$1^3 + 5^3+ 3^3=153$。
"""

""" 寻找水仙花数 """

print("水仙花数：")
for i in range(100,1000):
    if (i%100%10)**3 + ((int(i/100))**3) + (int(i/10)%10)**3 == i:
        print(i)
        
        
        
#        //	取整除 - 返回商的整数部分（向下取整）
""" low = num % 10
    mid = num // 10 % 10
    high = num // 100
"""

"""反转数字"""

print("---------反转数字----------")

num = int(input("请输入要反转的整数："))

reversed_num=0
while num:
    reversed_num = reversed_num * 10 + num % 10
    num //=10
print(reversed_num)