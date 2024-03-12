import cv2
import numpy as np

"""
"拉普拉斯金字塔是通过将原图像减去通过向上采样后再向下采样（或者说是先缩小后再放大）的图像构成的"
"这个过程旨在保留原始图像中的高频信息,即相对较小尺度的细节,从而得到一系列突出图像细节的图像"
拉普拉斯金字塔是由高斯金字塔构成的,没有专门的函数
拉普拉斯金字塔图像主要包含原图像的高频信息,其中大部分元素代表图像中的边缘、纹理等相对较小尺度的细节,而且这些元素的绝大部分值为0。这种特性使得拉普拉斯金字塔在图像压缩和特征提取方面具有优势
"""

# 获取图像
img = cv2.imread('../image/lena.png')
print(img.shape)

# 先缩小原图
downdst= cv2.pyrDown(img)
print(downdst.shape)

# 再放大缩小后的图
updst= cv2.pyrUp(downdst)
print(updst.shape)

# 原图和高斯金字塔(缩小放大)的差就是拉普拉斯金字塔
lap0=img-updst

# 第二层拉普拉斯金字塔
dst1=cv2.pyrDown(updst)
dst1=cv2.pyrUp(dst1)
lap1=updst-dst1


# 显示
cv2.imshow('img',img)
cv2.imshow('lap0',lap0)
cv2.imshow('lap1',lap1)
cv2.waitKey(0)
cv2.destroyAllWindows()