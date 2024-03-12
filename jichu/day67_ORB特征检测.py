import cv2
import numpy as np

"""
ORB(Oriented FAST and Rotated BRIEF)是一种快速特征点提取和描述的算法.
ORB算法分两部分,特征点提取和特征的描述.
特征提取是由FAST算法发展来的
特征点描述是根据BRIEF特征描述算法改进的
ORB特征是将FAST特征点的检测方法和BRIEF特征描述子结合起来,并在他们原来的基础上做了改进与优化.
ORB算法最大的优势是可以做到实时检测
ORB的劣势是检测准确率略有下降
ORB是开源的算法,SIFT和SURF都被申请了专利 
"""
# 读取图片
img=cv2.imread('../image/chess.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 创建ORB对象
orb=cv2.ORB.create()

"""
方法1
"""

# 进行检测
kp=orb.detect(gray)

# 计算描述子
kp,des=orb.compute(img,kp)
# ORB算法的描述子只有32维向量
print(des.shape)
"""
方法2
"""
# 也可以一步到位得到关键点和描述子
kp,des=orb.detectAndCompute(img,None)

# 绘制关键点
cv2.drawKeypoints(gray,kp,img)

# 展示图片
cv2.imshow('ORB', img)
cv2.waitKey(0)
cv2.destroyAllWindows()