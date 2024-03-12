"""
获得图像和灰度图像的差分
探测到动的图像
并发送到手机
"""

import cv2
import datetime
import dem5_wx_notic2 as dm

# 默认摄像头
camera=cv2.VideoCapture(0)
# 存储第一幅图像
background=None
# 把画面做了一个膨胀
es=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,4))
# 标识符，记录有无发送过通知
is_send_msg=False

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
    diff=cv2.threshold(diff,100,255,cv2.THRESH_BINARY)[1]
    # 形态学膨胀
    diff=cv2.dilate(diff,es,iterations=3)

    # findContours发现图像中有多少个连续物体
    contours,hierarchy=cv2.findContours(diff.copy(),cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
    # 是否有动的物体
    is_datected=False
    for c in contours:
        if cv2.contourArea(c)<2000:
            # 物体小于2000像素的跳过检测
            continue
        # 通过boundingRect拿到物体的坐标
        (x,y,w,h)=cv2.boundingRect(c)
        # 画框，参数：图像，左上角点位，右下角点位，颜色粗细
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        # 有动的物体
        is_datected=True

        if not is_send_msg:
            is_send_msg=True
            wx_tools=dm.WxTools("wx6c83f1dba496bfbb","f8817f4987903dab5e4b33a9fd7dea75")
            wx_tools.send_wx_customer_msg("oYMly6SiLaR2TedvAKJ7D3GoxoZQ","有物体闯入摄像区，请留意")

    # 活体探测判断
    if is_datected:
        show_text="Motion:Detected"
        show_color=(0,0,255)
    else:
        show_text = "Motion:Undetected"
        show_color = (0, 255, 0)
    # 左上角画面：画面，展示文字，展示位置，字体，字大小，颜色，字体粗细
    cv2.putText(frame,show_text,(10,10),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,show_color,2)

    # 左下角画面：画面，当前时间.格式化，展示位置，字体，字大小，颜色，字体粗细
    cv2.putText(frame,datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10,frame.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX,
                0.35,show_color,1)

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