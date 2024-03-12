import cv2
import numpy as np
"""
获取鼠标事件，创建纯黑图片
"""
"""
函数名可以随便取，参数必须是5个
event表示鼠标事件：0-11表示鼠标事件
x,y是鼠标坐标
flags表示鼠标的组合按键 快捷键+鼠标按键，也是用数字表示
"""
def mouse_callbace(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)
    print('=========分割线==========')

# 创建窗口
cv2.namedWindow('mouse',cv2.WINDOW_NORMAL)
# 宽度和高度
cv2.resizeWindow('mouse',(640,480))
# 设置鼠标回调函数
cv2.setMouseCallback('mouse',mouse_callbace,'123')
# 生产全黑的图片
img=np.zeros((480,640,3),np.uint8)

while True:
    cv2.imshow('mouse',img)
    key=cv2.waitKey(1)
    if key==ord('Q'):
        break


cv2.destroyAllWindows()
