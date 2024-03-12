import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
车辆识别(简易版,有漏洞)
"""
# 打开摄像头
#cap=cv2.VideoCapture(0)

# 打开视频
cap=cv2.VideoCapture('../image/bus2.mp4')
# 创建背景减除算法对象
mog=cv2.createBackgroundSubtractorMOG2()
gsoc= cv2.bgsegm.createBackgroundSubtractorGSOC()
# 创建卷积核
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# 计算外接矩形的中心点
def center(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=int(x)+x1
    cy=int(y)+y1
    return cx,cy
# 阈值(用于过滤非汽车的物体)
min_w=60
min_h=50
# 检测线位置
line_high=600
# 检测线的偏移量
offset=8
# 车的空列表
cars=[]
# 车辆计数
carno=0
# 循环读取视频
while True:
    ret,frame=cap.read()
    if ret==True:
        # 把原始帧进行灰度化,然后去噪
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 去除视频中微小的噪点
        blur=cv2.GaussianBlur(gray,(5,5),5)
        # 背景减除
        fgmask=mog.apply(blur)
        # 腐蚀掉非汽车的物体
        erode=cv2.erode(fgmask,kernel)
        # 腐蚀后车变小了,尝试膨胀回来
        dialte=cv2.dilate(erode,kernel,iterations=2)
        # 闭运算消除内部的噪点,小物体
        close= cv2.morphologyEx(dialte,cv2.MORPH_CLOSE,kernel)
        # 查找汽车轮廓
        contours,_= cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # 画出汽车检测线
        cv2.line(frame,(10,line_high),(1250,line_high),(255,255,0),3)
        # 画出所有检测出来的轮廓
        for contour in contours:
            # 最大外接矩形
            x,y,w,h=cv2.boundingRect(contour)
            # 通过判断框的大小,来过滤掉小的框
            is_valid=(w>=min_w)&(h>=min_h)
            if not is_valid:
                continue
            # 能走到这一步都算正常的车
            # 在原图上画出矩形(坐标点都是整数)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            # 把车抽象为一点，即外接矩形的中心点
            # 要通过外接矩形计算矩形的中心点(车的中心)
            cpoint= center(x,y,w,h)
            # 将过去的车添加到集合中
            cars.append(cpoint)
            cv2.circle(frame,(cpoint),5,(0,255,0),-1)

            # 判断汽车是否过检测线
            for (x,y) in cars:
                if y>(line_high-offset) and y<(line_high+offset):
                    # 有效检测
                    carno+=1
                    cars.remove((x,y))
                    print(carno)
        # 显示标题
        cv2.putText(frame,'Vehicle Count:'+str(carno),(500,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
        # 显示处理后的图像
        cv2.imshow('video',close)
        # 显示原的图像
        cv2.imshow('frame',frame)
    
    # 图片为0,视频为1
    key=cv2.waitKey(100)
    # 用户按esc退出
    if key==27:
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()