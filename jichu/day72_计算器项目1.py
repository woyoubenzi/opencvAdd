import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

class Button:
    # 初始化按钮的属性
    def __init__(self, pos, width, height, value):
        # 按钮位置
        self.pos = pos
        # 按钮宽度
        self.width = width
        # 按钮高度
        self.height = height
        # 按钮显示的值
        self.value = value

    # 在画布上绘制按钮
    def draw(self, img_or):
        # 绘制按钮的主体，填充为白色
        cv2.rectangle(img_or, (self.pos[0], self.pos[1]), (self.pos[0] + self.width, self.pos[1] + self.height), (255, 255, 255), -1)
        # 绘制按钮的边框，颜色为黑色
        cv2.rectangle(img_or, (self.pos[0], self.pos[1]), (self.pos[0] + self.width, self.pos[1] + self.height), (0, 0, 0), 2)
        # 在按钮上显示其值
        cv2.putText(img_or, self.value, (self.pos[0] + 20, self.pos[1] + 65), cv2.FONT_HERSHEY_COMPLEX, 2, (50, 50, 50), 2)

    # 检查是否点击了按钮
    def check_click(self, x, y, img):
        # 判断点击的坐标是否在按钮区域内
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            # 绘制点击特效，显示在按钮上方
            #cv2.rectangle(img, (self.pos[0], self.pos[1] - 10), (self.pos[0] + self.width, self.pos[1] - 5), (0, 255, 0), -1)
            return True
        else:
            return False

# 打开摄像头
cap = cv2.VideoCapture(0)
# 设置摄像头分辨率
cap.set(3, 1280)
cap.set(4, 720)

# 定义按钮布局
button_values = [['7', '8', '9', '*'],
                 ['4', '5', '6', '-'],
                 ['1', '2', '3', '+'],
                 ['0', '/', '.', '=']]
button_list = []
# 创建按钮实例并添加到列表中
for y in range(4):
    for x in range(4):
        x_pos = x * 100 + 800
        y_pos = y * 100 + 150
        button = Button((x_pos, y_pos), 100, 100, button_values[y][x])
        button_list.append(button)

# 创建手势检测器
detector = HandDetector(maxHands=1, detectionCon=0.9)
# 初始化表达式变量
my_equation = ""
# 用于标记按钮是否已被按下
button_pressed = False

# 主循环
while True:
    flag, img = cap.read()
    if flag:
        # 将图像翻转以创建镜像效果
        img_or = cv2.flip(img, 1)
        # 检测手部
        hands, img_or = detector.findHands(img_or, flipType=False)
        point1=None
        point2=None
        if hands:
            # 获取手指的坐标列表
            lmlist = hands[0]['lmList']
            # 获取食指和中指的坐标
            point1 = tuple(lmlist[8][:2])
            point2 = tuple(lmlist[12][:2])
            # 计算两指之间的距离
            length, _, img_or = detector.findDistance(point1, point2, img_or)

            x, y = point1
            # 判断是否点击按钮
            if length < 40 and not button_pressed:
                for button in button_list:
                    if button.check_click(x, y, img_or):
                        my_value = button.value
                        # 处理按钮点击逻辑
                        if my_value == '=' and my_equation:
                            try:
                                my_equation = str(eval(my_equation))
                            except:
                                my_equation = "Error"
                        elif my_value in '0123456789' or (my_value in '/*-+.' and my_equation and my_equation[-1] not in '/*-+.'):
                            my_equation += my_value
                        button_pressed = True  # 标记为已点击
                        break
            elif length > 80:
                button_pressed = False  # 重置点击状态

        # 绘制所有按钮
        for button in button_list:
            button.draw(img_or)

        # 绘制食指和中指的连线
        cv2.line(img_or, point1, point2, (0, 255, 0), 2)

        # 绘制显示计算结果的区域
        cv2.rectangle(img_or, (800, 70), (1200, 170), (225, 225, 225), -1)
        cv2.rectangle(img_or, (800, 70), (1200, 170), (50, 50, 50), 3)
        # 显示当前表达式或结果
        cv2.putText(img_or, my_equation, (810, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)

        # 显示图像
        cv2.imshow('img', img_or)
        key = cv2.waitKey(1)
        if key == ord('Q'):
            break
        elif key == ord('C'):
            # 清除表达式
            my_equation = ''

    else:
        print('摄像头打开失败')
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()