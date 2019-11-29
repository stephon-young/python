#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# 由于下面是中文注释，并且中文是utf-8编码，所以需要文件的开头行:
#   #-*- coding: utf-8 -*-
# 注意，如果同时要按照脚本方式运行，第一行写的:
#   #!/usr/bin/env python3
# 存在冲突，则需要按照下面的顺序填写即可:
#   #!/usr/bin/env python3
#   #-*- coding:utf-8 -*-

# 运行方式:
#   1. python hello.py 或者 python3 hello.py
#   2. 直接用脚本方式运行./hello.py，但是需要文件的首行添加:
#     #!/usr/bin/env python3
#  注意: 如果首行存在: #!/usr/bin/env python3 
#       但是命令行按照: python hello.py 
#       这时，首行失效，按照python运行，即意味着按照python 2 执行。
# 

'''
我是一个单引号注释
'''
"""
我是一个双引号注释
"""

# 字符串可以使用: 单引号，双引号，和三个单/双引号的方式用于注释
print('hello, world')
print("hello, world")
print('''hello, world''') # 这样通常用于多行字符串，并不会转义
print('hello, world''')  # 后面的两个引号为空字符串，是字符串字面值的连接。
print("hello, world""")  # 和上面的相同

a = '''
newbee, i am a three ' comment string.
i am a.
'''
b = """
abcdefg...
"""
# 下面的打印将会是一个元组打印: (xxx, yyy)
print("string a is: ", a)
print("string b is: ", b)

# 字符串连接打印
print("string a is: " + a)
print("string b is: " + b)

# 字符串字面值连接
print("a concat " "b")
print('a concat ' "b")
print('a concat ' + "b")

# 这个函数只能在python3中运行。
print('hello', 'world', sep=', ', end='!\n')
print('goodbye, world', end="!\n")


