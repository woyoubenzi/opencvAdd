"""
逆傅里叶操作(还原图像)
傅里叶过程是可逆的,图像经过傅里叶变换,逆傅里叶变换后,能够恢复到原始图像
可以在频域对图像进行处理,在频域的处理会反映在逆变换图像上

[函数介绍]
np.fft.ifft2 实现逆傅里叶变换,返回一个复数数组

numpy.fft.ifftshift 将低频由中心位置转移到左上角

iimg=np.abs 逆傅里叶变换结果取绝对值
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img=cv2.imread('../image/cat.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 傅里叶变换
f=np.fft.fft2(gray)
fshift=np.fft.fftshift(f)
# 傅里叶逆回来(原图)
ifshuft=np.fft.ifftshift(fshift)
io=np.fft.ifft2(ifshuft)
io=np.abs(io)

# 显示
plt.subplot(121)
plt.imshow(gray,cmap='gray')
plt.title('one')
plt.axis('off')
plt.subplot(122)
plt.imshow(io,cmap='gray')
plt.title('two')
plt.axis('off')
plt.show()
