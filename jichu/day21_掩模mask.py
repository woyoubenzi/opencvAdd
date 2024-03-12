# 1 引入图片
# 2 设计logo
# 3 规划logo位置，背景色
# 4 利用add方法，把图片叠加在一起
"""
掩码/掩模(mask),设计logo
"""
import cv2
import numpy as np

# 读取图片
dog=cv2.imread('../image/cat.png')

# 查看读取到图片的长宽
print(dog.shape)

# 创建一个符合原图的黑色背景的logo
logo=np.zeros((200,200,3),np.uint8)

# 绘制logo
logo[20:120,20:120]=[0,0,255] # 红
logo[80:180,80:180]=[0,255,0] # 绿


# 掩码(抠图用)
mask=np.zeros((200,200),np.uint8)
mask[20:120,20:120]=255 # 白
mask[80:180,80:180]=255 # 白

# 将掩码颜色翻转
m=cv2.bitwise_not(mask)

# 选择添加logo的位置
roi=dog[100:300,100:300]

# roi与roi进行与运算还是roi,然后再和mask做与运算
# 如果与mask运算的结果是T，则返回原图，F则返回0(纯黑)
tmp=cv2.bitwise_and(roi,roi,mask=m)

# add合并两个图片
dst=cv2.add(logo,tmp)

# 在dog上还原
dog[100:300,100:300]=dst

# 显示图片
cv2.imshow('dog',roi)

cv2.waitKey(0)
cv2.destroyAllWindows()