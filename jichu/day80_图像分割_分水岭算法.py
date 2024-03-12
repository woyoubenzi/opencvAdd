"""
图像分割:将前景物体从背景中分离出来
图像分割为传统图像分割和基于深度学习的图像分割方法
传统图像分割就是使用opencv进行图像分割
传统分割的方法:分水岭发,GrabCut法,MeanShift法,背景扣除

分水岭算法

分水岭算法的灵感来自地理上的分水岭——即山脉分隔不同流域的边界。在图像处理中,可以将图像看作是一个地形表面,其中亮度高的区域可以视为山峰,亮度低的区域视为山谷。算法的目的是找到山谷的边界,从而实现图像的分割。

算法步骤通常包括:

图像预处理:可能包括灰度转换、噪声移除、边缘检测等,为分水岭算法准备图像。
确定标记:在图像的不同对象上放置不同的标记（例如,通过人工选择或自动算法如形态学运算）。
应用分水岭:OpenCV实现的分水岭算法会模拟水位上升过程,不同标记的区域会逐渐“淹没”直到水位达到山峰,标记之间的边界即为所求的分水岭。

dst = cv2.distanceTransform(src, distanceType, maskSize) 计算img中非零值到距离它最近的0值之间的距离
src:要处理的图像,8位单通道二值图像。
distanceType:计算距离的方式。常用的有cv2.DIST_L2、cv2.DIST_L1、cv2.DIST_C等。
maskSize:掩码大小。它决定了用于计算距离的邻域的大小。L1用3,L2用5
返回值:
dst: 与源图像大小相同的浮点型图像,其中的每个像素表示该点到最近零像素点的距离。

numLabels, labels = cv2.connectedComponents(image, connectivity, ltype)用于统计二值图像中所有连通域,用0标记背景,大于0的数标记其他对象
image: 8位单通道二进制图像。
connectivity: 可选,表示连通性。常用的是4或8,分别代表像素的4连通和8连通。
ltype: 输出标签图像的类型,默认是cv2.CV_32S。
返回值：
numLabels: 连通域的数量,包括背景。
labels: 一个与输入图像大小相同的数组,类型为ltype,其中每个元素的值对应其所属连通域的标签。

cv2.watershed(image, markers)分水岭算法 用于图像分割,特别适用于对象的边界不清晰的情况
image: 输入图像,8位3通道图像。
markers: 输入/输出的标记图像,单通道32位整数图像。与原始图大小相同的矩阵,表示那些是背景那些是前景
在函数调用前,应将其中的每个标记（即待分割对象的种子位置）设置为一个正整数,背景设为0,其他所有像素设为-1。
返回值：
函数没有返回值,但是markers图像会被修改,以包含结果。分水岭算法执行后,每个区域被标记为不同的正整数,边界区域被标记为-1。
"""
import cv2
import numpy as np
import matplotlib.pyplot as ptl

img=cv2.imread('../image/coins.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 显示ptl图
#_=ptl.hist(gray.ravel(),bins=256,range=[0,255])

# 二值化处理(大津算法进行二值化),THRESH_BINARY_INV使黑白颜色翻转
thresh,dst= cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV| cv2.THRESH_OTSU)

# (开运算)发现二值化后的图片,存在毛边和一些噪点
ken= cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dst_open= cv2.morphologyEx(dst,cv2.MORPH_OPEN,ken,iterations=2)

# 找出图中前景和背景
# 膨胀
big=cv2.dilate(dst_open,ken,iterations=2)
# 腐蚀
fg=cv2.erode(big,ken,iterations=2)

# 剩下的区域(硬币边界附近)不能确定是背景还是前景
# 可以通过膨胀之后的图减去腐蚀之后的图,得到未知区域的大小
unkown=cv2.subtract(big,fg)

# 因为硬币之间彼此是接触的,导致腐蚀之后的前景图不对(硬币之间形成了通道)
# 腐蚀在分水岭算法中不适合
# (分水岭步骤1)使用cv2.distanceTransform来确定前景图
dist_tran= cv2.distanceTransform(dst_open,cv2.DIST_L2,5)
#print(dist_tran[:10])
# 对dist_tran做归一化方便展示结果
cv2.normalize(dist_tran,dist_tran,0,1.0,cv2.NORM_MINMAX)

# 对dist_tran做二值化处理
_,fg= cv2.threshold(dist_tran,0.5*dist_tran.max(),255,cv2.THRESH_BINARY)
# 转换格式为:8位单通道图片
fg=np.uint8(fg)

# (分水岭步骤2)connectedComponents要求输入的图片是8位单通道图片,即单通道0-255的图片
_,labels=cv2.connectedComponents(fg)

# 因为watershed中认为1是不确定区域,1是背景,大于1的是前景
# labels+1把原来的0变1
labels=labels+1
# 从labels中筛选出位置区域,赋值为0
labels[unkown==255]=0

# 展示labels
labels_copy=labels.copy()
labels_copy1= np.uint8(labels_copy)
cv2.imshow('labels1',labels_copy1)
# 位置区域
labels_copy[labels==0]=150
labels_copy1= np.uint8(labels_copy)
cv2.imshow('labels2',labels_copy1)
# 背景
labels_copy[labels==1]=0
labels_copy1= np.uint8(labels_copy)
cv2.imshow('labels3',labels_copy1)
# 前景
labels_copy[labels>1]=255
labels_copy1= np.uint8(labels_copy)
cv2.imshow('labels4',labels_copy1)
labels_copy= np.uint8(labels_copy)


# 至此,我们的markers就已经生成好了
# watershed返回的数据已经做了修改,边界区域标记为-1了
markers=cv2.watershed(img,labels)
print(markers.min(),markers.max())

# 显示一下前景图片边缘
img[markers==-1]=[0,0,255]
# 显示
#ptl.show()
cv2.imshow('img',np.hstack((dst_open,big,fg,unkown,dist_tran,labels_copy)))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()