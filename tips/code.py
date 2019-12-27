#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 二维码的学习与使用
#   1. 需要先安装 pip install qrcode, qrcode依赖Image, 所以需要安装Image
#from qrcode import QRCode
import qrcode
import matplotlib.pyplot as plt
#import image

def qr_simple(str):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # 下面的并不能在终端显示照片
    # 终端显示图片
    plt.imshow(img)
    plt.show()

    
    with open('baidu.png', 'wb') as f:
        img.save(f)
    img.show()

qr_simple('www.baidu.com')