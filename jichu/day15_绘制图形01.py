# 引用命名空间
import cv2
import numpy as np
"""
利用OpenCV提供的绘制图形API可以轻松在图像上绘制各种图形，比如直线，矩形，园，椭圆等图形
"""
# 黑,白色背景图 绘制图形-直线，圆形，矩形，椭圆(弧线)
"""
----1 画直线
line(img,pt1,pt2,color,thickness,lineType,shift) 
-img 在哪个图像上画线
-pt1 开始的位置,二元组(x,y)
-pt2 结束的位置,二元组(x,y)
-color 颜色
-thickness (可选): 绘制椭圆轮廓的线条宽度。如果为正值，则表示线条的宽度。如果为负值，表示填充椭圆内部。默认值为1
-lineType (可选):线型(线型位-1，4，8，16)，默认为8(数值越大线条越光滑)
-shift (可选):坐标缩放比例,如果为0，则表示不进行位移。

----2 画矩形
rectangle(img,pt1,pt2,color,thickness,lineType,shift) 
属性跟直线一样，这些属性名可以互相参考

----3 画圆
circle(img,center,radius,color[thickness[lineType[shift]]]) ，[]内参数代表可选
-center 中心点,二元组(x,y)
-radius 半径

----4 画椭圆
ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) 
-axes  椭圆的长轴和短轴长度(长宽的一半)，是一个二元组(长，宽)
-angle 椭圆的旋转角度，以度为单位。正值表示逆时针旋转
-startAngle  椭圆弧的起始角度，以度为单位
-endAngle 椭圆弧的结束角度，以度为单位
"""



"""
np.zeros 用于创建一个由零组成的数组。
np.ones 用于创建一个由1组成的数组。
"""

# 创建纯黑的背景图用来画图形(由于zeros默认为000,所以是全黑)
img=np.zeros((480,640,3),np.uint8)

# 创建纯白的图像(zeros默认为111,将其*255。得到一个纯白图像)

#white_img = np.ones((480, 640, 3),np.uint8) * 255

# 画直线
cv2.line(img,(10,20),(300,400),(0,0,255),5,4)

# 画矩形
cv2.rectangle(img,(80,100),(180,480),(0,255,0),5,16)

# 画圆
cv2.circle(img,(320,240),100,(255,255,0),2,18)

# 画椭圆
cv2.ellipse(img, (140, 420), (100, 30), 0, 1, 360, (255, 255, 255))

# 展示图像
cv2.imshow('draw',img)
cv2.waitKey(0)
cv2.destroyAllWindows()