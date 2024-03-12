import cv2
import numpy as np

"""
查找轮廓findContours

contours, hierarchy = cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]])
返回值:
contours: 轮廓的列表,每个轮廓是一个点集。
hierarchy: 轮廓的层次结构(层级),通常用不到,可以不指定。
参数说明:
image:输入的二值图像,通常是通过阈值处理或边缘检测得到的二值图像。
mode:轮廓检索模式,指定轮廓的提取方式。常用的有:
1-cv2.RETR_EXTERNAL(或者0):只提取最外层的轮廓。
2-cv2.RETR_LIST(或者1):提取所有轮廓,不建立等级关系。
3-cv2.RETR_CCOMP(或者2):提取所有轮廓,并将其组织为两层的层次结构。每层最多两级,从小到大,从里到外
4-cv2.RETR_TREE(或者3):提取所有轮廓,并重构轮廓之间的整个层次结构。按树型储存轮廓,从小到大,从右到左。人容易理解，最为方便

method:轮廓逼近方法,指定轮廓的近似方法。常用的有:
1-cv2.CHAIN_APPROX_NONE:存储所有的轮廓点,不进行逼近。
2-cv2.CHAIN_APPROX_SIMPLE:压缩水平、垂直和对角线方向上的部分,只保留端点。(比如四边形，只保留四个点)
3-cv2.CHAIN_APPROX_TC89_L1:使用 Teh-Chin 链逼近算法。

contours:输出的轮廓列表,每个轮廓是一个点集,可以通过索引访问单个轮廓。
hierarchy:可选参数,用于存储轮廓的层次结构,通常用不到。
offset:可选参数,每个点的偏移量,通常用不到。
"""

# 导入图片
img = cv2.imread('../image/lun.png')

# 变成单通道黑白图像
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)

# 全局二值化,返回两个东西，一个阈值,一个二值化后的图
thresh,binary=cv2.threshold(new_img,150,255,cv2.THRESH_BINARY)

# 查找轮廓，返回两个东西，轮廓，层级
contours,hierarchy= cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# 查看轮廓的数量
num_contours = len(contours)

# contours是元组，元组内的元素才是ndarray类型，每一个ndarray表示一个contours
print("轮廓类型",type(contours))
print("轮廓",contours)
print("层级",contours)
print("轮廓数量",num_contours)


# 显示
cv2.imshow('img',img)
cv2.imshow('new_img',new_img)
cv2.imshow('binary',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()