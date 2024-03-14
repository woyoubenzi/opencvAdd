"""
此文件仅展示低通滤波器操作,高频同理

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

# 图像
img=cv2.imread('../image/lena.png',0)
# 进行傅里叶变换
dft=cv2.dft(np.float32(img),None,cv2.DFT_COMPLEX_OUTPUT)
# 将低频移动到图形中间
dshift=np.fft.fftshift(dft)
# 创建掩码，用于过滤高频分量
rows, cols = img.shape
mask = np.zeros((rows, cols, 2), np.uint8)
crow, ccol = rows // 2, cols // 2
# 指针,值越大掩膜区域越大,保留的空间域就越大
i=30
mask[crow-i:crow+i, ccol-i:ccol+i] = 1  # 选择一个中心区域作为掩码
# 应用掩码
md=dshift*mask
# 将空域还原成时域
imd=np.fft.ifftshift(md)
io=cv2.idft(imd)
io=cv2.magnitude(io[:,:,0],io[:,:,1])

# 显示
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.subplot(122)
plt.imshow(io,cmap='gray')
plt.show()