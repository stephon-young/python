#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 分支结构: if.
#   - 关键字: if, else, elif(这个关键字，是类c语言没有的)

# 例子:
#   1. 用户名、密码验证
def valid():
  username = input('请输入用户名: ')
  password = input('请输入密码: ')
  if username == 'admin' and password == '12345':
    print('身份验证成功')
  else:
    print('身份验证失败')

#valid()

#   2. f(x)
#             3x - 5  (x > 1)
#     f(x) =  x + 2   (-1 <= x <= 1)
#             5x + 3  (x < -1)
#

def f(x):
  if x > 1:
    return 3 * x - 5
  elif x >= -1 and x <= 1:
    return x + 2
  else:
    return 5 * x + 3

def fx():
  x = float(input('x = '))
  print('f(%.2f) = %.2f' % (x, f(x)))

#fx()

# 3. 嵌套分支版本 f(x)

def f2(x):
  if x > 1:
    return 3 * x - 5
  else:
    if x >= -1:
      return x + 2
    else:
      return 5 * x + 3

def fx2():
  x = float(input('x = '))
  print('f(%.2f) = %.2f' % (x, f2(x)))

fx2()