"""
获得图像
"""

import cv2
import datetime

# 默认摄像头
camera = cv2.VideoCapture(0)

while True:
    # 持续读取摄像头画面
    ret, frame = camera.read()

    # 画面，展示文字，展示位置，字体，字大小，颜色，字体粗细
    cv2.putText(frame, "Motion: Undetected", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # 画面，当前时间.格式化，展示位置，字体，字大小，颜色，字体粗细
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)

    # 名称，画面
    cv2.imshow('video', frame)

    # 按Q退出循环
    key = cv2.waitKey(1) & 0xFF
    if key == ord('Q'):
        break

# 退出
camera.release()
cv2.destroyAllWindows()