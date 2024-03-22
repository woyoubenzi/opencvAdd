"""
霍夫(hough)梯度法-圆检测功能
原则上霍夫变换可以检测任何形状,但复杂的形状需要的参数越多,霍夫空间的维度就越多.霍夫梯度法是霍夫变换的改进,目的是减少霍夫空间的维度,提高效率
霍夫圆检测对噪声比较明显

[语法]
circles = cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
image:需要进行霍夫变换的输入图像,通常是单通道灰度图像。
method:用于检测圆的方法。OpenCV中提供了两种方法:
cv2.HOUGH_GRADIENT:基于梯度的霍夫变换方法。
cv2.HOUGH_GRADIENT_ALT:改进的基于梯度的霍夫变换方法。(这个改进的方法没几个人提到)
dp:霍夫空间的累加器分辨率与图像分辨率之比的倒数。通常取值为 1,表示与图像分辨率相同。
minDist:检测到的圆之间的最小距离。如果设为太小的值,可能会导致检测到重复的圆。
param1:Canny边缘检测的高阈值。通常这个参数是用来辅助检测圆边缘的,可根据具体情况调整。
param2:霍夫变换的累加器阈值。只有当某个候选圆的累加器值高于这个阈值时,才会被认为是检测到的圆。
minRadius:检测到的圆的最小半径。
maxRadius:检测到的圆的最大半径。

返回值 circles 是一个三维数组,其形状为 (1, N, 3),其中 N 是检测到的圆的数量。每个圆由 (x, y, radius) 表示,其中 (x, y) 是圆心的坐标,radius 是半径。

除了检测直线外,霍夫变换也可以用于检测其他形状.

用人话来说:就是读图,然后去噪(如果有的话),检测圆(调整参数),得到包含圆的长宽半径,在原图上画出来
"""

import cv2  
import numpy as np  
  
# 读取图片  
img = cv2.imread('../image/qiu.jpg')  
  
# 确保图片正确读取  
if img is None:  
    print("Error: Could not read the image.")  
    exit()  
  
# 转换为灰度图像  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
# 使用中值滤波进行噪点过滤  
median = cv2.medianBlur(gray, 7)  
  
# 霍夫圆检测  
circles = cv2.HoughCircles(median, cv2.HOUGH_GRADIENT, 1, 150,   
                             param1=50, param2=30, minRadius=0, maxRadius=0)  
print(circles) 
# 检查是否检测到圆  
if circles is not None:  
    # 遍历检测到的圆  
    for i in circles[0, :]:  
        print('分割线----------')
        print(i)
        # 绘制圆形  
        cv2.circle(img, (int(i[0]), int(i[1])), int(i[2]), (0, 255, 0), 2)  
        # 绘制圆心  
        cv2.circle(img, (int(i[0]), int(i[1])), 2, (0, 0, 255), 3)  
  
# 显示图像  
cv2.imshow('img', img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()