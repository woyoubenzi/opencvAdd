import cv2
import numpy as np

"""
我们获取到图像特征点和描述子之后,可以将两幅图进行特征匹配
BF(Brute-Force)暴力特征匹配方法,通过枚举的方式进行特征匹配
暴力匹配器很简单.它使用第一组(即第一幅图像)中一个特征的描述子,并使用一些距离计算将其与第二组中的所有其他特征匹配.返回最接近的一个

cv2.BFMatcher(nprmType,crossCheck)
normType: 计算距离的方式
1.NORM_L1,L1距离,即绝对值,SIFT和SURF使用
2.NORM_L2,L2距离,(默认值)即平方,SIFT和SURF使用
3.NORM_L1,汉明距离,ORB使用
crossCheck: 是否进行交叉匹配,默认False

使用match函数进行特征点匹配,返回的对象为DMatch对象,该对象具有以下属性:
DMatch.distance-描述符之间的距离.越低越好
DMatch.trainldx-训练描述符中描述符的索引
DMatch.queryldx-查询描述符中描述符的索引
DMatch.imgldx-训练图像的索引

match方法返回一个包含所有匹配结果的列表。
knnMatch方法返回每个查询特征点的k个最近邻匹配,可以通过比值测试或其他筛选方法来进一步选择合适的匹配。

关于距离:
L1距离又称为曼哈顿距离,它是两点在坐标系上的绝对差值的和.
L2距离又称为欧几里得距离,它是两点在坐标系上的直线距离.
汉明距离是用于衡量两个等长字符串之间的差异性的度量.它表示将一个字符串变为另一个所需的最小位翻转次数.

这些距离度量在不同的应用中有不同的用途:
L1和L2距离通常用于连续数据,如图像处理,机器学习中的特征相似性等.
汉明距离通常用于衡量两个二进制序列之间的相似性,例如在编码,错误检测和纠正等领域.
"""
# 读取图片
img1=cv2.imread('../image/opencv.jpg')
img2=cv2.imread('../image/opencvtxt.jpg')

gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# 创建特征检测对象
sift=cv2.SIFT.create()

# 计算,关键点,描述子
kp1,des1=sift.detectAndCompute(img1,None)
kp2,des2=sift.detectAndCompute(img2,None)

# 构建暴力匹配器
bf=cv2.BFMatcher(cv2.NORM_L1)
"""
match匹配,返回值的结构(<1>,<2>,<3>,<4>)
"""
# 进行match匹配描述子
match=bf.match(des1,des2)
# print("type",type(match))
# print("len",len(match))
# print("distance",match[0].distance) # 表示两个特征点之间的距离或相似度
# print("queryIdx",match[1].queryIdx) # 第一张图的描述子
# print("trainIdx",match[1].trainIdx) # 第二张图的描述子

# 绘制特征匹配
#result= cv2.drawMatches(img1,kp1,img2,kp2,match,None)
"""
knnMatch匹配,返回值的结构((<1>,<2>),(<3>,<4>),(<5>,<6>))
"""
# 除了match,还有knnMatch(多个K,一般值=2)
knnMatch=bf.knnMatch(des1,des2,2)
print("type",type(knnMatch))
print("len",len(knnMatch))

good=[]
# 人为调整匹配到描述子
for m,n in knnMatch:
    # 设定阈值,距离小于对方距离的0.7倍(这个值可调整)
    if m.distance<0.6*n.distance:
        good.append(m)

# 专门用来画knnMatch匹配结果的
result=cv2.drawMatchesKnn(img1,kp1,img2,kp2,[good],None)

# 展示图片
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',900,900)
cv2.imshow('img', result)
cv2.waitKey(0)
cv2.destroyAllWindows()