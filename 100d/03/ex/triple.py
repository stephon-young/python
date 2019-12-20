#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 输入三条边，看能否组成三角形，如果能，则计算周长和面积。
#   - 面积公式: s = 平方根(p * (p - a) * (p - b) * (p - c)), 其中p是三角形周长的一半，这个公式称为: 海伦公式

def triple(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    l = a + b + c
    p = l / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('周长: %.2f， 面积: %.2f' % (l, s))
  else:
    print('不能构成三角形')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
triple(a, b, c)