#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 温度转换 华氏温度转换为摄氏温度, 转换公式:
#   C = (F - 32) / 1.8

def to_celsius(f):
  c = float(f - 32) / 1.8
  return c

f = float(input('请输入华氏温度: '))
c = to_celsius(f)
print('%.1f华氏度 = %.1f摄氏度' % (f, c))