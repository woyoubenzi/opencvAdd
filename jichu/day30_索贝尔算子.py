import cv2
import numpy as np
"""
索贝尔(sobel)算子
边缘是像素值发生跃迁(差异大)的位置,是图像的显著特征之一,在图像特征提取,对象检测,模式识别等方面都有重要的作用。

sobel算子对图像求一阶导数。一阶导数越大,说明像素在该方向的变化越大,边缘信号越强。
因为图像的灰度值都是离散的数字,sobel算子采用离散差分算子计算图像像素点亮度值的近似梯度
图像是二维的,即沿着宽度/高度两个方向

sober算子计算的是近似值,有误差
sober算子必须分开计算x,y轴,不然效果很差
"""

# 导入图片
img=cv2.imread('../image/chess.png')

# 计算X轴方向的梯度,留下垂直方向的边缘
dx=cv2.Sobel(img,-1,dx=1,dy=0,ksize=3)

# 计算y轴方向的梯度,留下水平方向的边缘
dy=cv2.Sobel(img,-1,dx=0,dy=1,ksize=3)

# 1.使用加法将xy合并
dst=cv2.add(dx,dy)

# 2.使用图像融合将xy合并
cv2.addWeighted(dx,0.5,dy,0.5,0)

# 展示
cv2.imshow('img',img)
cv2.imshow('xy',np.hstack((dx,dy)))
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()