#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 判断是否为闰年

def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  return False

year = int(input('请输入年份: '))
# python不支持 二元运算符 (?:)
# val = (is_leap_year(year) == 1) ? '是' : '否'
# print('%d 是否为闰年: %s' % (year, val))
print('%d 是否为闰年: %d' % (year, is_leap_year(year)))

