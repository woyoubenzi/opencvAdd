import cv2
"""
颜色空间切换
"""
# 创建一个回调函数
def callback(value):
    #pass:省略方法
    pass

cv2.namedWindow('color',cv2.WINDOW_NORMAL)
cv2.resizeWindow('color',480,640)

# opencv读取的图片默认是BGR的色彩空间
img=cv2.imread('../face_database/boss.jpg')

# 定义颜色空间(定义不同颜色空间)
# 所有颜色空间的转换都是COLOR开头,RGBA，A代表不透明度
colorspaces=[
    cv2.COLOR_BGR2RGBA,
    cv2.COLOR_BGR2BGRA, # 原图
    cv2.COLOR_BGR2GRAY, # 灰度图
    cv2.COLOR_BGR2HSV,
    cv2.COLOR_BGR2YUV
]

# 设置回调函数callback
cv2.createTrackbar('trackbar','color',0,4,callback)

while True:
    # 获取trackbar的值
    index=cv2.getTrackbarPos('trackbar','color')

    # 进行颜色空间的转换
    cvt_img=cv2.cvtColor(img,colorspaces[index])

    cv2.imshow('color',cvt_img)
    k= cv2.waitKey(1)
    if k==ord('Q'):
        break

cv2.destroyAllWindows()