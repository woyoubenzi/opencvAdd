import cv2
"""
视频的写入，读取，播放
"""
# 打开第一个摄像头
cap =cv2.VideoCapture(0)

# 保存视频的格式，*mp4v就是解包操作，等同于'm','p','4','v'
fourcc=cv2.VideoWriter.fourcc(*'mp4v')


"""
cv2.VideoWriter 创建一个视频写入对象
例子 vw=cv2.VideoWriter('outpur.mp4',fourcc,20,(640,480))
'outpur.mp4':输出视频文件的名称
fourcc：视频压缩格式
120 帧率
(640,480) 分辨率
vw.write(frame) 编码并写入缓存(避免有同名文件)
cap.release() 缓存写入磁盘，并释放资源
"""
# (640,480)是摄像头拍视频的默认分辨率，这个大小搞错了也不行
# 主要是这个分辨率
vw=cv2.VideoWriter('outpur.mp4',fourcc,120,(640,480))

# 通过摄像头是否打开来显示视频
while cap.isOpened():
    # 读取到画面
    ret,frame=cap.read()

    if not ret:
        print('error')
        break

    # 将frame读取到的帧写入文件
    vw.write(frame)

    # 播放
    cv2.imshow('frame',frame)

    if cv2.waitKey(1)==ord('Q'):
        break

# 释放摄像头
cap.release()
# 用于释放 cv2.VideoWriter 对象占用的资源
vw.release()
# 用于关闭所有通过 OpenCV 创建的窗口
cv2.destroyAllWindows()