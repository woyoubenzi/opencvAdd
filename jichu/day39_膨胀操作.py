import cv2
import numpy as np

"""
膨胀是腐蚀的相反操作,基本原理是只要保证卷积核的锚点是非0值,周边无论是否为0,都会变成0

cv2.dilate(src, kernel, iterations=None, anchor=None, borderType=None, borderValue=None)
src:输入图像,可以是单通道或多通道图像。
kernel:用于膨胀操作的结构元素（核）。可以使用 cv2.getStructuringElement 函数创建,也可以自定义一个 NumPy 数组作为核。
iterations:指定膨胀操作的迭代次数,默认为 1。
anchor:核的锚点位置,默认为核的中心。如果不指定,将使用核的中心作为锚点。
borderType:边界填充类型,默认为 cv2.BORDER_CONSTANT。
borderValue:当边界类型为 cv2.BORDER_CONSTANT 时,指定填充边界的值,默认为 0。
"""
# 腐蚀会让图片上的物体会变小,膨胀可以让其恢复到原来的大小

# 读取图像，确保为二值(灰度)图像
img = cv2.imread('../image/zhangsan.png', cv2.IMREAD_GRAYSCALE)

# 进行非操作,改变黑白
new_img=cv2.bitwise_not(img)

# 形态学卷积核-十字结构(可以选其他结构的)
kernel= cv2.getStructuringElement(cv2.MORPH_RECT ,(7,7))

# 膨胀
dst= cv2.dilate(new_img,kernel,iterations=1)

# 显示原始图像和膨胀后的图像
cv2.imshow('xy', np.hstack((img,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()