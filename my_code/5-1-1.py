# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 09:51:23 2021

@author: 72721
"""


#斐波那契数列的特点是数列的前两个数都是1，
#从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
#...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')