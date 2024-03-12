"""
获得图像和灰度图像的差分

"""

import cv2
import datetime

# 默认摄像头
camera=cv2.VideoCapture(0)
# 存储第一幅图像
background=None
# 把画面做了一个膨胀
es=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,4))

while True:
    # 持续读取摄像头画面
    grabbed,frame=camera.read()
    # 把画面转换成灰度图像
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 高斯滤波消除噪点
    gray_frame=cv2.GaussianBlur(gray_frame,(25,25),3)
    # 当background为空时，传入灰度图像的值，并跳过这次循环
    if background is None:
        background=gray_frame
        continue
    # 求背景图和灰度图的差
    diff=cv2.absdiff(background,gray_frame)
    # 设置差多少算不同
    diff=cv2.threshold(diff,50,255,cv2.THRESH_BINARY)[1]
    # 形态学膨胀
    diff=cv2.dilate(diff,es,iterations=3)

    # 画面，展示文字，展示位置，字体，字大小，颜色，字体粗细
    cv2.putText(frame,"Motion:Undetected",(10,10),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    # 画面，当前时间.格式化，展示位置，字体，字大小，颜色，字体粗细
    cv2.putText(frame,datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10,frame.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX,
                0.35,(0,255,0),1)

    # 名称，画面
    cv2.imshow('video',frame)
    # 展示差分图像
    cv2.imshow("diff",diff)

    # 按Q退出循环
    key =cv2.waitKey(1) & 0xFFf
    if key==ord('Q'):
        break

# 退出
camera.release()
cv2.destroyAllWindows()