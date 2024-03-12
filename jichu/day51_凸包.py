import cv2
import numpy as np

"""
逼近多边形是轮廓的高度近似,但是我们希望用一个多边形的凸包来简化它。
凸包跟多边形逼近很像,只不过他是物体的最外层的凸多边形。
凸包指的是完全包含原有轮廓,并且仅由轮廓上的点所构成的多边形.
凸包的每一处都是凸的,即在凸包内连接的任意两点都在凸包的内部。
在凸包内,任意连续的三个点的内角小于180°

cv2.convexHull(points[,hull[,clockwise[,returnPoints]]])
points:轮廓
colckwise:顺时针绘制
"""
# 该图像显示效果是黑白，但其实是三通道彩色图像
img = cv2.imread('../image/shou.png')

# 将图片转换为灰度图
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 二值化
thersh,binary=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

# 查找所有轮廓，以树形展示
continues,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# 在原图上绘制轮廓（这个图最大的轮廓在0号位,所以后面要画多边形也是0）
cv2.drawContours(img,continues,0,(0,0,255),2)

# 多边形逼近
approx=cv2.approxPolyDP(continues[0],20,True)

# 画出多边形逼近的轮廓
cv2.drawContours(img,[approx],0,(0,255,0),2)

# 计算凸包
hull= cv2.convexHull(continues[0])

# 画出凸包的轮廓
cv2.drawContours(img,[hull],0,(255,0,0),2)

# 显示
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()