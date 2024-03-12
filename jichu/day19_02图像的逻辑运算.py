import cv2
import numpy as np

# 创建2张黑色背景的图片
img=np.zeros((200,200),np.uint8)
img2=np.zeros((200,200),np.uint8)

# 指定区域内的像素值为255(纯白)
img[20:120,20:120]=255
img2[80:180,80:180]=255

# 白色区域的非
new_img=cv2.bitwise_not(img,img2)

# 白色区域的与
#new_img=cv2.bitwise_and(img,img2)

# 白色区域的或
#new_img=cv2.bitwise_or(img,img2)

# 白色区域的异或
#new_img=cv2.bitwise_xor(img,img2)

cv2.imshow('new_img',np.hstack((img,img2,new_img)))
cv2.waitKey(0)
cv2.destroyAllWindows()