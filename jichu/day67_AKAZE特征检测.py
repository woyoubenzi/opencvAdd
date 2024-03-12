import cv2
import numpy as np

"""
AKAZE算法
算法是一种用于特征检测和描述的算法,由Pablo F. Alcantarilla等人开发。
它是KAZE算法的加速版本,旨在提供一种高性能的特征匹配方法,同时保持对图像噪声的鲁棒性和对尺度变化的不变性
"""

img=cv2.imread('../image/chess.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 创建对象
sift=cv2.AKAZE.create()
# 进行检测,kp是一个列表,里面存放的是封装的KeyPoint对象(关键点)
kp=sift.detect(gray)

# 计算描述子
kp,des= sift.compute(gray,kp)
print(des.shape)

# (在原图上)绘制找到的关键点
cv2.drawKeypoints(gray,kp,img)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()