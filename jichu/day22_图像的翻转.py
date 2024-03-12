import cv2
"""
图像的翻转
语法  cv2.flip(src,flipCode)
· flipCode=0 上下翻转
· flipCode>0 左右翻转
· flipCode<0 上下+左右
"""
dog=cv2.imread('../image/cat.png')

# 上下翻转
dog_up=cv2.flip(dog,flipCode=0)
# 左右翻转
dog_left=cv2.flip(dog,flipCode=1)
# 上下+左右
dog_up_left=cv2.flip(dog,flipCode=-1)

cv2.imshow('dogup',dog_up)

cv2.waitKey(0)
cv2.destroyAllWindows()