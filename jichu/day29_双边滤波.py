import cv2
import numpy as np

"""
双边滤波(去噪,美颜)
双边滤波对于图像的边缘信息能更好的保存.其原理为一个空间距离相关的高斯函数与一个灰度距离相关的高斯函数相乘
双边滤波本质上是高斯滤波,不同点在于:双边滤波既利用了位置信息又利用了像素信息来定义滤波窗口的权重。而高斯滤波只用了位置
双边滤波可以保留边缘，同时可以对边缘内的区域进行平滑处理。
双边滤波的作用就相当于做了美颜

cv2.bilateralFilter(src,d,sigmaColor,sigmaSpace,dst,borderType)
sigmaColor是计算像素信息使用的sigma
sigmaSpace是计算空间信息使用的sigma
"""
# 导入图片
img=cv2.imread('../image/lena.png')

# 双边滤波
# 双边滤波对椒盐噪声几乎没任何效果
dst= cv2.bilateralFilter(img,7,sigmaColor=20,sigmaSpace=10)

# 展示
cv2.imshow('lena',np.hstack((img,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()