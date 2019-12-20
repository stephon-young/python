#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 基本类型:
#   整型: python2 还有int与long区分，python3就没有了
#     - 0b 开头 二进制
#     - 0o 开头 八进制
#     - 0x 开头 十六进制
#   浮点型: 
#   字符串: 单引号、双引号都能表示字符串
#     - 原始字符串
#     - 字节字符串
#     - unicode字符串
#     - 多行形式，三个单/双引号开头，三个单/双引号结尾
#   布尔型: True/False
#   复数型: 和数学中区分为, 将i变为j了。
# 

def integer():
  a = 2
  b = 3
  print(a + b)
  print(a - b)
  print(a * b)
  print(a / b)  # 和c语言不同，这里不是整除，整除需要使用 //
  print(a % b)
  # 
  print(a // b)
  print(a ** b) # a的b次方

#integer()

# 2. 变量命名规则
#   字母(包括unicode字符，特殊字符除外)，数字，下划线组成，但是首字母不能是数字，
#   大小写敏感
#   建议:
#     - 不要和关键字重名，
#     - 不要和系统保留字重名。
#   PEP8规范命名规则:
#     - 用小写字符，多个单词用下划线连接
#     - 受保护的实例属性用一个下划线开头 ???
#     - 私有的实例属性用两个下划线开头  ???

# 3. 可以使用内置的type()函数返回变量的类型

def typed():
  a = 1
  b = 1.1
  c = 'string'
  d = True
  e = 1 + 2j
  '''返回值
  <class 'int'>
  <class 'float'>
  <class 'str'>
  <class 'bool'>
  <class 'complex'>
  '''
  print(type(a))
  print(type(b))
  print(type(c))
  print(type(d))
  print(type(e))

#typed()

# 5. 类型转换
#   - int() 可以将数值或者字符串转换为数字，可以指定进制。
#   - float() 可以将数值或者字符串转换为浮点数。
#   - str() 可以将对象转换为字符串，注意是对象。
#   - chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
#   - ord() 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
#       如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。

def int_cast():
  sa = '0x10'
  sb = '0b1111'
  sc = '0o17'
  sd = '12345'
  se = '123.5'
  e = 123.5

  print(int(sa, base=16)) # 需明确指定base，即进制数，
  print(int(sb, base=2))  # 需明确指定base，即进制数，
  print(int(sc, base=8))  # 需明确指定base，即进制数，
  print(int(sd))
  # 浮点数字符串无法转换为整数，报错
  #print(int(se))
  # 但是浮点数可以转换为整型，即截断操作。
  print(int(e))

def float_cast():
  sa = '123.5'
  sb = '123'
  sc = '0x123'
  sd = '1.2345e3'
  e = 123
  f = 1.23e1
  # 可以转换整型和浮点型字符串
  print(float(sa))
  print(float(sb))
  # 不能转换十六进制整数字符串。
  #print(float(sc))
  #科学计数法也支持
  print(float(sd))
  print(float(e))
  print(float(f))

def str_cast():
  a = 123
  b = 12.3
  c = 'aux string'
  d = (1, 2)
  e = {'a': 123, 'b': 111}

  print(str(a))
  print(str(b))
  print(str(c))
  print(str(d)) # 元组
  print(str(e)) # map

def chr_cast():
  a = 66

  print(chr(a))

def ord_cast():
  a = 'A'
  print(ord(a))

#int_cast()
#float_cast()
#str_cast()
#chr_cast()
#ord_cast()

# 6. 变量运算

def var_op():
  # input获取标准输入，作为字符串返回。
  a = int(input('a = '))
  b = int(input('b = '))

  # print的打印，可以使用占位符%<char>字符串，后面跟着一个百分号(%)，在后面跟一个元组，元组内容和字符串占位符对应。
  #   这时就会打印字符串，对应的占位符将自动替换为元组内的各个值。
  print('%d + %d = %d' % (a, b, a + b))
  print('%d - %d = %d' % (a, b, a - b))
  print('%d * %d = %d' % (a, b, a * b))
  print('%d / %d = %f' % (a, b, a / b))
  print('%d // %d = %d' % (a, b, a // b))
  print('%d %% %d = %d' % (a, b, a % b))
  print('%d ** %d = %d' % (a, b, a ** b))

#var_op()

# 7. 运算符优先级，这个没必要去记忆，如果不清楚，可以用括号。
#   - 需要注意有几个运算符比较特殊，c/c++没有的
#     - 切片: [:]
#     - 按位取反: ~
#     - 指数: **
#     - 整除: //
#     - 身份运算符: is, is not
#     - 成员运算符: in, not in
#     - 逻辑运算符: and or not
#     - 组合运算符: +=, -=, *=, /=, //=, **=, ^=, &=, >>=, <<=等。需要注意的是: //=, **=, ^=
# 

def operator():
  a = 10
  b = 3
  a += b # a = a + b 注意python中没有自增与自减运算符。
  a *= a +2 # a = a * (a + 2) 注意这个的优先级
  print(a)

#operator()

def operator2():
  flag0 = 1 == 1
  flag1 = 3 > 2
  flag2 = 2 < 1
  flag3 = flag1 and flag2
  flag4 = flag1 or flag2
  flag5 = not (1 != 2)
  print('flag0 = ', flag0)
  print('flag1 = ', flag1)
  print('flag2 = ', flag2)
  print('flag3 = ', flag3)
  print('flag4 = ', flag4)
  print('flag5 = ', flag5)
  print(flag1 is True)
  print(flag2 is not False)

operator2()