import cv2
import numpy as np

"""
腐蚀操作也是用卷积核扫码图像,只不过腐蚀操作的卷积核一般为1。假如卷积核内所有像素点都是白色,那么锚点即为白色
腐蚀主要用于缩小或消除图像中物体的边界。它的基本思想是通过将结构元素沿图像边界移动,去除物体边界上的像素点,使物体整体缩小。

腐蚀的过程是这样的：对于图像中的每一个像素,结构元素（也称为卷积核）被放置在图像上,只有当结构元素完全覆盖图像中的物体时,
中心像素才保持不变,否则它将被置为背景（通常是黑色）。这样,物体的边缘就被腐蚀掉了。

腐蚀的效果有助于去除小的细节、减小物体的尺寸、分离连接的物体等。
在二值图像中,腐蚀操作可以将物体的边界腐蚀掉,使物体更加紧凑。在灰度图像中,腐蚀操作可以降低物体的亮度。

语法:cv2.erode(src, kernel, iterations=None, anchor=None, borderType=None, borderValue=None)
src: 输入图像,通常是二值图像（黑白图像）,可以是灰度图像或彩色图像。
kernel: 结构元素（卷积核）,定义了腐蚀操作的形状。它通常是一个矩形或椭圆的形状,使用 np.ones 函数创建。
iterations: 可选参数,表示腐蚀操作的迭代次数。默认为1。
anchor: 可选参数,结构元素的锚点,默认为结构元素的中心。
borderType: 可选参数,指定边界模式,默认为 cv2.BORDER_CONSTANT。
borderValue: 可选参数,指定边界值,当 borderType 为 cv2.BORDER_CONSTANT 时使用,默认为0。
"""
# 腐蚀会让图片上的物体会变小

# 读取图像，确保为二值(灰度)图像
img = cv2.imread('../image/zhangsan.png', cv2.IMREAD_GRAYSCALE)

# 进行非操作,改变黑白(因为目前的卷积核是白色的,只会腐蚀白色区域)
new_img=cv2.bitwise_not(img)

# 定义腐蚀的结构元素（卷积核）
kernel = np.ones((5, 5), np.uint8)

# 进行腐蚀操作(iterations腐蚀1次)
dst = cv2.erode(new_img, kernel, iterations=1)

# 显示原始图像和腐蚀后的图像
cv2.imshow('xy', np.hstack((new_img,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()