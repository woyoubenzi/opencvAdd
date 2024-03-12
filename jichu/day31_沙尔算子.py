import cv2
import numpy as np

"""
沙尔算子(Scharr)
Scharr(src,ddepth,dx,dy,dst,scale,delta,borderType)
当内核大小为3*3时,以上Sobel内核可能产生比较明显的误差(毕竟,Sobel算子只是求取了导数的近似值)。
为解决这一问题,OpenCV提供了Scharr函数,但该函数仅作用于大小为3的内核。
该函数的运算于Sobel函数一样快,但结果更加精确
Scharr算子和Sobel很类似,只不过使用不同的Kernel值,放大了像素变换的情况

Scharr算子只支持3*3的kernel所有没有kernel参数
Scharr算子只能求X方向或Y方向的边缘
Sobel算子的ksize设为-1就是Scharr算子
Scharr算子擅长寻找细小的边缘,一般用的很少
"""

# 导入图片
img=cv2.imread('../image/lena.png')

# 计算X轴方向的梯度,留下垂直方向的边缘
dx=cv2.Scharr(img,-1,dx=1,dy=0)

# 计算y轴方向的梯度,留下水平方向的边缘
dy=cv2.Scharr(img,-1,dx=0,dy=1)

# 使用加法将xy合并
dst=cv2.add(dx,dy)



# 展示
#cv2.imshow('img',img)
cv2.imshow('xy',np.hstack((dx,dy,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()