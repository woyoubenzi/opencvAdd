import cv2
import matplotlib.pyplot as mp
import numpy as np
"""
显示图像(颜色默认按RGB排列)，matplotlib中展示
语法 cv2.imshow()
参数:要加载的图像/视频

用matplotlib显示图片，和真实的图片不一样(颜色默认按BGR排列)
一般不要用这个方式读取图
语法 mp.imshow(img)
"""
# # 读取图片
# img= cv2.imread("C:/Users/MVV/Pictures/Camera Roll/hd1.webp")
# # 设置窗体大小
# cv2.namedWindow('img',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('img', 800, 600)
# # 展示图片
# cv2.imshow('img',img)
# # 等待按键暂停
# cv2.waitKey(0)
# # 关闭
# cv2.destroyAllWindows()

# 读取图片
img= cv2.imread("C:/Users/MVV/Pictures/Camera Roll/hd1.webp")

# 显示图片
cv2.imshow('start',img)

# 显示第一帧图片，输入任意字符后结束

# matplotlib中展示
#使用Matplotlib的imshow函数来显示图像
mp.imshow(img)
#设置标题为'ppppp'，并且不显示X轴和Y轴的刻度
mp.title('ppppp'),mp.xticks([]),mp.yticks([])
#显示Matplotlib图形窗口
mp.show()
k= cv2.waitKey(0)

# # matplotlib读取,显示,保存图
# china=mp.imread('../image/cat.png')
# mp.imshow(china)
# mp.imsave("china.png",china)
# mp.show()