import cv2
import numpy
"""
优化运行速度，滤波
"""
# 检查优化开关的开启和关闭
flag=cv2.useOptimized()
print("优化开关的状态是",format(flag))

# 开启/关闭优化
# 语法 cv2.setUseOptimized(布尔值)

e1=cv2.getTickCount()
img=cv2.imread('../image/ali.png')

"""
这是使用 OpenCV 中的中值滤波器对图像进行滤波的代码。
具体来说，这段代码使用了一个循环，在每次迭代中，
以增量为2的步长从5到349之间的奇数值作为内核大小，对图像进行中值滤波。

中值滤波是一种非线性滤波方法，它用局部区域内的像素值的中值来替代中心像素的值。
在这个例子中，cv2.medianBlur(img, i) 将图像 img 使用大小为 (i, i) 的方形内核进行中值滤波。
i 的取值从5开始，以2的步长递增，一直到349。

这种操作常常用于去除图像中的噪声，因为中值滤波对于椒盐噪声等噪声类型有较好的去除效果。
在实际应用中，你可以根据图像的特性和需要去除的噪声类型来选择合适的内核大小。
"""

for i in range(5,201,2):
    img=cv2.medianBlur(img,i)

e2=cv2.getTickCount()
t=(e2-e1)/cv2.getTickFrequency()
print(t)