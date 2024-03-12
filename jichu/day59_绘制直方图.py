import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
使用matplotlib画直方图
"""
# 获取图像
img = cv2.imread('../image/lena.png')

"""
不使用opencv的统计方法cv2.calcHist
"""
# 转换为灰度图
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 将图像转换为一维后,统计直方图数据
#plt.hist(gray.reshape(-1))
#plt.hist(gray.ravel(),bins=256,range=[0,255])

"""
使用opencv的统计方法
"""
# 统计直方图
histb= cv2.calcHist([img],[0],None,[256],[0,255])
histg= cv2.calcHist([img],[1],None,[256],[0,255])
histr= cv2.calcHist([img],[2],None,[256],[0,255])

#
plt.plot(histb,color='b',label='b')
plt.plot(histg,color='g',label='g')
plt.plot(histr,color='r',label='r')
# 图例,和label配合使用
plt.legend()

# 展示
plt.show()