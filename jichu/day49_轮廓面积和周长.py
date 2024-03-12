import cv2
import numpy as np

"""
轮廓面积是指每个轮廓中所有像素带你围成区域的面积，单位为像素。
轮廓面积是轮廓重要的统计特性之一，通过轮廓面积的大小可以进一步分析每个轮廓隐含的信息
例如:通过轮廓面积区分物体大小识别不同的物体
在查找轮廓后,可能会有很多细小的轮廓,我们可以通过轮廓的面积进行过滤
//计算面积
cv2.contourArea(contour)
//计算周长
cv2.arcLength(curve,closed)
1-curve即轮廓
2-closed是否是闭合的轮廓
"""
# 该图像显示效果是黑白，但其实是三通道彩色图像
img = cv2.imread('../image/lun.png')
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
new_lun=cv2.drawContours(img_copy,contours,-1,(0, 0, 255),2)

# 计算轮廓的面积,contours[1]代表计算第2个轮廓
area= cv2.contourArea(contours[2])
print('面积',area)

# 计算轮廓的周长,contours[1]代表计算第2个轮廓
perimeter= cv2.arcLength(contours[1],False)
print('周长',np.int32(perimeter))

# 查看轮廓的数量
num_contours = len(contours)
print("轮廓数量",num_contours)
#print(contours)
# 显示
cv2.imshow('img',img)
cv2.imshow('new_lun',new_lun)
cv2.waitKey(0)
cv2.destroyAllWindows()