#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 输出100以内所有的素数。
#   说明：素数指的是只能被1和自身整除的正整数（不包括1）。
# 
#   解题思路: 从2开始整除，直到 n // 2 + 1
# 

def is_prime(x):
    if x <= 1:
        return False

    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False

    return True

def range_prime(n):
    ns = []
    for i in range(2, n + 1):
        if is_prime(i):
            ns.append(i)

    return ns

ns = range_prime(100)
print('100以内的素数: ', ns)