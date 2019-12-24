#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 打印三角形

def left_triple(line):
  for i in range(1, line + 1):
    print(i * '*')

def right_triple(line):
  for i in range(1, line + 1):
    print((line - i) * ' ' + (i * '*'))

def middle_triple(line):
  for i in range(1, line + 1):
    print((line - i) * ' ' + (2 * i - 1) * '*')

left_triple(5)
right_triple(5)
middle_triple(5)