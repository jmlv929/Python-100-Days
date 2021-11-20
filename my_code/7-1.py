# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 23:26:00 2021

@author: 72721
"""


import time

content = '北京欢迎你，为你开天辟地......'
while True:
    print(content)
    time.sleep(1)
    content = content[1:] + content[0]
