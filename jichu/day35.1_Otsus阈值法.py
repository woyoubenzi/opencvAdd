import cv2

"""
Otsu's 阈值法(Otsu's Thresholding)是一种自适应阈值选择方法,它通过最大化类间方差来确定图像的二值化阈值。这个方法由日本学者Otsu于1979年提出,因其简单而有效而广泛应用于图像处理领域。

Otsu's 阈值法的核心思想是寻找一个阈值,使得在该阈值处,图像的两个类别(通常是前景和背景)之间的方差最大。在直观上,方差越大,表示两个类别的差异越明显,因此选择这个阈值能够最好地将图像分为两个部分。

算法步骤如下：

1.计算图像的直方图(histogram)和归一化直方图。
2.遍历所有可能的阈值(0到255),对每个阈值计算类间方差(between-class variance)。
3.选择使类间方差最大的阈值作为最优阈值。

Otsu's 阈值法适用于具有双峰直方图的图像,即图像包含明显的前景和背景。这种方法可以有效地处理不同光照条件下的图像,并自适应地选择合适的阈值。
"""

image = cv2.imread('../image/cat.png', cv2.IMREAD_GRAYSCALE)

# 应用Otsu's 阈值法
ret, threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 限制窗体大小,原图太大了
cv2.namedWindow('xy',cv2.WINDOW_NORMAL)
cv2.resizeWindow('xy',900,1000)
cv2.namedWindow('xyx',cv2.WINDOW_NORMAL)
cv2.resizeWindow('xyx',900,1000)
# 展示
cv2.imshow('xyx', image)
cv2.imshow('xy', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()