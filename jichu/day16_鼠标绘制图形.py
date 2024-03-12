import cv2
import numpy as np

"""
结合控制鼠标和绘图实现用鼠标绘制图形

按下a进入直线绘制模式
按下s进入矩形绘制模式
按下d进入圆形绘制模式
"""


# 创建全局标准，判断画什么类型的图
curshape=0
startpos=(0,0)

# 创建黑色背景图
img=np.zeros((480,640,3),np.uint8)

# 获取鼠标轨迹并画图的方法
def mouse_callbace(event,x,y,flags,userdata):
    # 引入全局变量
    global curshape,startpos
    print(curshape)
    # 当鼠标按下时
    if event==cv2.EVENT_LBUTTONDOWN:
        # 记录起始位置
        startpos=(x,y)
    # 当鼠标释放时
    elif event==cv2.EVENT_LBUTTONUP:
        if curshape==0:
            # 直线
            cv2.line(img, startpos, (x,y), (255, 0, 255), 3)
            cv2.imshow('mvv', img)
        elif curshape==1:
            # 矩形
            cv2.rectangle(img, startpos, (x,y), (0, 0, 255), 3)
            cv2.imshow('mvv', img)
        elif curshape==2:
            # 圆
            a = (x - startpos[0])
            b = (y - startpos[1])
            # 画圆时半径必须是整数
            r = int((a**2+b**2)**0.5)
            cv2.circle(img, startpos,r,(0,255,255),3)
            cv2.imshow('mvv', img)
        else:
            print('暂不支持其他按键')


# 创建窗体
cv2.namedWindow('mvv',cv2.WINDOW_NORMAL)

# 设置鼠标回调函数
cv2.setMouseCallback('mvv',mouse_callbace)

while True:
    #cv2.imshow('mvv', img)
    # 检测键鼠操作
    key=cv2.waitKey(0)
    if key==ord("q"):
        break
    elif key==ord("a"):
        curshape = 0
    elif key==ord("s"):
        curshape = 1
    elif key==ord("d"):
        curshape = 2

cv2.destroyAllWindows()
