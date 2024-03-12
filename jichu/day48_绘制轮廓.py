import cv2
import numpy as np

"""
这个函数可以用于在图像上绘制指定轮廓的边界,也可以用于填充轮廓内部。如果 thickness 参数为负值(-1),则函数将会填充轮廓内部。

cv2.drawContours(image, contours, contourIdx, s[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]])
image: 要绘制轮廓的图像。
contours: 轮廓列表,是一个点集的列表。可以通过 cv2.findContours() 函数获取。
contourIdx: 要绘制的轮廓的索引,-1 表示绘制所有轮廓。
color: 绘制轮廓的颜色,通常是一个BGR三元组,例如 (0, 255, 0) 表示绿色。
thickness: 可选参数,轮廓线的粗细,默认值为 1。
lineType: 可选参数,轮廓线的类型,可以是 cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA 等,默认值为 cv2.LINE_8。
hierarchy: 可选参数,轮廓的层次结构,通常可以不指定。
maxLevel: 可选参数,绘制的轮廓的最大层级,默认值为 0。
offset: 可选参数,指定每个轮廓中的每个点的偏移量,默认值为 (0, 0)。
"""

# 以灰度图像方式读取图像
img = cv2.imread('../image/lun.png')
img1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# 全局二值化,返回两个值
thresh,dst= cv2.threshold(img1,150,255,cv2.THRESH_BINARY)

# 查找轮廓，返回两个值
contours,hierarchy= cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓会直接修改原图，可以将原因copy一份
img_copy=img.copy()

# 绘制轮廓
# 绘制时需要注意，灰度图因为只有黑白两种颜色，所以在灰度图是绘制不出彩色的
cv2.drawContours(img_copy,contours,-1,(255, 0, 255),2)

# 显示
cv2.imshow('img',img)
cv2.imshow('new_lun',img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()