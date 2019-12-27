#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 寻找水仙花数:
#   水仙花数定义: 三位数，每位数的立方和等于他自身。
#   153 = 1^3 + 5^3 + 3^3
#

def narcissus():
    for i in range(100, 1000):
        a = i // 100
        b = (i % 100) // 10
        c = i % 10
        if a ** 3 + b ** 3 + c ** 3 == i:
            print('%d 是水仙花数，a=%d,b=%d,c=%d' % (i, a, b, c))
    
narcissus()