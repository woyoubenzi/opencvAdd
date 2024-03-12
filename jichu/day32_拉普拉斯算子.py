import cv2
import numpy as np

"""
拉普拉斯算子

索贝尔算子是模拟一阶求导，导数越大的地方说明变换越剧烈，越有可能是边缘。
那如果继续求导呢？
可以发现"边缘处"的二阶导数=0,我们可以利用这一特性去寻找图像的边缘。注意:二阶求导为0的位置也可能是无意义的位置(可能需要去噪)

Laplacian(src,ddepth,dst,scale,delta,borderType)
可以同时求两个方向的边缘
对噪音敏感,一般调用拉普拉斯算子前先要去噪
"""

# 导入图片
img=cv2.imread('../image/lena.png')

# 高斯滤波去噪
dst= cv2.GaussianBlur(img,(3,3),50)

# 导入椒盐噪点图片
#img=cv2.imread('../image/blue.png')

# 中值滤波去噪点
#dst=cv2.medianBlur(img,15)

# 拉普拉斯算子
dst1=cv2.Laplacian(dst,-1,ksize=3)


# 展示img
cv2.imshow('xy',np.hstack((img,dst,dst1)))
cv2.waitKey(0)
cv2.destroyAllWindows()