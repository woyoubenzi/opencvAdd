import cv2
import numpy as np
"""
filter2D-通用的卷积操作函数,可以使用自定义的卷积核对图像进行卷积操作。

语法:filter2D(src,ddepth,kernel[,dst[,anchor[,delta[,borderType]]])
ddepth是卷积之后图片的位深,即卷积之后图片的数据类型,一般设为-1,表示和原图类型一致.
kernel是卷积核大小,用元组或者ndarray表示,要求数据类型必须是float型
anchor锚点,即卷积核的中心带,是可选参数,默认是(-1,-1)
delta可选参数,表示卷积之后额外加的一个值,相当于线性方程中的偏差,默认是0
borderType边界类型,一般不设置
"""
# 导入图片
img= cv2.imread("../image/blue.png")
# 卷积核大小
ken=(5,5)
"""
方盒滤波-是一种特殊的平均滤波方法,使用一个正方形矩阵作为卷积核,所有元素的值相等,通常为1,然后对整个矩阵进行归一化。

cv2.boxFilter(src,ddepth,ksize,dst,anchor,normalize,borderType)
normalize:标准化
normalize=True时,a=1/(W*H) a=滤波器的宽高
normalize=False时,a=1
一般使用normalize=True,这时方盒滤波等价于均值滤波
方盒滤波的卷积核形式如下：
"""
# 主要作用是对图像进行平均滤波,使图像变得更加平滑
# 不用手动创建卷积核,只需要告诉方盒滤波卷积核的大小
dst= cv2.boxFilter(img,-1,ken,normalize=False)
"""
均值滤波-均值滤波是一种平滑图像的基本滤波方法,使用一个卷积核对图像进行卷积操作,卷积核的每个元素都相等,通常为1。

blur(src,ksize,dst,anchor,borderType)
"""
# 与方盒滤波类似，均值滤波的目的是降低图像中的噪声，使图像更加平滑
# 不用手动创建卷积核,只需要告诉方盒滤波卷积核的大小。
dst1=cv2.blur(img,ken)
"""
结果展示
"""
cv2.imshow('img',np.hstack((img,dst,dst1)))
cv2.waitKey(0)
cv2.destroyAllWindows()
