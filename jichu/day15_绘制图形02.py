import cv2
import numpy as np
from PIL import ImageFont,ImageDraw,Image

"""
利用OpenCV提供的绘制图形API可以轻松在图像上绘制各种图形，比如直线，矩形，园，椭圆等图形
"""
# 绘制图形-直线，圆形，矩形，椭圆(弧线)，多边形，文本
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

----5 画多边形
polylines(img,[pts],isClosed,color[thickness[lineType[shift]]])
-多边形的点集，必须是int32位
-[pts] 三维，包含多个点的坐标[[(坐标1),(坐标2),(坐标N)]]
-isClosed 一个布尔值，表示多边形是否闭合

----6 填充多边形
fillPoly(img,[pts],color)

----7 绘制文本
putText(img,text,org,fontScale,color[thickness[lineType[bottomLeftOrigin]]])
-text 要绘制的文本
-org 文本在图片中的坐标
-fontFace 字体类型
-fontScale 字体大小
"""

# 创建纯黑的背景图用来画图形(由于zeros默认为000,所以是全黑)
img=np.zeros((480,640,3),np.uint8)

# 1-绘制多边形
pts=np.array([[(255,100),(150,300),(50,280)]],np.int32)
cv2.polylines(img,pts,True,(0,0,255),0)

# 1.1-填充多边形
cv2.fillPoly(img,pts,(0,255,0))

# 2-绘制文本
cv2.putText(img,'hello,world',(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,[0,0,255])

# 2.1-绘制中文(opencv没有办法直接绘制中文，但是pillow包可以曲线绘制)
# 导入pillow包,导入名是PIL.

# 创建白色背景
img2=np.full((200,200,3),fill_value=255,dtype=np.uint8)
img3=np.ones((200,200,3),np.uint8)

# 导入字体文件(window下面的font文件内有)
font=ImageFont.truetype('./FZYTK.TTF',25)

# 创建一个pillow的图片
img_pil=Image.fromarray(img3)

draw=ImageDraw.Draw(img_pil)

# 利用draw去绘制中文
draw.text((40,50),'你好，世界',font=font,fill=(0,255,0,0))

# 重新变回ndarray
img2=np.array(img_pil)

cv2.imshow('draw2',img2)

# 展示图像
cv2.imshow('draw',img)
cv2.waitKey(0)
cv2.destroyAllWindows()