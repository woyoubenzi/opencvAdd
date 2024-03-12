import cv2
import numpy as np

"""
图像的融合

图像融合是通过混合两幅图像的像素值,通过调整两幅图像的权重并相加来创建一幅新的图像。
主要用于将两幅图像合并成一幅,使得合并后的图像具有某种过渡效果。常用于图像混合、渐变、融合等应用。
cv2.addWeighted(src1,alpha,src2,beta,gamma)
-src1 图像1
-alpha 图像1权重 百分比,一般是0-1
-src2 图像2
-beta 图像2权重 百分比,一般是0-1
-gamma 可选,用于控制输出图像的亮度 任意实数值,默认为0
"""

# 读取图片
img1=cv2.imread('../image/ali.png')
img2=cv2.imread('../image/ali.jpg')

# 需要将两个图片的形状,维度保持一致
new1= img1[0:1440,0:1280]
new2= img2[0:1440,1280:2560]

# 图像融合
cv_aw= cv2.addWeighted(img1,0.5,img2,0.5,0)


cv2.namedWindow('mao',cv2.WINDOW_NORMAL)
cv2.resizeWindow('mao',800,800)

cv2.imshow('mao',cv_aw)

cv2.waitKey(0)

cv2.destroyAllWindows()
