import time
import cv2
import numpy as np
import math
"""
利用时间差来查看程序运行速度
"""
# time
# 1.如何利用opencv库函数进行测试时间
# 2.如何提高代码性能 tips

t1=time.time()

e1=cv2.getTickCount() #返回时钟数

src=cv2.imread('../image/tur.png')

cv2.imshow('src',src)

e2=cv2.getTickCount() #返回时钟数

t2=time.time()
tall=t2-t1
print("这是",tall)
fre= cv2.getTickFrequency() # 返回时钟计数频率，每秒的时钟数

timeall=(e2-e1)/fre

print("整个运行时间",timeall)
cv2.waitKey(0)
cv2.destroyAllWindows()