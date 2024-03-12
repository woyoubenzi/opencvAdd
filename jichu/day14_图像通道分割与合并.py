import cv2
import numpy as np
"""
分割图像通道，融合通道，堆叠展示图像
"""

# 创建一个长宽200,3通道的图像
img=np.zeros((200,200,3),np.uint8)

# 分割图像的通道
b,g,r=cv2.split(img)

# 修改通道颜色
"""
b 是一个NumPy数组，通常代表图像中的蓝色通道。
[10:100, 10:100] 是一个切片操作，表示对数组的部分区域进行切片。
具体而言，它选择了数组中行的索引从10到99（不包括100），列的索引从10到99（不包括100）的区域。
=255 是对切片区域进行赋值，将该区域的所有元素的值设置为255（255表示最大强度，即白色）。
"""
b[10:100,10:100]=255
g[10:100,10:100]=255
print("img",img)

# 合并通道
img2=cv2.merge((b,g,r))
print("img2",img2)
# 展示图片
#cv2.imshow("img",img2)

# 堆叠展示图片(维度不同不能放一起)
cv2.imshow("img",np.hstack((b,g)))
cv2.imshow("img2",np.hstack((img,img2)))

cv2.waitKey(0)