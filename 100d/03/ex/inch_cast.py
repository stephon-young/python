#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 英寸和厘米转换:
#   1英寸 = 2.54 厘米

def cast():
  size = float(input('请输入长度: '))
  unit = input('请输入单位: ')
  if unit == 'in' or unit == '英寸':
    print('%.2f英寸 = %.2f厘米' % (size, size * 2.54))
  elif unit == 'cm' or unit == '厘米':
    print('%.2f厘米 = %.2f英寸' % (size, size / 2.54))
  else:
    print('不支持的单位: %s' % (unit))

cast()
