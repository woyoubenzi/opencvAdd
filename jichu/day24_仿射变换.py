import cv2
import numpy as np
"""
仿射变换(图像平移,变换矩阵,通过三个点来确定变换矩阵,透视变换)
仿射变换是图像旋转缩放平移的总称,具体的做法是通过一个矩阵和原图片坐标进行计算,得到新的坐标,完成变换,所以关键就是这个矩阵

"""
# 获取图片
dog=cv2.imread('../image/lookbook.jpg')
# 长宽高
h,w,ch=dog.shape

"""
1.仿射变换-平移矩阵
假如要沿着X轴移动,就在tx的位置写下移动值
假如要沿着Y轴移动,就在ty的位置写下移动值

warpAffine(src,M,dsize,dsize,mode,value)
M:变换矩阵{
  矩阵种的每个像素由(x,y)组成,(x,y)表示这个像素的坐标
  x=1*x,0*y,tx*1=x+tx
  y=0*x,1*y,ty*1=y+ty
}
dsize:输出图像的大小
dsize:与resize的插值算法一致
mode:边界外推法标志
value:填充边界值
  
"""
# # 变换矩阵-平移,最少是float32位。[[X轴][Y轴]]向右平移500像素,向下平移100像素,默认向右向下,-代表相反方向
# M=np.float32([[1,0,500],[0,1,100]])
# # 平移操作
# new_dog= cv2.warpAffine(dog,M,dsize=(w,h))
"""
2.仿射变换-交换矩阵(旋转,缩放)

仿射变换的难点就是计算变换矩阵,OpenCV提供了计算变换矩阵的API
cv2.getRotationMatrix2D(center,angle,scale)
center:中心点,以图片的哪个点作为旋转时的中心点
angle:角度,旋转的角度,按照逆时针旋转
scale:缩放比例.scale=1意味着保持原大小,scale<1意味着缩小图像,scale>1意味着放大图像
"""
# 变换矩阵-以图像中心点旋转
#M=cv2.getRotationMatrix2D((100,100),20,0.5)
# W是原图的宽,H是原图的高。W/2是原图的一半宽度的位置
M=cv2.getRotationMatrix2D((w/2,h/2),270,1)
# 注意opencv种是先宽度,再高度
new_dog=cv2.warpAffine(dog,M,(w,h))

"""
3.仿射变换-通过三个点来确定变换矩阵
可以用来对齐图像
cv2.getAffineTransform(src[],dst[])通过三点可以确定交换后的位置,相当于解方程,3个点对应三个方程,能解出偏移的参数和旋转的角度
src[]:原目标的三个点
dst[]:对应变换后的三个点
"""
# # 获取原始点
# src=np.float32([[200,100],[300,200],[200,300]])
# # 获取变换后的点
# dst=np.float32([[100,150],[360,200],[280,120]])
# # 变换矩阵-从原点变为指定点
# M=cv2.getAffineTransform(src,dst)
# new_dog=cv2.warpAffine(dog,M,(w,h))
"""
4.仿射变换-透视变换
透视变换就是将一种坐标系变换成另一种坐标系,简单来说可以把一张斜的图变正
warpPerspective(img,M,dsize,...)
对于透视变换来说,M是一个3*3的矩阵
getPerspectiveTransform(src,dst)获取透视变换的变换矩阵,需要4个点,即图片的4个角
"""
# # 获取原图的4个坐标
# src=np.float32([[100,300],[900,300],[100,1000],[900,1000]])
# # 获取目标图的4个坐标
# dst=np.float32([[100,300],[900,300],[100,1000],[900,1000]])
# #
# M= cv2.getPerspectiveTransform(src,dst)
# #透视变换
# new_dog=cv2.warpPerspective(dog,M,(1080,1080))

# 显示
cv2.imshow('dog',dog)
cv2.imshow('new_dog',new_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()