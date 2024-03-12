"""
获得图像和灰度图像

"""

import cv2
import datetime

# 默认摄像头
camera=cv2.VideoCapture(0)

while True:
    # 持续读取摄像头画面
    ret,frame=camera.read()
    # 把画面转换成灰度图像
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 高斯滤波消除噪点
    gray_frame=cv2.GaussianBlur(gray_frame,(25,25),3)

    # 画面，展示文字，展示位置，字体，字大小，颜色，字体粗细
    cv2.putText(frame,"Motion:Undetected",(10,10),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
    # 画面，当前时间.格式化，展示位置，字体，字大小，颜色，字体粗细
    cv2.putText(frame,datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10,frame.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX,
                0.35,(0,255,0),1)

    # 名称，画面
    cv2.imshow('video',frame)
    # 展示经过高斯滤波处理过的灰度图像
    cv2.imshow("diff",gray_frame)

    # 按Q退出循环
    key =cv2.waitKey(1) & 0xFFf
    if key==ord('Q'):
        break

# 退出
camera.release()
cv2.destroyAllWindows()