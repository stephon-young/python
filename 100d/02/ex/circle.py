#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 计算圆周长和面积

import math

radius = float(input('请输入圆半径: '))
area = math.pi * (radius ** 2)
perimeter = 2 * math.pi * radius

print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
