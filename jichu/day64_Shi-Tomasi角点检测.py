import cv2
import numpy as np
"""
Shi-Tomasi角点检测是Harris角点检测的改进
Harris角点检测计算的稳定性与K有关,而K是一个经验值,不太好设定最佳的K值
Shi-Tomasi发现,角点的稳定性其实和矩阵M的较小特征值有关,于是直接用较小的那个特征值作为分数,这样就不用调整K值了
-Shi-Tomasi将分数公式改为如下形式R=min(入1入2)
-和Harris一样,如果该分数大于设定的阈值,我们就认为他是一个角点

corners= cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, corners=None, mask=None, blockSize=None, useHarrisDetector=None, k=None)
参数说明:
image:输入图像,通常是灰度图像。
maxCorners:角点的最大数,为0表示无限制
qualityLevel:角点的最低质量水平,取值范围为 0 到 1,表示角点响应的最小值。(小于1.0的整数,一般在0.01-0.1之间)
minDistance:角之间最小欧式距离,忽略小于此距离的点(避免太近的角点被重复检测)
corners:可选参数,输出的角点坐标,可以是一个 numpy 数组。
mask:可选参数,表示感兴趣区域的掩码。如果提供了掩码,只有在掩码内的区域才进行角点检测。
blockSize:可选参数,表示角点检测时的邻域大小。(检测窗口大小)
useHarrisDetector:可选参数,如果为 True,则使用 Harris 角点检测器,如果为 False,则使用 Shi-Tomasi 角点检测器。
k:可选参数,Harris 角点检测器的自由参数,当 useHarrisDetector=True 时使用
返回值:
corners:包含检测到的角点的数组。
"""
img=cv2.imread('../image/chess.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# shi-tomasi角点检测
corners= cv2.goodFeaturesToTrack(gray,maxCorners=0,qualityLevel=0.01,minDistance=10)
print(type(corners))
print(corners)
print(corners.shape)
# 需要转换为int型
corners= np.intp(corners)
# 画出角点
for i in corners:
    # 将二维数据变1维,即角点的坐标点
    x,y= i.ravel()
    cv2.circle(img,(x,y),3,(255,0,0),-1)

#
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()