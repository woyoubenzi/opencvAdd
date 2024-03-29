
"""
在统计学中,直方图是一种对数据分布情况的图形表示,是一种二维统计图表。

图像直方图基本概念:
图像直方图用于表示数字图像中亮度分布的情况,它绘制了图像中每个亮度值对应的像素数量。
通过观察直方图,我们能够了解图像的亮度分布情况,从而指导如何调整图像的亮度。
在这种直方图中,横坐标的左侧代表较暗的区域,而右侧代表较亮、近似纯白的区域。
因此,一张较暗的图片的直方图数据会主要集中在左侧和中间部分,而整体较亮的图片则呈现相反的趋势。
通过观察这些趋势,我们能够判断图像的亮度分布情况,有助于进行相应的优化调整。

横坐标:图像中各个像素点的灰度级
纵坐标:具有该灰度级的像素个数
https://www.cambridgeincolour.com/tutorials/histograms1.htm

归一化直方图：
横坐标:图像中各个像素点的灰度级
纵坐标:出现这个灰度级的概率

直方图术语：
dims:需要统计的特征的数目。例如:dims=1,表示我们仅统计灰度值
bins:每个特征空间子区段的数目(默认是0-255)
range:统计灰度值的范围,一般为[0,255]
"""