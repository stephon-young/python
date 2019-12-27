#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 找出10000以内的完美数。
#   说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
#   例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
#   
#   解题思路: 从1开始，求取其真因子，然后相加，如果等于自身就是完美数。
#       1 -> n // 2
#

def is_perfect(n):
    if n <= 1:
        return False

    sum = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum += i

    if sum != n:
        return False

    return True

def range_perfect(r):
    ns = []
    for i in range(2, r + 1):
        if is_perfect(i):
            ns.append(i)

    return ns

ns = range_perfect(10000)
print('10000以内的完美数: ', ns)

    
    