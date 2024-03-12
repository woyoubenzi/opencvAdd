import cv2
import numpy as np
"""
可手动调节的进度条，回调函数
"""
# 创建可改变大小的窗口(WINDOW_NORMAL)
cv2.namedWindow('trackbar',cv2.WINDOW_NORMAL)
# 分辨率
cv2.resizeWindow('trackbar',640,480)
# 定义回调函数
def callback(value):
    # 接受用户自定义的RGB值，并在控制台显示
    print(value)

# 创建trackbar 进度条名称，窗口名称，从0到255，回调函数
cv2.createTrackbar('R','trackbar',0,255,callback)
cv2.createTrackbar('G','trackbar',0,255,callback)
cv2.createTrackbar('B','trackbar',0,255,callback)

# 创建一个背景图
img=np.zeros((480,640,3),np.uint8)

while True:
    # 获取当前trackbar的值
    r = cv2.getTrackbarPos('R','trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')

    # 改变背景图颜色
    img[:] =[b,g,r]
    # 展示图像
    cv2.imshow('trackbar',img)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break


cv2.destroyAllWindows()