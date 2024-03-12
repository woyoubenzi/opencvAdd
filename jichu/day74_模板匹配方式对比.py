"""
6种匹配方式的对比(扩展)
**TM_SQDIFF:计算平分不同,计算出来的值越小,越相关
**TM_CCORR:计算相关性,计算出来的值越大,越相关
**TM_CCOEFF:计算相关系数,计算出来的值越大,越相关
**TM_SQDIFF_NORMED:计算归一化平方不同,计算出来的值越接近0,越相关
**TM_CCORR_NORMED:计算归一化相关性,计算出来的值越接近1,越相关
**TM_CCOEFF_NORMED:计算归一化相关系数,计算出来的值越接近1,越相关
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt # 画图包

# 以灰度图方式读取图片
img= cv2.imread('../image/lena.png',0)
template= cv2.imread('../image/ldnaw.png',0)

# 定义6种模板匹配方法列表
methods=[cv2.TM_SQDIFF,cv2.TM_CCORR,cv2.TM_CCOEFF,cv2.TM_SQDIFF_NORMED,cv2.TM_CCORR_NORMED,cv2.TM_CCOEFF_NORMED]
method_names =["TM_SQDIFF","TM_CCORR","TM_CCOEFF","TM_SQDIFF_NORMED","TM_CCORR_NORMED","TM_CCOEFF_NORMED"]

# 循环匹配方法,enumerate(methods)函数用于创建一个下标
for idx,method in enumerate(methods):
    # 复制原图
    img2=img.copy()
    # 进行模板匹配
    result= cv2.matchTemplate(img,template,method)
    # 找最大值和最小值的位置
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    # 假如匹配方法是TM_SQDIFF和TM_SQDIFF_NORMED,数值越大越接近,需要用到最大值.其他是越小越好
    if method in [cv2.TM_SQDIFF_NORMED,cv2.TM_SQDIFF]:
        top_left=minLoc
    else:
        top_left=maxLoc
    # 画出匹配到的位置(画矩形)
    h, w = template.shape # 原图
    bottom_right = (top_left[0] + w, top_left[1] + h) # 得到宽高
    des = cv2.rectangle(img2, top_left, bottom_right, (0, 0, 255), 2) # 在原图上画匹配区域

    # 画子图,都画在一起
    plt.subplot(121),plt.imshow(img2,cmap='gray')
    plt.axis('off')
    plt.subplot(122),plt.imshow(result,cmap='gray')
    plt.axis('off')
    plt.suptitle(method_names[idx])
    plt.show()
    # 展示图片
    #cv2.imshow(method_names[i],des)

cv2.waitKey(0)
cv2.destroyAllWindows()