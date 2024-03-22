"""
概率霍夫变换: 概率霍夫变换在计算上更高效,尤其适用于检测图像中的线段
lines = cv2.HoughLinesP(image, rho, theta, threshold, minLineLength, maxLineGap)

image(输入数组):这是输入的二值化图像,通常是Canny边缘检测的输出或其他二值化图像。HoughLinesP 将在这个图像上执行霍夫变换以检测直线。
lines(输出数组):这是一个输出参数,用于存储检测到的直线的参数。通常,这是一个二维数组,每一行代表一条直线,每行包含四个元素,分别表示直线上的两个端点的坐标 (x1, y1, x2, y2)。
rho:表示霍夫空间中的距离分辨率(以像素为单位)。它决定了在霍夫空间中离散化的距离间隔大小。
theta:表示霍夫空间中的角度分辨率(以弧度为单位)。它决定了在霍夫空间中离散化的角度间隔大小。
threshold:这是一个阈值,表示检测直线所需的最小投票数。只有在霍夫空间中投票超过这个阈值的直线才会被检测到。
minLineLength:可选参数,表示所允许的直线的最小长度。任何短于此值的直线都不会被检测。
maxLineGap:可选参数,表示在同一直线上的线段之间的最大允许间隔。如果两条线段之间的间隔小于或等于此值,它们将被视为同一直线的一部分。
"""

import cv2  
import numpy as np  
  
# 读取图像  
image= cv2.imread('../image/pc2.jpg')
  
# 转换为灰度图像  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
  
# 使用Canny边缘检测  
edges = cv2.Canny(gray, 50, 150)  
  
# 使用概率霍夫变换检测线段  
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)  

# 在原图像上绘制检测到的线段  
for line in lines: 
    print('------------') 
    print(line)
    x1, y1, x2, y2 = line[0]  
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  
  
# 显示图像  
cv2.imshow('Detected Lines', image)  
cv2.waitKey(0)  
cv2.destroyAllWindows()