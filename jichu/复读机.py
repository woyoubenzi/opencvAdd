import cv2
import numpy as np
import matplotlib.pyplot as ptl

img=cv2.imread('../image/coins.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 二值化处理(大津算法进行二值化),THRESH_BINARY_INV使黑白颜色翻转
ret,thresh= cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV| cv2.THRESH_OTSU)

# (开运算)发现二值化后的图片,存在毛边和一些噪点
ken= cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
opening= cv2.morphologyEx(thresh,cv2.MORPH_OPEN,ken,iterations=1)

# 显示
cv2.imshow('imp',thresh)
#cv2.imshow('img',np.hstack((dst_open)))
#cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()