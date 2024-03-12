"""
cv2.calcBackProject可以用来做直方图反向投影。它的参数与函数 cv2.calcHist 的参数基本相同。
"""
import cv2
import numpy as np

# 读取输入图像
img = cv2.imread('../image/lena.png')

# 将图像从 BGR 颜色空间转换到 HSV 颜色空间
# 这样做是因为 HSV 能够将图像的颜色信息（色调和饱和度）与亮度信息（值）分离
hsvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 计算 HSV 图像的直方图
# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# images：输入图像，指定为数组形式。
# channels：需要计算直方图的通道索引。例如，[0, 1]代表色调和饱和度。
# mask：遮罩图像。若计算整个图像的直方图，则为"None"。
# histSize：BIN的数量。需要为每个通道指定，对于色调和饱和度分别为[180, 256]。
# ranges：强度值的范围。对于色调和饱和度，范围分别是[0,180]和[0,256]。
roihist = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])

"""
 归一化：原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
#cv2.NORM_MINMAX 对数组的所有值进行转化，使它们线性映射到最小值和最大值之间
# 归一化之后的直方图便于显示，归一化之后就成了 0 到 255 之间的数了。
"""
# 规范化直方图
# cv2.normalize(src, dst[, alpha[, beta[, norm_type[, dtype[, mask]]]]]) → dst
# src：输入数组。
# dst：与src大小相同的输出数组。
# alpha：规范化到的范围下限或者是范围规范化的下限。
# beta：范围规范化的上限；对于规范化类型norm_type不使用。
# norm_type：规范化类型（cv2.NORM_MINMAX，cv2.NORM_L1，cv2.NORM_L2等）。
# dtype：当其为负时，输出数组与src类型相同；否则，它与src有相同数量的通道且深度为CV_MAT_DEPTH(dtype)。
# mask：可选的操作遮罩。
cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)

"""
# 此处卷积可以把分散的点连在一起
"""
# 执行直方图的反向投影
# cv2.calcBackProject(images, channels, hist, ranges, scale[, dst]) → dst
# images：输入图像，指定为数组形式。
# channels：计算反向投影的通道索引。
# hist：输入直方图，是反向投影的基础。
# ranges：直方图BIN的范围。
# scale：比例因子。
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

# 应用圆盘形卷积核
# cv2.getStructuringElement(shape, ksize[, anchor]) → retval
# shape：元素形状，可以是cv2.MORPH_RECT，cv2.MORPH_CROSS，cv2.MORPH_ELLIPSE。
# ksize：结构元素的大小。
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(dst, -1, disc, dst)

# 将反向投影的图像二值化
# cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
# src：输入数组（单通道，8位或32位浮点）。
# thresh：阈值。
# maxval：与cv2.THRESH_BINARY和cv2.THRESH_BINARY_INV阈值类型一起使用的最大值。
# type：阈值类型（cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV等）。
ret, thresh = cv2.threshold(dst, 50, 255, 0)
"""
别忘了是三通道图像，因此这里使用 merge 变成 3 通道
"""
# 合并通道形成彩色图像
# cv2.merge(mv[, dst]) → dst
# mv：要合并的输入数组或矩阵向量；所有的矩阵必须大小相同且深度相同。
thresh = cv2.merge((thresh, thresh, thresh))

# 对原图像和掩码进行按位与操作，提取颜色对象
# cv2.bitwise_and(src1, src2[, dst[, mask]]) → dst
# src1：第一个输入数组或标量。
# src2：第二个输入数组或标量。
# dst：与输入数组大小和类型相同的输出数组。
# mask：可选的操作遮罩，8位单通道数组，指定了要更改的输出数组的元素。
res = cv2.bitwise_and(img, thresh)

# 为显示目的，将原图像、阈值图像和结果图像水平堆叠
res = np.hstack((img, thresh, res))

# 显示最终的反向投影图像
cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()