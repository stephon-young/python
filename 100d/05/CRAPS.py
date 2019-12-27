#!/usr/bin/python3
# -*- coding: utf-8 -*-

# CRAPS 赌博游戏:
# 说明：
#   CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
#   简单的规则是：
#       玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
#       其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
#       其他点数，玩家继续要骰子，直到分出胜负。
# 

import random

def CRAPS_game(init_money):
    all = init_money
    while all > 0:
        print('你的总资产为: %d' % all)
        while True:
            dept = int(input('请下注: '))
            if dept < 0 and dept > all:
                print('下注数非法')
            else:
                break

        first = random.randint(1, 6) + random.randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜')
            all += dept
        elif first == 2 or first == 3 or first == 11:
            print('庄家胜')
            all -= dept
        else:
            while True:
                next = random.randint(1, 6) + random.randint(1, 6)
                print('玩家摇出了%d点' % next)
                if next == 7:
                    print('庄家胜')
                    all -= dept
                    break
                if first == next:
                    print('玩家胜')
                    all += dept
                    break
    print('你破产了, 游戏结束!')

CRAPS_game(1000)