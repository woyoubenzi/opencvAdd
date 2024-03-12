"""
模板匹配和卷积原理类似,模板在源图像上从原点开始滑动,计算模板与(图像被模板覆盖的地方)的差别程度
这个查别程度的计算方法在opencv中有6钟,然后将每次计算的结果放入一个矩阵钟,作为结果输出.
假如原图形是A*B大小,而模板是a*b大小,则输出结果的矩阵是(A-a+1)*(B-b+1)

OpenCV提供了几种不同的方法:
(建议使用归一化计算方法)
**TM_SQDIFF:计算平分不同,计算出来的值越小,越相关
**TM_CCORR:计算相关性,计算出来的值越大,越相关
**TM_CCOEFF:计算相关系数,计算出来的值越大,越相关
**TM_SQDIFF_NORMED:计算归一化平方不同,计算出来的值越接近0,越相关
**TM_CCORR_NORMED:计算归一化相关性,计算出来的值越接近1,越相关
**TM_CCOEFF_NORMED:计算归一化相关系数,计算出来的值越接近1,越相关

模板匹配语法
result = cv2.matchTemplate(image, templ, method, result=None, mask=None)
image:要匹配的图像。
templ:作为模板的小图像,大小应小于输入图像。
method:指定匹配方法。OpenCV提供了几种不同的方法:(方法在上面)
result:可选的输出结果,它是一个矩阵,用来存储每一个可能的匹配位置的匹配度。
mask:可选的掩码图像,它是一个与模板图像同样大小的8位图像。
函数返回值:
result:一个灰度图像,其中的每个像素表示该点作为模板左上角时的匹配程度。你可以使用cv2.minMaxLoc()函数来找到这个图像中值最小或最大的位置,这取决于使用的方法。

获取最大值和最小值的位置的语法:这个函数在图像处理中经常用于找到图像的亮度范围以及某些特征的位置信息
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src[, mask])
src:是输入的单通道图像（灰度图像）。
mask:是一个可选参数,用于指定在哪些区域内搜索最小值和最大值。如果提供了掩码,那么只有掩码中值为非零的像素才会被考虑。默认值为 None,表示对整个图像进行搜索。
该函数返回:

minVal:是图像中的最小像素值。
maxVal:是图像中的最大像素值。
minLoc:是最小像素值的坐标。
maxLoc:是最大像素值的坐标。
"""
import cv2
import numpy as np

# 读取图片
img= cv2.imread('../image/lena.png')
template= cv2.imread('../image/ldnaw.png')

print("img",img.shape) # (512, 512, 3)
print("template",template.shape) # (190, 160, 3)

# 进行模板匹配(这里使用的是cv2.TM_SQDIFF方法)
# 匹配完之后的结果的大小应该是263-110+1,263-85+1
result= cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
print("result",result.shape) # (323, 353)

# 找最大值和和最小值的位置
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
print("minVal",minVal) # 1102601472.0
print("maxVal",maxVal) # 1979550336.0
print("minLoc",minLoc) # (71, 322)
print("maxLoc",maxLoc) # (218, 58)

# 画出匹配到的位置(画矩形)
h, w, _ = template.shape # 模板
bottom_right = (minLoc[0] + w, minLoc[1] + h)
des = cv2.rectangle(img, minLoc, bottom_right, (0, 0, 255), 2)

# 展示图片
cv2.imshow('img',des)
cv2.imshow('template',template)
cv2.waitKey(0)
cv2.destroyAllWindows()