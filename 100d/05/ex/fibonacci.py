#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 斐波那契数列:
#   下一数等于上两个数之和: 1 1 2 3 5 8 13 ...

def fibonacci(n):
    x = 0
    y = 1
    out = [1,]
    for i in range(1, n):
        z = x + y
        x = y
        y = z
        out.append(z)

    return out

n = int(input('请输入斐波那契数列个数: '))
out = fibonacci(n)
print('数列: ', out)