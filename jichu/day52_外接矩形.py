import cv2
import numpy as np

"""
外接矩形分最小外接矩形和最大外接矩形

最小外接矩阵(根据物体不同,可能会倾斜)
rect = cv2.minAreaRect(points)
points:轮廓
返回值:
rect[0] 是矩形的中心坐标 (X, Y)。
rect[1] 是矩形的宽度和高度。
rect[2] 是矩形的旋转角度。

获取由最小外接矩阵返回的旋转矩形的四个顶点坐标
points = cv2.boxPoints(rect)
rect 是 cv2.minAreaRect() 返回的旋转矩形参数。points 将包含旋转矩形的四个顶点坐标。

最大外接矩阵(正正方方的矩形)
x, y, w, h = cv2.boundingRect(points)
返回值是一个包围轮廓的矩形，其中 (x, y) 是矩形的左上角坐标，(w, h) 是矩形的宽度和高度
"""
# 该图像显示效果是黑白，但其实是三通道彩色图像
img = cv2.imread('../image/hello.png')

# 将图片转换为灰度图
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 二值化
thersh,binary=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

# 查找所有轮廓，以树形展示
continues,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

"""
最小外接矩形(根据物体不同,可能会倾斜)
"""
# 最小外接矩形,rect是一个Rotated Rect旋转的矩形
rect=cv2.minAreaRect(continues[1])

# 计算最小外接矩形的4个坐标点
box=cv2.boxPoints(rect)
print(box)
# 注意坐标必须是整数，所以需要将4个坐标点转换为整数(四舍五入)
box=np.round(box)
box=np.intp(box)

# 绘制最小外接矩形
cv2.drawContours(img,[box],0,(255,0,0),2)

"""
最大外接矩阵(正正方方的矩形)
"""
# 最大外接矩形
x, y, w, h = cv2.boundingRect(continues[1])

# 画图-根据4个点画矩形(xy是左上角坐标,x+w,y+h是右下角坐标)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

# 显示
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()