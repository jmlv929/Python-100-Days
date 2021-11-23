# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:01:12 2021

@author: 72721
"""





def is_leap_year(year):
    """判断年份是不是闰年"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year,month,day):
    days = 0
    if is_leap_year(year):
        days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(month-1):
        days += days_of_month[i]
    days += day
    return days

def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))
    
if __name__ == '__main__':
    main()