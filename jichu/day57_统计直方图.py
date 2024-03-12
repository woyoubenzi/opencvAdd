import cv2
import numpy as np

"""
opencv统计直方图
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
images: 输入的图像,可以是单张图像或图像列表。
channels: 需要统计的通道,如果输入图像是灰度图,则设置为 [0]；如果是彩色图像,可以设置为 [0] 表示灰度通道,[0, 1, 2] 表示 RGB 三个通道。
mask: 可选的掩码图像,用于限制计算直方图的区域。
1-统计整幅图像的直方图,设为None
2-统计图像某一部分的直方图时,需要掩码图像
histSize: 指定每个通道的直方图分 bin 的数量,以列表形式提供,例如 [256] 表示每个通道有 256 个 bin。
ranges: 指定每个 bin 的范围,通常为 [0, 256]。
hist: 输出的直方图。如果提供了这个参数,计算的直方图将被存储在这里。
accumulate: 可选参数,默认为 False。如果设置为 True,则直方图在多个图像上累积。
"""

# 获取图像
img = cv2.imread('../image/lena.png')

# 统计直方图
hist=cv2.calcHist([img],[0],None,[256],[0,255])

print(hist)
print(hist.size)
print(hist.shape)