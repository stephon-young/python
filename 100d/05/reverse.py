#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 将一个数字反转

def reverse(n):
    x = 0
    while n > 0:
        x = 10 * x + n % 10
        n = n // 10

    return x

n = int(input('请输入一个正整数: '))
print('%d反转后为: %d' % (n, reverse(n)))