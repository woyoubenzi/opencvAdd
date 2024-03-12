import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
直方图均衡化是通过拉伸像素强度的分布范围,使得在0-255灰阶上的分布更加均衡,提高了图像的对比度,达到改善图像主观视觉效果的目的。
对比度较低的图像适合使用直方图均衡化方法来增强图像细节
原理:
1.计算累计直方图
2.将累计直方图进行区间转换
3.在累计直方图中,概率相近的原始值,会被处理为相同的值

直方图均衡化方法
cv2.equalizeHist(src[,dst])
src:原图像
dst:目标图像,即处理结果。如果提供了这个参数，将直接在这个图像上进行操作，而不是在原图像上进行操作。如果不提供，函数会返回均衡化后的图像。
"""

# 获取图像
img = cv2.imread('../image/lena.png')

# 转换为灰度图
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# lena变黑
gray_dark=gray-40

# lena变亮
gray_bright=gray+40

# 统计各自的直方图
hist_gray= cv2.calcHist([gray],[0],None,[256],[0,255])
hist_dark= cv2.calcHist([gray_dark],[0],None,[256],[0,255])
hist_bright= cv2.calcHist([gray_bright],[0],None,[256],[0,255])

# 使用matplotlib画出直方图
# plt.plot(hist_gray,label='gray',label='gray')
# plt.plot(hist_dark,label='dark',label='dark')
# plt.plot(hist_bright,label='bright',label='bright')
# plt.legend()

# 进行直方图均衡化
dark_gray= cv2.equalizeHist(gray)
dark_equ= cv2.equalizeHist(gray_dark)
bright_equ= cv2.equalizeHist(gray_bright)

# 统计直方图,用于画出直方图
hist_dark_equ= cv2.calcHist([dark_equ],[0],None,[256],[0,255])
hist_bright_equ= cv2.calcHist([bright_equ],[0],None,[256],[0,255])

# 使用matplotlib画出均衡化后的直方图
plt.plot(hist_dark_equ,label='dark')
plt.plot(hist_bright_equ,label='bright')
plt.legend()

cv2.imshow('dark_gray',dark_gray)
cv2.imshow('gray_dark',np.hstack((gray_dark,dark_equ)))
cv2.imshow('gray_bright',np.hstack((gray_bright,bright_equ)))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()