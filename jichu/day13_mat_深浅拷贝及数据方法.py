# mat
import cv2
import numpy as np
import copy
"""
mat(维度，行列，位深，通道),转换为ndarray对象，深浅拷贝(复制)

opencv是用Mat这种数据结构来表示图片的
c++中是用mat来保存图片，python中把mat转化成了numpy的ndarray
"mat" 对象指的是 OpenCV 中的 Mat 对象，而不是 Python 中的 ndarray 对象。
mat由header和data组成,header中记录了图片的维数，大小，数据类型等数据
OpenCV 的 Mat 对象是一种专门用于图像处理的数据结构，而 Python 的 ndarray 对象是 NumPy 库中用于表示多维数组的数据结构。
"""
# Mat属性
"""
dims:维度
rows:行数
cols:列数
depth:像素的位深
channels:通道数RBG是3
size:矩阵的大小
type:dep+dt+chs CV_8UC3(深度+数据类型+通道数 OpenCV图片_8位 无符号 三通道)
data:存放数据的内存地址
"""
# (ai)演示了如何将OpenCV中的Mat对象转换为NumPy的ndarray对象
"""
import cv2
import numpy as np

# 读取图像，得到OpenCV中的Mat对象
img_mat = cv2.imread('example.jpg')

# 将Mat对象转换为NumPy的ndarray对象
img_np = np.array(img_mat)

# 现在img_np是一个NumPy的ndarray，可以利用NumPy的功能进行处理
print("NumPy数组的形状:", img_np.shape)
print("NumPy数组的数据类型:", img_np.dtype)

"""

# 读取一张图片
img=cv2.imread('../face_database/boss.jpg')

# 对一个包含两个元素的元组 (2,3) 进行深拷贝，赋给 ones
ones=np.copy((2,3))
print(ones.data) # <memory at 0x000002A7DBFFB4C0> 内存地址

# 创建一个形状为 (2, 3) 的全为 1 的 NumPy 数组
ones = np.ones((2, 3))

# 元素的总个数****
print(img.size)

# 数据类型****
print(img.dtype)

# 维度：宽，高，通道数****
print(img.shape)

# 返回图像中每个像素值的字节大小, 通常是1，因为每个像素占用1个字节
print(img.itemsize)

# 返回数组的维度数，对于图像来说，通常是3。这是因为图像是一个三维数组，包含高度、宽度和通道数。
print(img.ndim)

# 虚拟数组
print(img.imag)

"""
因为python中图片数据已经包装成ndarray了,所以对mat的深浅拷贝，其实就是对ndarray深浅拷贝
浅拷贝就是源数据发生变化后，拷贝数据也会发生变化；深拷贝是完全复制一份
"""

# 浅拷贝
img2=img.view()

# 深拷贝
img3=img.copy()

# 给数据源img添加一个红色图块
img[10:100,10:100]=[0,0,255]

# 横向堆叠显示
cv2.imshow('img',np.hstack((img,img2,img3)))

# 竖向堆叠显示
#cv2.imshow('img',np.vstack((img,img2,img3)))

cv2.waitKey(0)
cv2.destroyAllWindows()