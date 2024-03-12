import cv2

"""
图像的旋转
语法:cv2.rotate(img,rotateCode)
POTATE_90_CLOCKWISE 90度顺时针旋转
POTATE_180 180度旋转
POTATE_90_COUNTERCLOCKWISE 90度逆时针旋转
"""

dog=cv2.imread('../image/cat.png')
# 90°旋转
new_dog = cv2.rotate(dog,rotateCode=cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('dog',new_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()