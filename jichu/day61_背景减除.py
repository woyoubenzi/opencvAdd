import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
背景减除
cv2.BackgroundSubtractorMOG2
这是一个以混合高斯模型为基础的前景/背景分割算法
他使用K(K=3或5)个高斯分布混合对背景像素进行建模。使用这些颜色(在整个视频中)存在时间的长短作为混合的权重。背景颜色一般持续的时间最长,而且更加静止
移动的物体会被标记为白色,背景会被标记为黑色
"""
# 打开摄像头
cap=cv2.VideoCapture(0)

# 背景减除算法(两种)
mog=cv2.createBackgroundSubtractorMOG2()
gsoc=cv2.bgsegm.createBackgroundSubtractorGSOC()
while True:
    ret,frame=cap.read()
    if ret==True:
        # 有图像就显示这一帧
        fgmask=mog.apply(frame)
        cv2.imshow('video',fgmask)
    
    # 图片为0,视频为1
    key=cv2.waitKey(1)
    # 用户按esc退出
    if key==27:
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()