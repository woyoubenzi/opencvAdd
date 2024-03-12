# ww
import cv2
import numpy as np
"""
按照具体数值缩放图像，按照比例缩放图像，查看对象大小

图像的放大缩小
resize(src,dsize[dst[fx[fy[interpolation]]]])
-src 要缩放的图片
-dsize 缩放之后的图像大小，元组和列表表示即可
-dst 可选，缩放之后的输出图片
-fx x轴缩放比，即宽度的缩放比
-fy y轴缩放比，即高度的缩放比
-interpolation 插值算法
  -INTER_NEAREST 邻近插值，速度快，效果差
  -INTER_LINEAR 双线性插值，使用原图中的4个点进行插值，默认是这个
  -INTER_CUBIC 三次插值，原图中的16个点
  -INTER_AREA 区域插值，效果最好，计算时间最长
"""

dog=cv2.imread('../face_database/boss.jpg')
cat=cv2.imread('../image/ali.jpg')

print(dog.shape)
print(cat.shape)
print("============原始大小==============")
# 使用resize将两张图像缩放成一样大
# OpenCV中dsize的值，是先输入宽度，再输入高度(1280,1440)
new_cat= cv2.resize(cat,(1280,1440))
new_dog= cv2.resize(dog,(1280,1440))

# 以dog为例,展示resize4种属性,4种插值算法
#new_dog1= cv2.resize(dog,(280,440),interpolation=cv2.INTER_NEAREST)
#new_dog2= cv2.resize(dog,(280,440),interpolation=cv2.INTER_LINEAR) # 默认效果
#new_dog3= cv2.resize(dog,(280,440),interpolation=cv2.INTER_CUBIC)
#new_dog4= cv2.resize(dog,(280,440),interpolation=cv2.INTER_AREA)

# 还可以按照x,y轴进行缩放，dsize=None表示不设置长宽，通过缩放处理
new_dog5=cv2.resize(dog,dsize=None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)  # 长宽缩短为原来的一半

print(new_dog.shape)
print(new_cat.shape)
print("============缩放大小==============")

# cv2.imshow('mvc',np.hstack((new_dog1,new_dog2,new_dog3,new_dog4)))
# cv2.imshow('mvv',np.hstack((new_dog,new_cat)))
cv2.imshow('mvd',new_dog5)
cv2.imshow('mve',dog)


cv2.waitKey(0)
cv2.destroyAllWindows()

# 查看对象大小，单位字节
print(cat.__sizeof__())
print(new_dog.__sizeof__())