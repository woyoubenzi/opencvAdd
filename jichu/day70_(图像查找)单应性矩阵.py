import cv2
import numpy as np

"""
单应性(Homography)变换:可以简单理解为它用来描述物体在世界坐标系和像素坐标系之间的位置映射关系
(最少要有4个点 len(特征点)>=4)
retval, mask = cv2.findHomography(srcPoints, dstPoints, method=0, ransacReprojThreshold=3.0, mask=None, maxIters=None, confidence=None, refineIters=None)
参数: 
srcPoints: 源图像中的坐标矩阵,可以是CV_32FC2类型,也可以是vector <pointf>类型
dstPoints: 目标图像中的坐标矩阵,可以是CV_32FC2类型,也可以是vector <pointf>类型
method: 计算单应性矩阵的方法,有多种选择,默认为0。
1-0: 利用所有点的常规算法
2-RANSAC: (一般用这个算法多)基于RANSAC的鲁棒算法,Random Sample Consensus,随机抽样一致性
3-LMEDS: 最小中值鲁棒算法
4-PROSAC: 基于PROSAC的鲁棒算法
ransacReprojThreshold: 将点对视为内点的最大允许重投影错误阈值(仅用于RANSAC和RHO方法).若srcPoints和dstPoints是以像素为单位的,则该参数通常设置在1到10的范围内.
mask: 输出的掩码矩阵,,通常有鲁棒算法(RANSAC或LMEDS)设置.注意,输入掩码矩阵是不需要设置的。
maxIters: RANSAC算法的最大迭代次数,默认为2000。
confidence: RANSAC算法的置信度。
返回值: 
retval: 返回计算得到的3x3的单应性矩阵。
mask: RANSAC算法中用于标记内点和外点的掩码矩阵。

cv2.perspectiveTransform() 是 OpenCV 库中的一个函数，用于执行透视变换
cv2.perspectiveTransform(src, M)
src: 一个包含原始图像上点坐标的数组
M: 透视变换矩阵，用于将原始图像中的点映射到目标图像中的对应点。
函数的返回值是一个包含目标图像上点坐标的数组
"""

# 读取两张图片
img1 = cv2.imread('../image/opencvtxt2.jpg')
img2 = cv2.imread('../image/opencvtxt.jpg')

# 灰度化
g1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
g2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# 创建特征检测器
sift=cv2.SIFT.create()

# 计算特征点和描述子
kp1,des1=sift.detectAndCompute(g1,None)
kp2,des2=sift.detectAndCompute(g2,None)

# 创建特征匹配(这里用fiann)
index_params=dict(algorithm=1,trees=5)
search_params=dict(checks=50)
fiann= cv2.FlannBasedMatcher(index_params,search_params)

# 对描述子进行特征匹配
matches= fiann.knnMatch(des1,des2,k=2)

# 通过goods把特征点找到
goods=[]
for(m,n) in matches:
    # 阈值一般是0.7到0.8之间.
    if m.distance<0.8*n.distance:
        goods.append(m)

# 计算单应性矩阵需要4个点
if len(goods)>=4:
    # 这里是python列表推导公式
    # kp1[m.queryIdx]拿到KP1中特征点的坐标
    src_points=np.float32([kp1[m.queryIdx].pt for m in goods]).reshape(-1,1,2)
    dst_poingts=np.float32([kp2[m.trainIdx].pt for m in goods]).reshape(-1,1,2)

    # 根据匹配上的关键点去计算单应性矩阵
    H,_= cv2.findHomography(src_points,dst_poingts,cv2.RANSAC,5)

    # 通过单应性矩阵,计算小图(img1)在大图中对应的位置
    h,w=img1.shape[:2]
    # 将列表转换成ndary类型
    pts= np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0]]).reshape(-1,1,2)
    # 透视变换
    # cv2.warpPerspective()只能对图片进行透视变换,无法用于pts
    dst= cv2.perspectiveTransform(pts,H)
    # 在大图中,把dst画出来(在这里dst需要转换为整数)
    cv2.polylines(img2,[np.int32(dst)],True,(0,0,255),2)
else:
    # 没有找到足够的特征点
    print('not enough porint number to compute homeography matrix')
    exit()

# 画图匹配的特征点
ret=cv2.drawMatchesKnn(img1,kp1,img2,kp2,[goods],None)
# 展示图片
cv2.namedWindow('ret',cv2.WINDOW_NORMAL)
cv2.resizeWindow('ret', 580, 520)
cv2.imshow('ret', ret)
cv2.waitKey(0)
cv2.destroyAllWindows()