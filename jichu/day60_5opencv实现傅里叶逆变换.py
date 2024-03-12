"""
[语法]
dft(src, dst=None, flags=None, nonzeroRows=None) 傅里叶变换
idft(src, dst=None, flags=None, nonzeroRows=None) 傅里叶逆变换
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

# 读图
img=cv2.imread('../image/lena.png',0)

# 傅里叶变换
dft=cv2.dft(np.float32(img),None,cv2.DFT_COMPLEX_OUTPUT)
# 将低频移动到图形中间
dshift=np.fft.fftshift(dft)

# 傅里叶逆变换
idshift=np.fft.ifftshift(dshift)
idft=cv2.idft(idshift)

# 转换为图像可显示格式
idft=cv2.magnitude(idft[:,:,0],idft[:,:,1])

# 显示
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.subplot(122)
plt.imshow(idft,cmap='gray')
plt.show()