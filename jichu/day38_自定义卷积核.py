import cv2
import numpy as np

"""
opencv提供了获取形态学卷积核的api,不需要我们手工创建形态学卷积核

cv2.getStructuringElement(shape,ksize,anchor=none)
shape: 结构元素(卷积核)的形状，可以是以下几种：
1.cv2.MORPH_RECT: 矩形结构元素。
2.cv2.MORPH_ELLIPSE: 椭圆结构元素。
3.cv2.MORPH_CROSS: 十字形结构元素。
ksize: 结构元素(卷积核)的大小，定义为一个元组 (rows, cols)。
anchor: 结构元素的锚点位置，默认为结构元素的中心。可以是一个元组 (anchor_row, anchor_col)
"""

# 读取图像，确保为二值(灰度)图像
img = cv2.imread('../image/zhangsan.png', cv2.IMREAD_GRAYSCALE)

# 进行非操作,改变黑白(因为目前的卷积核是白色的,只会腐蚀白色区域)
new_img=cv2.bitwise_not(img)

# 形态学卷积核-十字结构(可以选其他结构的)
kernel= cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

# 查看卷积核形状
print(kernel)

# 腐蚀
dst= cv2.erode(new_img,kernel)

# 显示原始图像和腐蚀后的图像
cv2.imshow('xy', np.hstack((img,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()