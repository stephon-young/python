#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 函数的定义与使用:
#   def <function name>(<arg list>):
#       <function body>
#       [return [value]]
# 由于python函数
#   1. 支持默认值，
#   2. 并且支持指定函数参数名称的赋值，所以不需要重载。
#       当函数使用指定参数名的方式的时候，参数赋值与位置无关。
#
#   3. 可变参数: <*arg>的参数形式，支持零个参数的调用。
#       如: def add(*arg)
#       访问方式: for a in arg:
#   4. 注意:
#       1. 最简单的场景就是在同一个.py文件中定义了两个同名函数，会是什么结果呢？
#       由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，也就意味着两个函数同名函数实际上只有一个是存在的。
#       项目中需要避免这种情况
#
#       2. 如果项目是由多人协作进行团队开发的时候，团队中可能有多个程序员都定义了名为foo的函数，那么怎么解决这种命名冲突呢？
#       答案其实很简单，Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候
#       我们通过import关键字导入指定的模块就可以区分到底要使用的是哪个模块中的foo函数，代码如下所示。
#       
#       module1.py
#       def foo():
#           print('hello, world!')
#
#       module2.py
#       def foo():
#           print('goodbye, world!')
#
#       test.py
#       from module1 import foo
#       # 输出hello, world!
#       foo()
#       from module2 import foo
#       # 输出goodbye, world!
#       foo()
#
#       也可以通过别名的方式引用
#
#       test.py
#       import module1 as m1
#       import module2 as m2
#       m1.foo()
#       m2.foo()
#
#       这样的方式将会存在覆盖
# 
#       test.py
#       from module1 import foo
#       from module2 import foo
#       # 输出goodbye, world! 后者覆盖前者，如果上面的反过来，则输出的是module1的foo()
#       foo()
#       

from random import randint

def roll_dice(n=2):
    '''
    添加函数注释，会以文档的方式提示用户。
    '''
    result = 0
    # i 变量不在后续引用可以用下划线代替: _
    for i in range(1, n + 1):
        result += randint(1, 6)
    
    # 上面的等价于下面的，倾向于下面的写法:
    #for _ in range(n):
    #    result += randint(1, 6)

    return result

def add(a=0,b=0,c=0):
    return a + b + c

def add_ex(*arg):
    sum = 0
    for i in arg:
        sum += i
    return sum

def test():
    # 无参数: 将使用默认值2
    print(roll_dice())
    # 有参数: 
    print(roll_dice(3))

    # 无参数
    print(add())
    # 1个参数，自行匹配到a,跟位置相关
    print(add(1))
    # 2个参数，自行匹配到a,b,跟位置相关
    print(add(1, 2))
    # 3个参数，自行匹配到a,b,c,跟位置相关
    print(add(1,2,3))

    # 位置无关参数，即参数名匹配方式:
    print(add(c=1,b=2,a=3))
    print(add(c=3))

    # 注意可变参数支持0个参数。
    print(add_ex())
    print(add_ex(1))
    print(add_ex(1, 2))
    print(add_ex(1, 2, 3, 4, 5, 6, 7))

test()