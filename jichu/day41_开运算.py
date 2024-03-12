import cv2
import numpy as np

"""
开运算和闭运算都是腐蚀和膨胀的基本应用
开运算是去除图形外部的噪点
开运算也可以去噪点,去除小物体,平滑边界等
开运算=先腐蚀再膨胀

cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])
src:输入图像,可以是单通道或多通道的图像（灰度图或彩色图）。
op:形态学操作的类型,可以是以下其中之一:
1-cv2.MORPH_OPEN:开运算
2-cv2.MORPH_CLOSE:闭运算
3-cv2.MORPH_GRADIENT:形态学梯度
4-cv2.MORPH_TOPHAT:顶帽运算
5-cv2.MORPH_BLACKHAT:黑帽运算
kernel:形态学操作的核（结构元素）,用于定义操作的形状和大小。噪点多就大,反之小
dst:可选参数,输出图像。如果没有提供,函数会自动创建一个与输入图像大小相同的输出图像。
anchor:可选参数,表示锚点的位置,默认为 (-1, -1),即核的中心。
iterations:可选参数,指定形态学操作的迭代次数,默认为 1。
borderType:可选参数,指定边界类型,默认为 cv2.BORDER_CONSTANT。
borderValue:可选参数,指定边界值,当 borderType 为 cv2.BORDER_CONSTANT 时生效,默认为 0。
"""

# 读取图像,确保为二值(灰度)图像
img = cv2.imread('../image/jjii.png', cv2.IMREAD_GRAYSCALE)

# 进行非操作,改变黑白
new_img=cv2.bitwise_not(img)

# 结构元素（卷积核）
kernel= cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

# 开运算(这个图要腐蚀2次才能把小物体去掉)
dst=cv2.morphologyEx(new_img,cv2.MORPH_OPEN,kernel,iterations=1) 

# 显示
cv2.imshow('xy', np.hstack((new_img,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()