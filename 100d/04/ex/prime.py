#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 输入一个数判断是否为素数。

import math

def is_prime(n):
  if n == 1:
    return False

  max = int(math.sqrt(n))
  for x in range(2, max + 1):
    if n % x == 0:
      return False

  return True

n = int(input('请输入一个正整数: '))
if is_prime(n):
  print('%d是素数' % n)
else:
  print('%d不是素数' % n)