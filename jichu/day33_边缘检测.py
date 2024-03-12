import cv2
import numpy as np

"""
边缘检测Canny(最优算法)
Canny边缘检测算法是John F.Canny于1986年开发出来的一个多级边缘检测算法,也被很多人认为是边缘检测的最优算法
最优边缘检测的三哥主要评价标准是：
-低错误率:标识出尽可能多的实际边缘,同时尽可能的减少噪声产生的误报
-高定位性:标识出的边缘要与图像中的实际边缘尽可能接近
-最小定位:图像中的边缘只能标识一次
Canny边缘检测的一般步骤
-去噪:边缘检测容易受到噪声影响,在进行边缘检测前通常需要先进行去噪,一般用高斯滤波。
-计算梯度:对平滑后的图像采用sobel算子计算梯度和方向

非极大值抑制(Non-maximum suppression),简称NMS算法,可以获取局部最大值
-在获取了梯度和方向后,遍历图像,去除所有不是边界的点
-实现方法:逐个遍历像素点,判断当前像素点是否是周围像素点中具有相同方向梯度的最大值

滞后阈值:是指在进行边缘检测时,使用两个阈值进行处理的一种方法,这两个阈值分别是minVal和maxVal。
小于minVal的像素抛弃。
大于maxVal的像素保留作为强边缘。
介于minVal和maxVal之间的像素,如果与强边缘相连,则保留,否则抛弃
阈值大小需要自己设置


Canny(img,minVal.maxVal,...)
"""
# 导入图片
img=cv2.imread('../image/lena.png')

# 阈值越小,细节越丰富
ds= cv2.Canny(img,100,200)
de= cv2.Canny(img,64,128)
dt= cv2.Canny(img,50,250)

# 展示
cv2.imshow('img',img)
cv2.imshow('xy',np.hstack((ds,de,dt)))
cv2.waitKey(0)
cv2.destroyAllWindows()