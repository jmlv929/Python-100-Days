# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 11:03:51 2021

@author: 72721
"""
import math

"""
区分加不加 类 中加不加self 的区别

"""

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def move(self,dx,dy):       #x之前加的x ，x是类中共享的 ，dx , dy不用加 self  
        self.x += dx
        self.y += dy
    
    def calculate_distance(self,x1,y1):
        return math.sqrt(math.pow(x1-self.x,2) + math.pow(y1-self.y,2))
                                          #加 self算 类中 的属性
    
    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))
        
        
def main():
    point = Point(1,2)
    point.move(2,3)
    print(point)
    print(point.calculate_distance(3,5))
    
if __name__ =='__main__':
    main()