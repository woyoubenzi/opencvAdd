import  cv2

"""
灰度图像有什么用？
   起到降维的作用，把一个像素点的表示数据从三个变成了一个，只丢失了颜色信息，这样计算机处理起来会更快
"""
# 把彩色图像转换为灰度图像，查看灰度图像在计算机中的展示

# 1 读取彩色图片
rgb_cat=cv2.imread("C:/Users/MVV/Pictures/Camera Roll/hd1.webp")
# 2 把彩色图片转换为灰度图片
#gray_cat= cv2.cvtColor(rgb_cat,cv2.COLOR_BGR2GRAY)
# 3 查看灰度图像的像素内容
#print(gray_cat)
# 4 查看灰度图片的维度
#print(gray_cat.shape)
"""
(1440, 2560)表示该图像数组有两个维度，第一个维度的大小为1440，第二个维度的大小为2560。
因此，该数组可以被视为一个1440行2560列的矩阵，
表示一个灰度图像，其中每个元素代表图像中的一个像素点的灰度值。
"""
# 5 保存灰度图像
#cv2.imwrite("image/ali.png",gray_cat)

# 5 保存彩色图像
cv2.imwrite("image/ali.jpg",rgb_cat)