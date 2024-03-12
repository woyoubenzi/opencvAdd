""""""
"""
1-python的逻辑运算
^ 异或 204^213 结果是25
& 与  204&213 结果是196
| 或  204| 213 结果是221
~ 非  ~204 结果是-205 

2-opencv的逻辑运算 与或非 异或

2.0-与运算 (cv2.bitwise_and):
result_and = cv2.bitwise_and(img1, img2)
结果相当两个图像中对位的元素分别:img&img2

2.1-或运算 (cv2.bitwise_or):
result_or = cv2.bitwise_or(img1, img2)
结果相当两个图像中对位的元素分别:img|img2

2.2-非运算 (cv2.bitwise_not):
result_not = cv2.bitwise_not(img)
结果相当于每个元素值用255-像素值(只有这个和Python的逻辑运算不一样)

2.3-异或运算 (cv2.bitwise_xor):
result_xor = cv2.bitwise_xor(img1, img2)
结果相当两个图像中对位的元素分别:img^img2
"""
import cv2
import numpy as np

# 设置窗体
cv2.namedWindow('mvv',cv2.WINDOW_NORMAL)
cv2.resizeWindow('mvv',400,400)

# 读取图片
dog=cv2.imread('../image/ali.png') # 灰度
cat=cv2.imread('../image/ali.jpg') # 彩色

# 对比照片时使两张照片抱持一致
new_cat=cat[0:1440,0:2560]

print(cat.shape)
# 非操作(像素取反操作)
#cat_not=cv2.bitwise_not(new_cat)

# 与操作(两个图片要大小一致)

#cat_and=cv2.bitwise_and(new_cat,dog)

# 或操作
cat_or=cv2.bitwise_or(new_cat,dog)

# 异或
#cat_xor=cv2.bitwise_xor(new_cat,dog)

# 展示
cv2.imshow('mvv',np.hstack((new_cat,dog,cat_or)))
print(new_cat[:1,:1])
print('==============')
print(dog[:1,:1])
print('==============')
print(cat_or[:1,:1])

cv2.waitKey(0)
cv2.destroyAllWindows()