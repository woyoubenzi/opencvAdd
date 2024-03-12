import cv2
"""
摄像头，窗体,帧率解释
"""
# 打开摄像头（也可以用于打开视频）
cmm=cv2.VideoCapture(0)

# 静态图像可以用namedWindow来调整大小，视频和动态图像一般不用
# cv2.namedWindow('window',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('window',640,480)

# 判断摄像头是否打开成功
# 语法 cmm.isOpened() 返回值 bool

# 循环读取摄像头的每一帧
while cmm.isOpened():
    # 读一帧数据，返回标记和这一帧数据。True表示读到了数据，False表示没有读到数据
    ret,frame=cmm.read()

    # 画面设置
    frame=cv2.flip(frame,1) # 1水平镜像 -1垂直镜像

    # 如果没有读取到数据，直接退出
    if not ret:
        break

    # 滤波
    frame=cv2.medianBlur(frame,3)

    # 显示(图像，视频)
    cv2.imshow('window',frame)

    # 0是暂停接收用户键入后关闭显示，其他数字是多少毫秒后关闭显示，输入数字必须是整数
    # 假如一个视频是30帧，则输入1000//30，即1秒钟两张图间隔1000//30毫秒
    key=cv2.waitKey(1000//30)

    # 通过用户按键判断用户是否退出
    if key & 0xFF==ord('Q'):
        break


# 释放摄像头资源
cmm.release()
# 释放窗口资源
cv2.destroyAllWindows()