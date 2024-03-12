import cv2
import numpy as np

"""
Speeded-Up Robust Features(SURF)是一种用于图像特征检测与描述的算法,是对SIFT算法的改进
如果相对一系列的图像进行快速的特征检测,SIFT会非常慢,因此才有了SURF
不过准确率美SIFT算法高
注意:在较新的opencv版本中因为专利问题不能使用,需要降级到3.4.1.15
"""

# 用法SURF和SIFT一样,就是把SIFT的代码改成SURF

img=cv2.imread('../image/chess.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 创建SIFT对象
#sift=cv2.SURF.create()
surf = cv2.xfeatures2d.SURF_create()
# 进行检测,kp是一个列表,里面存放的是封装的KeyPoint对象(关键点)
kp=surf.detect(gray)

# 计算描述子
kp,des= surf.compute(gray,kp)
# SURF算法的描述子只有64个
print(des.shape)

# (在原图上)绘制找到的关键点
cv2.drawKeypoints(gray,kp,img)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()