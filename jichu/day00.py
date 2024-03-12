import cv2

"""
//这是马士兵教育的视频
namedWindow() 创建可命名窗口
resizeWindow() 改变窗口大小
imshow() 展示可命名窗口
destroyAllWindows() 摧毁窗口
waitKey() 暂停画面，等待用户按键
"""

# WINDOW_AUTOSIZE让窗口大小不可调节
# cv2.namedWindow('new',cv2.WINDOW_AUTOSIZE)

# WINDOW_AUTOSIZE让窗口大小可调节
cv2.namedWindow('new',cv2.WINDOW_NORMAL)
cv2.resizeWindow('new',980,980) # 修改窗口大小
cv2.imshow('new',0) # 显示窗口

# waitKey表示等待按键，0表示任何按键。其他整数表示等待按键的时间，单位毫秒，超时窗口会自动关闭
# waitKey会返回按键的ascii值
key=cv2.waitKey(0)

# ord()是计算ascii值的函数
if key & 0XFF==ord('Q'):
    print(key)

# 销毁所有窗口
cv2.destroyAllWindows()


