import cv2
import numpy as np

"""
高斯滤波
要理解高斯滤波首先要知道什么是高斯函数,高斯函数是符合高斯分布(正态分布)的数据的概率密度函数
高斯函数的特点是以X轴某一点(这一点称为均值)为对称轴,越靠近中心数据发生概率越高,最终形成一个两边平缓,中间陡峭的钟型(有的地方也叫帽子)图形
高斯滤波就是使用符合高斯分布的卷积核对图片进行卷积操作,所以高斯滤波的重点就是如何计算符合高斯分布的卷积核,即高斯模板
我们可以观察到越靠近中心,数值越大,符合高斯分布的特点

cv2.GaussianBlur(src,ksize,sigmaX,dst,sigmaY,borderType)
ksize 高斯核的大小
sigmaX X轴的标准差
dst 输出图像,通常可以设置为 None,函数会自动创建一个新的图像来存储结果。
sigmaY Y轴的标准差,默认为0,这时sigmaY=sigmaX
borderType 边界类型.这个参数决定了如何处理图像边缘。

如果没有指定sigma值,会分别从ksize的宽度核高度中计算sigma
选择不同的sigma值会得到不同的平滑效果,sigma越大,平滑效果越明显
没有指定sigma时,ksize越大,平滑效果越明显
"""
# 导入图片
img=cv2.imread('../image/blue.png')

# 高斯滤波
# 优点:去除噪声，图像平滑，边缘保留，图像金子塔
# 缺点:图像模糊
dst= cv2.GaussianBlur(img,(5,5),sigmaX=50)

# 展示
cv2.imshow('lena',np.hstack((img,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()

