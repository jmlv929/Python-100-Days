# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 16:31:42 2021

@author: 72721
"""
from random import sample,randint


def display(num):
    for i in range(num):
        balls = select_balls()
        for j in range(6):
            print(balls[j],end=" ")
        print(" " + str(balls[6]))

def select_balls():
    N = [x for x in range(1,34)]
    balls = sample(N,6)
    balls.append(randint(1,16))
    return balls


def main():
    N = int(input("请问您想投几注？"))
    display(N)

if __name__ == '__main__':
    main()
    