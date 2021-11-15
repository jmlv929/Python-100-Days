# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:12:37 2021

@author: 72721
"""


"""
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。

简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
"""

from random import randint

money=int(input("请输入你的初始钱数："))

while(money):
    request=input("您是否要继续 任意键/No：")
    if request.lower() == "no":
        break
    print("您现在的金额为%d" % money)
    debt=int(input("请下注："))
    print("第一次摇骰子中...")
    num=randint(1,6)+randint(1,6)
    print("第一次骰子:%d" % num)
    if(num==7 or num ==11):
        print("you win!")
        money=money+debt*2
    elif num==2 or num==3 or num==12:
        print("you lose")
        money=money-debt
    else:        
        while(True):
            print("摇骰子中...")
            num1=randint(1,6)+randint(1,6)
            print("骰子:%d" % num1)
            if num1 == 7:
                print("you lose")
                money=money-debt
                break
            if num1 == num:
                print("you win!")
                money=money+debt*2
                break
            else:
                print("",end="")
                
 print("你全输光了！！")