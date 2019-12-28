#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 作用域: 
#   1. 分类: 全局作用域、局部作用域、嵌套作用域、内置作用域
#   2. 查找规则: 先局部作用域，后嵌套作用域，再全局作用域，最后内置作用域。
#   3. 穿透:
#       1. 可以在局部作用域中，访问全局作用域的变量，通过使用global关键字实现。
#       2. 可以在局部作用域中，访问嵌套作用域的变量，通过使用nonlocal关键字实现。
#       x. 可以通过上面的方式在局部作用域修改全局作用域变量，或者在嵌套作用域修改局部作用域变量。
#       XXX: 通常不建议已这种方式修改其他作用域的变量，这将导致程序变得不可读，也不可维护。
#       XXX: 通常不建议使用全局变量，因为其生命周期会很长，垃圾回收无法回收。并且全局部变量不易维护。
#            减少全局变量，能减低耦合性。
#       XXX: 减少全局变量的使用就意味着我们应该尽量让变量的作用域在函数的内部，但是如果我们希望将一个局部变量的生命周期延长，
#            使其在定义它的函数调用结束后依然可以使用它的值，这时候就需要使用闭包。这里不再解释，后续会专门讲解。
#            很多人经常会将“闭包”和“匿名函数”混为一谈，两者并不相同。
#       XXX: 注意函数内部为局部作用域，非函数内部，都是全局作用域。嵌套作用域是相对于外面的函数作用域来说的。

def foo():
    b = 'hello'
    # python允许嵌套函数。
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()

a = 100
foo()
# 解析:
#   foo()调用内部的bar()函数的时候，
#       bar先打印a，
#           1. 查找函数bar内部局部作用域，没有，
#           2. 向上层查找，嵌套作用域foo()函数中，也没有，
#           3. 在向外寻找，全局作用域找到: a = 100
#       bar再打印b，
#           1. 查找函数bar内部局部作用域，没有，
#           2. 向上层查找，嵌套作用域foo()函数中，找打: b = 'hello'
#       bar再打印c，
#           1. 查找函数bar内部局部作用域，找打: c = True
#
# 整个过程完毕
#   注意内置作用域，指的是内置函数，如: input,等的作用域，当在全局作用域都找不到的时候，就会到内置作用域寻找。


g_a = 100
def change_global():
    global g_a  # 如果全局作用域没有该变量，则在全局作用域中声明一个。
    g_a = 200
    print('local range change g_a=', g_a)

print('before change, global g_a=', g_a)
change_global()
print('after change, global g_a=', g_a)

def change_local():
    l_a = 100
    print('before change, local l_a=', l_a)
    def changed():
        nonlocal l_a # 如果外围的嵌套作用域没有此变量，将声明一个。
        l_a = 200
        print('embeded range change l_a=', l_a)
    
    changed()
    print('after change, local l_a=', l_a)

change_local()