#!/usr/bin/python3
# -*- coding: utf-8 -*-

# __name__ 是一个隐含变量，代表了模块名称，当直接执行python脚本的时候，
#   即类似于: $ ./xxx.py 或者 $ python3 xxx.py 的时候
#   这个隐含变量的值为: __main__
#   这时，就可以通过这种方式做一些手脚了，比如测试程序等。
#   在使用 import <module>的方式的时候，这个变量的值变为了<module>的名字，将不会调用这部分:
#

if __name__ == '__main__':
    print('this is execute like: ./xxx.py')
else:
    print('this is import or others: ', __name__)

# import.py
#   import if_main
# 将输出: this is import or others: if_main
# 参考import.py

    