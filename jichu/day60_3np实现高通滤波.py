"""
此文件仅展示高通滤波器操作,低频同理

低频,高频
低频对应图像内变换缓慢的灰度分量.例如:在一幅大草原的图像中,低频对应着广袤的颜色趋于一致的草原.
高频对应图像内变换快速的灰度分量,是由灰度的尖锐过度造成的.例如:在一幅大草原的图像中,其中狮子的边缘等信息

衰减高频而通过低频,是低通滤波器 效果是模糊一幅图像
衰减低频而通过高频,是高通滤波器 效果是增强尖锐的细节,但是会导致图像的对比度降低

[滤波器]
接受(通过)或拒绝一定频率的分量
通过低频的滤波器称为低通滤波器
通过高频的滤波器称为高通滤波器

[频域滤波]
修改傅里叶变换以达到特殊目的,然后计算IDFT返回到图像域
特殊目的:图像增强,图像去噪,边缘检测,特征提取,压缩加密等
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img=cv2.imread('../image/lena.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 傅里叶变换
f=np.fft.fft2(gray)
fshift=np.fft.fftshift(f)
# 高通滤波器去除低频,将低频变成0
rows,cols=gray.shape # 获取原始图宽高
crow,ccol=int(rows/2),int(cols/2) # 裁剪出低频区
fshift[crow-30:crow+30,ccol-30:ccol+30]=0 # 将低频区变为0
# 傅里叶逆回来(原图)
ifshuft=np.fft.ifftshift(fshift)
io=np.fft.ifft2(ifshuft)
io=np.abs(io)

# 显示
plt.subplot(121)
plt.imshow(gray,cmap='gray')
plt.title('one')
plt.axis('off')
plt.subplot(122)
plt.imshow(io,cmap='gray')
plt.title('two')
plt.axis('off')
plt.show()