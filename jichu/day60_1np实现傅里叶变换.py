"""
傅里叶变换的作用
高频: 变换剧烈的灰度分量,列如边界
低频: 变换缓慢的灰度分量,列如一片大海

[滤波]
低通滤波器: 只保留低频,会使得图像模糊
高通滤波器: 只保留高频,会使得图像细节增强

[函数介绍]
numpy.fft.fft2() 实现傅里叶变换
它返回一个复数数组(complex ndarray)

numpy.fft.fftshift 将低频从左上角移到频谱中心

20*np.log(np.abs(fshift)) 设置频谱范围

cv2.dft() 是用来计算输入数组的离散傅立叶变换的函数。
它将输入的图像转换为频域表示,即将图像从空间域转换到频率域。
在频率域中,图像的特征以频率的形式表示,例如高频、低频成分等。
DFT 可以用于各种图像处理任务,例如频率域滤波、图像增强等。

cv2.idft() 是用于计算输入数组的逆离散傅立叶变换的函数。
它将频域表示的图像转换回空间域。
在空间域中,图像的特征以像素的形式表示。
IDFT 可以用于从频率域中重构图像,或者进行频率域滤波后的逆操作,以获得空间域的结果。

[语法]
dft(src, dst=None, flags=None, nonzeroRows=None)
idft(src, dst=None, flags=None, nonzeroRows=None)

src: 输入数组,通常是一个灰度图像（单通道）,可以是 8 位无符号整数或 32 位浮点数。
dst: 输出数组,用于存储 DFT 或 IDFT 的结果。如果为 None,则函数会自动创建一个与 src 大小相同的数组。
flags: 指定 DFT 或 IDFT 的行为标志。可以是以下标志的组合: 
cv2.DFT_COMPLEX_OUTPUT: 结果是一个复数数组。
cv2.DFT_SCALE: 结果进行缩放,使其幅度范围适合显示。
cv2.DFT_INVERSE: 进行逆 DFT,用于 cv2.idft() 函数。
cv2.DFT_ROWS: 进行逐行 DFT。
nonzeroRows: 当输入矩阵的行数不等于原始尺寸时,指定原始尺寸的行数。
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 获取灰度图
img=cv2.imread("../image/lena.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 进行傅里叶变换,得到一个复数数组
f=np.fft.fft2(gray)
# 将零频率分量移到频谱中心,返回值同样是一个复数数组
fftshift=np.fft.fftshift(f)
# 设定返回值为0-255之间,用于图像显示(abs计算绝对值,log计算自然对数)
result=20*np.log(np.abs(fftshift))


# 展示
plt.subplot(121)
plt.imshow(gray, cmap='gray')
plt.axis('on') # 是否显示网格
plt.title('Fourier gray')
plt.subplot(122)
plt.imshow(result, cmap='gray')
plt.axis('off') # 是否显示网格
plt.title('Fourier result')
plt.show()