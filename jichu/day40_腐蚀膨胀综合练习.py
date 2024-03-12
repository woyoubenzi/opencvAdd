import cv2
import numpy as np
"""
因为二值只能对黑白(灰度)图进行操作
我这张图片是白底黑字,卷积核是白色。所以要把图片转换为黑底白字
先腐蚀掉触须,这时文字就变小了。然后膨胀到原来的大小。
这样一张只去掉触须,又不影响大小的图片就出来了
"""
# 读取图像，确保为二值(灰度)图像
img = cv2.imread('../image/zhangsan.png', cv2.IMREAD_GRAYSCALE)

# 进行非操作,改变黑白
new_img=cv2.bitwise_not(img)

# 结构元素（卷积核）
kernel = np.ones((5, 5), np.uint8)

# 进行腐蚀操作
dste = cv2.erode(new_img, kernel, iterations=1)

# 对腐蚀后的图像进行膨胀操作
dst=cv2.dilate(dste,kernel,iterations=1)

# 显示原始图像和腐蚀后,膨胀的图像
#cv2.imshow('xy', np.hstack((new_img,dste,dst)))
cv2.imshow('xy', np.hstack((new_img,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()