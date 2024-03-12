"""
opencv实现傅里叶变换

[dft语法]
cv2.dft() 函数是 OpenCV 库中用于进行离散傅里叶变换(DFT)的函数
dft = cv2.dft(src, flags=0, nonzeroRows=0)
src: 输入图像,它应该是一个单通道、浮点型的数组(即浮点数矩阵)。在对图像应用cv2.dft()之前,通常需要将图像的数据类型转换为np.float32。
flags: 转换的标志。这些标志可以控制转换的方向（正向或逆向）、尺寸、以及优化算法等。一些常用的标志包括：
--cv2.DFT_COMPLEX_OUTPUT: 输出一个复数数组。如果没有设置这个标志,输出的数组将只包含结果的实部。
--cv2.DFT_REAL_OUTPUT: 在进行逆变换时使用,表示输出是实数。
--cv2.DFT_INVERSE: 执行逆DFT。
--cv2.DFT_SCALE: 在执行逆变换时,通过结果数组的大小来缩放结果。这个标志通常与cv2.DFT_INVERSE结合使用。
nonzeroRows: 如果这个值不为0,函数会假设只有nonzeroRows行包含非零值,这可以进一步加快变换速度。在大多数情况下,这个参数都是默认的0,意味着所有的行都会被处理。

返回结果=cv2.dft(原始图像,转换标识)
返回结果: 双通道,第一个通道是结果的实数部分,第二个通道是结果的虚数部分
原始图像: 输入的图像首先转换成np.float32格式. np.float32(img)
转换标识: flags=cv2.DFT_COMPLEX_OUTPUT,输出一个复数阵列

[magnitude语法]
cv2.magnitude()函数是OpenCV库中用于计算向量的幅度的函数。
在处理图像时,特别是在进行傅里叶变换(DFT)或梯度计算之后,我们经常得到包含两个分量的复数或向量。

magnitude = cv2.magnitude(x, y)
返回结果=cv2.magnitude(参数1,参数2)
计算幅度值
参数1: 浮点型X坐标值,也就是实部
参数2: 浮点型Y坐标值,也就是虚部
magnitude: 输出数组,包含与输入数组(x和y)同样尺寸的幅度值
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img=cv2.imread('../image/lena.png',0)
# 读取的图片是ndarray,但是傅里叶变换需要float32位数据
img_float32 = np.float32(img)
# 进行离散傅里叶变换,得到一个双通道的数据
dft=cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
# 将低频从左上角移动到中心
dshift=np.fft.fftshift(dft)
# 设定返回值为0-255之间,用于图像显示(magnitude计算幅度值(绝对值),log计算自然对数)
result=20*np.log(cv2.magnitude(dshift[:,:,0],dshift[:,:,1]))

# 显示原始图像和幅度谱
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image')
plt.subplot(122), plt.imshow(result, cmap='gray')
plt.title('result')
plt.show()