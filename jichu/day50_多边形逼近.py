import cv2
import numpy as np

"""
多边形逼近可以将不规则的轮廓形状转化为具有更少角点的多边形，从而简化图形结构，提高处理效率

查找轮廓(findContours)后的轮廓信息(contours)可能过于复杂不平滑,可以用approxPolyDP函数对该多边形曲线做适当近似,这就是轮廓的多边形逼近。
approxPolyDP就是以多边形去逼近轮廓,采用的是Douglas-Peucker算法(方法名中的DP)

DP算法原理比较简单,核心就是不断找多边形最远的点,加入形成新的多边形,直到最短距离小于指定的精度

cv2.approxPolyDP(curve,epsilon,closed[,approxCurve])
curve: 输入的轮廓。 
epsilon: Douglas-Peucker 算法中的精度参数,它是一个距离阈值,用于控制逼近的精度。逼近值越大越粗糙,越小越精细
closed: 一个布尔值,表示轮廓是否是闭合的。
"""

# 该图像显示效果是黑白，但其实是三通道彩色图像
img = cv2.imread('../image/shou.png')
# 转换为双通道灰度图
img1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# 全局二值化,返回两个值
thresh,dst= cv2.threshold(img1,150,255,cv2.THRESH_BINARY)

# 查找轮廓，返回两个值.返回两个东西，轮廓，层级
contours,hierarchy= cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓会直接修改原图，可以将原图copy一份
img_copy=img.copy()

# 绘制轮廓
# 绘制时需要注意，灰度图因为只有黑白两种颜色，所以在灰度图是绘制不出彩色的
new_lun=cv2.drawContours(img_copy,contours,2,(0, 0, 255),2)

# 使用多边形逼近，近似模拟手的轮廓(返回结果只有一个轮廓)
# 逼近值越大越粗糙,越小越精细,当前逼近值是10
# 这个轮廓需要你自己找到
approx= cv2.approxPolyDP(contours[2],20,True)

# approx本质上就是一个轮廓数据,ndarray类型
print(type(approx))

# 因为绘制轮廓时需要接受数组类型的ndarray,所以要将approx重新包裹在数组[]内
cv2.drawContours(img_copy,[approx],0,(0, 255, 0),2)

# 显示
#cv2.imshow('img',img)
cv2.imshow('new_lun',new_lun)
cv2.waitKey(0)
cv2.destroyAllWindows()