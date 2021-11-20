# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 23:39:46 2021

@author: 72721
"""

import random

def generate_code(code_length = 4):
    code_lib = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length_code_lib = len(code_lib) - 1
    my_code = ''
    for i in range(code_length):
        my_code += code_lib[random.randint(0,length_code_lib)] 
    return my_code

print(generate_code(code_length = 3))