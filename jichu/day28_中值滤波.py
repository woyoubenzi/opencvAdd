import cv2
import numpy as np

"""
中值滤波
cv2=medianBlur()
原理:假设有一个数组[1556789],使其从小到大依次排列,取中间值(即中位数)作为卷积后的结果值即可,中值滤波对胡椒噪音(椒盐噪音)效果明细
"""

 # 导入噪声图片
img=cv2.imread('../image/blue.png')

# 中值滤波
dst=cv2.medianBlur(img,15)
# 展示
cv2.imshow('lena',np.hstack((img,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()