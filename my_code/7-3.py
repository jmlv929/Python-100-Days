# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:19:15 2021

@author: 72721
"""

def get_houzhui(filename):
    index = filename.rfind('.')
    if  0 < index < len(filename) - 1:
        return filename[index:]
    else:
        return ''
    
print(get_houzhui('1.txt'))
    