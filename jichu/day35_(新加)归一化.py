"""
归一化是一种将图像的像素值调整到指定范围(这里是0到1)的技术。
在图像处理中,归一化通常用于将不同尺度的图像数据转换为同一尺度,方便后续处理和分析。
cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)
src: 输入数组(例如图像)。
dst: 输出数组,与源数组有相同的大小和类型。这是函数的结果。
alpha: 归一化后的最小值。
beta: 归一化后的最大值。
norm_type: 归一化的类型。常见的类型包括cv2.NORM_MINMAX(线性归一化),cv2.NORM_L1,cv2.NORM_L2等。
dtype: 当这个参数为负数时,输出数组和输入数组类型相同。否则,它指定了输出数组的深度(例如,cv2.CV_32F表示32位浮点数类型)。
mask: 可选的操作掩码,用于指定要归一化的数组部分。
"""

import cv2
import numpy as np

# 假设img是一个已经加载的图像
img = cv2.imread('../image/lena.png')

# 使用cv2.normalize归一化
normalized_img = cv2.normalize(img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow('Normalized Image', normalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()