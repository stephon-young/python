#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 注意上面的两行的顺序不能乱了，否则，在linux下面按照脚本启动会失败。
# 1. 脚本运行的时候使用python3解释器来进行解析。
# 2. 文件编码为utf-8类型

import sys

print(sys.version_info)
print(sys.version)

# 或者使用 python --version 获取版本