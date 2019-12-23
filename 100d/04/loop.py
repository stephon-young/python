#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

# 循环: 分为for-in循环和while循环
#   1. for-in循环的应用场景:
#     - 明确的知道循环次数
#     - 对容器进行迭代。
#   2. while循环应用场景:
#     - 事先不知道循环次数的场景。
#  

# 求和，1~n
def sum(n):
  sum = 0
  # range()
  for x in range(n + 1):
    sum += x
  return sum

#print('sum(%d) = %d' % (10, sum(10)))

#  **重要**:
#   range()内置函数的使用:
#     - 函数返回一个序列
#     - 例如:
#       - range(101): 一个参数，返回[0~100]的序列
#       - range(1, 100): 两个参数，返回[1~99]的序列
#       - range(1, 100, 2): 三个参数，第三个参数是步长，即1,3,5,...
#     - 归纳一下:
#       - range(max): 上界为max(不包含)，下界默认为0(包含)，步长默认为1
#       - range(min, max): 上界为max(不包含)，下界为min(包含)，步长默认为1
#       - range(min, max, step): 上界为max(不包含)，下界为min(包含)，步长为step

# 偶数求和，1~n
def even_sum(n):
  sum = 0;
  for x in range(2, n + 1, 2):
    sum += x
  return sum

#print('even_sum(%d) = %d' % (100, even_sum(100)))

def guess_num():
  answer = random.randint(1, 100)
  counter = 0

  while True:
    number = int(input('请输入: '))
    counter += 1
    if number > answer:
      print('猜大了')
    elif number < answer:
      print('猜小了')
    else:
      print('恭喜你，猜对了')
      break
  print('你总共猜了%d次' % counter)
  if counter > 7:
    print('你的智商余额明显不足')

#guess_num()

def mul_table():
  for i in range(1, 10):
    for j in range(1, i + 1):
      print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

mul_table()