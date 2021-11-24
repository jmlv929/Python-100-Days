# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 10:30:04 2021

@author: 72721
"""
import time

class Clock:
    
    def __init__(self,hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def run_clock(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
                    
    def show_clock(self):
        return '%02d:%02d:%02d' % (self.hour,self.minute,self.second)
    
def main():

    clock = Clock(23,56,57)
    while True:
        print(clock.show_clock())
        clock.run_clock()
        time.sleep(1)
        
if __name__ == '__main__':
    main()
    
    
                    
            