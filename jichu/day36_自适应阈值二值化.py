import cv2
import numpy as np

"""
前面部分我们使用的是全局阈值,整幅图像采用同一个数作为阈值。
这种方法并不适应于所有情况,尤其是当同一副图像上的不同部分具有不同亮度时,这种情况下我们需要采用自适应阈值
此时的阈值是根据图像上每一个小区域计算与其对应的阈值。
因此在同一幅图像上的不同区域采用的是不同的阈值,从而使我们能在亮度不同的情况下得到更好的结果

cv2.adaptiveThreshold(src,maxValue,adaptiveMethod,thresholdType,blockSize,C,dst=None)
这种方法需要我们指定6个参数,返回值只有一个
src: 输入图像,应该是灰度图像。
maxValue: 当像素值高于阈值时,给予的新值。
adaptiveMethod: 指定计算阈值的方法,有两个选项:
1-cv2.ADAPTIVE_THRESH_MEAN_C:阈值取自相邻区域的平均值。
2-cv2.ADAPTIVE_THRESH_GAUSSIAN_C:阈值取自相邻区域的加权和,权重为一个高斯窗口。
thresholdType: 阈值类型,有四个选项：
1-cv2.THRESH_BINARY: 当像素值高于阈值时,给予的新值是 maxValue,否则是 0。
2-cv2.THRESH_BINARY_INV: 当像素值高于阈值时,给予的新值是 0,否则是 maxValue。
3-cv2.THRESH_TRUNC: 当像素值高于阈值时,给予的新值是阈值,否则保持不变。
4-cv2.THRESH_TOZERO: 当像素值高于阈值时,保持不变,否则是 0。
blockSize: 奇数,用来计算阈值的区域大小,它决定了邻域的大小。
C: 这是一个常数,阈值等于相邻区域平均值或加权平均值减去这个常数。
"""

# 因为光线问题，全局二值化导致有部分看不见了，这时就需要自适应阈值二值化

# 导入图片
img=cv2.imread('../image/lookbook.jpg')

# 二值化操作是对灰度图像操作,需要将img变成灰度图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 自适应阈值只有一个返回值
dst=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,0)

# 尝试去噪
#gauss=cv2.medianBlur(dst,7)
gauss=cv2.GaussianBlur(dst,(3,3),100)

# 展示
cv2.namedWindow('xy',cv2.IMREAD_GRAYSCALE)
cv2.resizeWindow('xy',1920,1080)

cv2.imshow('xy',np.hstack((gray,dst,gauss)))
cv2.waitKey(0)
cv2.destroyAllWindows()