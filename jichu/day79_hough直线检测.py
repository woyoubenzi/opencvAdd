"""
霍夫(hough)变换-直线检测功能

[语法]
lines = cv2.HoughLines(image, rho, theta, threshold)
image: 需要进行霍夫变换的输入图像,通常是二值化的图像（边缘检测之后）。
rho: 霍夫空间中表示距离的精度,以像素为单位。一般情况下,rho 可以取 1 像素。
theta: 霍夫空间中表示角度的精度,以弧度为单位。一般情况下,theta 可以取 np.pi/180,这样可以覆盖从 0 到 180 度的所有角度。
threshold: 累加器阈值参数,只有累加器中的值高于这个阈值时,才会被认为是一条直线。这个参数的值越高,返回的直线数量越少,反之亦然。
返回值 lines 是一个 N x 1 x 2 的数组,其中 N 是检测到的直线的数量。每条直线都由 (rho, theta) 表示,rho 表示距离,theta 表示角度。

除了检测直线外,霍夫变换也可以用于检测其他形状.
"""
import cv2
import numpy as np

# read
img= cv2.imread('../image/pc2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 边缘检测
edges=cv2.Canny(gray,100,140)
cv2.imshow('edges',edges)
# 霍夫变换检测直线
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# 绘制直线
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        # 在原图上画直线
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# show
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()