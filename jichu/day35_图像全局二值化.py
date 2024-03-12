import cv2
import numpy as np

"""
二值化:将图像的每个像素变成两种值(比如0,255,代表黑色和白色,这两种值需要自定义)
retval, dst = cv2.threshold(src, thresh, maxval, type)
src: 输入图像,最好是灰度图像。
thresh: 阈值,用于确定二值化的分界线。
maxval: 如果某个像素值超过了阈值,它将被赋予的最大值。最大值不一定是255
type: 二值化操作的类型。这是一个枚举值,表示要执行的具体操作。在OpenCV中,常见的类型有: 
-cv2.THRESH_BINARY: 当像素值超过阈值时,将其设为maxval,否则设为0。
-cv2.THRESH_BINARY_INV: 当像素值超过阈值时,将其设为0,否则设为maxval。
-cv2.THRESH_TRUNC: 当像素值超过阈值时,将其设为阈值,否则保持不变。
-cv2.THRESH_TOZERO: 当像素值超过阈值时,保持不变,否则设为0。
-cv2.THRESH_TOZERO_INV: 当像素值超过阈值时,设为0,否则保持不变。
例如,如果你想要将图像二值化为黑白,可以使用cv2.THRESH_BINARY类型,maxval设置为1,这样像素值超过阈值的部分就会变成1,否则为0。
retval: 所使用的阈值。
dst: 经过阈值处理后的图像。
"""

# 导入图片
img=cv2.imread('../image/god.jpeg')

# 二值化操作是对灰度图像操作,需要将img变成灰度图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 注意threshold会返回两个值,(阈值,二值化处理后的图片)
thresh,dst= cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

# 展示
cv2.namedWindow('xy',cv2.IMREAD_GRAYSCALE)
cv2.resizeWindow('xy',1000,600)

cv2.imshow('xy',np.hstack((gray,dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()