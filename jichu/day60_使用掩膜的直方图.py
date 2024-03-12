import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
复习:掩膜可以用来抠图
如何生成掩膜?
1-生成一个和原始图一样的黑色图片
2-将想要的区域通过索引方式设置为255
"""

# 读取三通道彩色图 
img = cv2.imread('../image/lena.png')
# 转为双通道灰度图
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 生成全黑的掩膜图像
mask=np.zeros(gray.shape,np.uint8)
# 设置想要统计直方图的区域
mask[200:400,200:400]=255

# 计算带掩膜直方图
hest_mask= cv2.calcHist([gray],[0],mask,[256],[0,255])
# 计算不带掩膜直方图
hest_gray= cv2.calcHist([gray],[0],None,[256],[0,255])
# 画matplotlib图
plt.plot(hest_mask,label='mask')
plt.plot(hest_gray,label='gray')
# 图例
plt.legend()
# 展示matplotlib图(直方图)
plt.show()

# 展示mask抠图效果
cv2.imshow('gray',gray)
cv2.imshow('mask',mask)
# gray与运算后还是gray,然后再和mask做与运算。mask黑色区域保留,白色区域变成gray
cv2.imshow('mask_gray',cv2.bitwise_and(gray,gray,mask=mask))
cv2.waitKey(0)
cv2.destroyAllWindows()