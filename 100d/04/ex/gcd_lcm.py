#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 求两个数的最大公约数，和最小公倍数。
# gcd: greatest common divosor
# lcm: lowerest common multiply

def gcd(x, y):
  if x > y:
    x, y = y, x

  for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
      return i
  
def lcm(x, y):
  if x > y:
    x, y = y, x
  
  for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
      return x * y // i

x = int(input('请输入第一个正整数: '))
y = int(input('请输入第二个正整数: '))

print('%d和%d的最大公约数为%d，最小公倍数为%d' % (x, y, gcd(x, y), lcm(x, y)))