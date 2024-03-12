import cv2

"""
读取图像 彩色，灰度，alpha通道
语法 cv2.imread(图像地址,读取方式)
  图像地址：这个是图片的具体位置或图片，路径错误会返回None
  读取方式：cv2.IMREAD_COLOR 默认，以彩色模式读取,忽略透明度,也可以用1代替
          cv2.IMREAD_GRAYSCALE 以灰度模式读取,也可以用0代替
          cv2.IMREAD_UNCHANGED 包含alpha通道的加载图像模式,也可以用-1代替
"""
# 彩色
img=cv2.imread('../image/bur.jpg',cv2.IMREAD_COLOR)
imgs=cv2.imread('../image/tur.png',1)
print(img)
print(imgs)
print("===================")

# 灰度
img2=cv2.imread('../image/tur.png',cv2.IMREAD_GRAYSCALE)
imgs2=cv2.imread('../image/tur.png',0)
print(img2)
print(imgs2)
print("===================")

# 包含alpha通道
img3=cv2.imread('../image/tur.png',cv2.IMREAD_UNCHANGED)
imgs3=cv2.imread('../image/tur.png',-1)
print(img3)
print(imgs3)

