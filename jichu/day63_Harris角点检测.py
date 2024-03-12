import cv2

"""
Harris角点检测原理
图像|(x,y)|(x,y),当在点(x,y)(x,y)处平移(小三角形x,小三角形y)(小三角形x,小三角形y)后的自相似性:

dst = cv2.cornerHarris(src, blockSize, ksize, k, dst=None, borderType=None)
src:输入图像,灰度图像,数据类型为 float32。
blockSize:(检测窗口大小)表示邻域大小,用于角点检测。它是指计算导数时使用的邻域大小,一般为2。
ksize:Sobel(的卷积核) 求导核的大小,一般为3。
k:Harris(权重) 角点检测参数,取值范围一般为 0.04 到 0.06。
dst:可选参数,输出图像,数据类型为 float32,表示每个像素的角点响应。
borderType:可选参数,表示图像边界的处理方式。默认为 cv2.BORDER_DEFAULT
"""
# 获取图像
img = cv2.imread('../image/chess.png')

# 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 角点检测(每一个像素都能算出角点响应)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
print(gray.shape)  # 输出灰度图的形状
print(dst)  # 输出角点响应矩阵
print(dst.shape)  # 输出角点响应矩阵的形状
print(type(dst))  # 输出角点响应矩阵的数据类型

# 显示角点
# 设定最大阈值 dst.max()
img[dst > (0.01 * dst.max())] = [0, 0, 255]  # 将角点标记为红色

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
