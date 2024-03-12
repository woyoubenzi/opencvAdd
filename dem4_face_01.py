import face_recognition
import cv2

"""
开摄像头，读取摄像头拍视到的画面
定位到画面中人的脸部，并用绿色的框框把人脸框住
top,right,bottom,left [(30,90,45,100)]
"""

# 1 打开摄像头。由于摄像头可能有多个，这里选择第一个
vide_capture = cv2.VideoCapture(0)
# 2 无限循环获取摄像头拍摄的画面，并做进一步处理
while True:
    # 2.1 获取摄像头拍摄的画面（会得到两个对象）
    ret,frame= vide_capture.read() # frame 摄像头所拍摄的画面 ret 布尔值，代表能否获取到画面
    # 2.2 从画图中提取人脸所在区域(列表) 元素是这样的： [(30,90,45,100)]
    face_location=face_recognition.face_locations(frame)
    # 2.3 循环遍历人脸部所在的区域，并画框
    for top,right,bottom,left in face_location:
        # 2.3.1 在人像所在区域画框（画面，点位1，点位2，颜色，线条宽度）
        cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
    # 2.4 通过opencv把画面展示出来,并把画面取名Video
    cv2.imshow("Video",frame)
    # 2.5 设定按Q退出while循环，退出程序的这样一个机制
    if cv2.waitKey(1) & 0xFF==ord('Q'):
        break
# 3 退出程序，释放摄像头或其他资源
vide_capture.release()
cv2.destroyAllWindows()