import cv2
import numpy as np

"""
FLANN(Fast Library for Approximate Nearest Neighbors)是一个用于快速计算近似最近邻的库。在面对大数据时优于暴力特征匹配

主要特点：
多种算法支持: FLANN 提供了多种最近邻搜索的算法,包括 KD 树、KMeans 树、线性搜索等。这些算法可根据数据集的特性和搜索需求进行选择。
高维数据处理: FLANN 能够高效地处理高维数据,适用于图像、文本等领域中的特征向量。
配置灵活: 用户可以配置 FLANN 的参数以满足不同的需求,例如搜索的近似程度和算法的选择

特征匹配记录下目标图像与待匹配图像的特征点,并根据特征点集合构造特征量,对这个特征量进行比较,筛选,最终得到一个匹配点的映射集合.
我们也可以根据这个集合的大小来衡量两幅图片的匹配程度

cv2.FlannBasedMatcher(index_params)
index_params字典: 匹配算法KDTREE,LSH,SIFT和SURF使用KDTREE算法,OBR使用LSH算法
sezrch_params字典:指定KDTREE算法中遍历树的次数,如KDTREE设为5,那么搜索次数设为50

Flann中除了普通的match方法,还有knnMatch方法
-多个参数K: 表示取欧式距离最近的前K个关键点
"""

# 读取两张图片
img1 = cv2.imread('../image/opencv.jpg')
img2 = cv2.imread('../image/opencvtxt.jpg')

# 将图片转换为灰度图
#gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 创建SIFT特征检测对象
sift = cv2.SIFT.create()

# 计算图像的SIFT描述子
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# 创建FLANN匹配器对象，设置算法和搜索参数
index_params = dict(algorithm=0, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# 使用FLANN匹配器进行特征匹配
matches = flann.match(des1, des2)

# 绘制特征匹配
result = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)

# 展示图片
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',900,900)
cv2.imshow('img', result)
cv2.waitKey(0)
cv2.destroyAllWindows()