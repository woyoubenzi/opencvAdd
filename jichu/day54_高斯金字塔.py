import cv2
import numpy as np

"""
高斯金字塔是通过高斯平滑和亚采样获得一系列采样图像
向下采样原理
原始图像M*N->处理后图像M/2*N/2
每次处理后,结果图像是原来的1/4
注意:向下采样会丢失图像信息

-向下采样,缩小是去除偶数位的像素
dst = cv2.pyrDown(img)
img: 输入的图像。
dst: 降采样后的图像，尺寸为输入图像的一半,大小为图像1/4

-向上采样,放大后在像素中填0,然后做近似处理。
dst = cv2.pyrUp(img)
img: 输入的图像。
dst: 上采样后的图像，尺寸为输入图像的两倍。  
"""

# 获取图像
img = cv2.imread('../image/lena.png')
print(img.shape)

"""
向下采样,缩小是去除偶数位的像素
"""
# 分辨率减小，向下采样
downdst= cv2.pyrDown(img)
print(downdst.shape)

"""
向上采样,放大后在像素中填0,然后做近似处理。
"""
updst= cv2.pyrUp(img)
print(updst.shape)

# 显示
cv2.imshow('img',img)
cv2.imshow('downdst',downdst)
cv2.imshow('updst',updst)
cv2.waitKey(0)
cv2.destroyAllWindows()