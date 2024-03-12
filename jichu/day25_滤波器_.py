import cv2
import numpy as np
# 滤波器(主要用来去噪)
"""
图像的卷积操作
卷积:图像卷积就是卷积核再图像上按行滑动遍历像素时不断的相乘求和的过程
卷积核:卷积核区域会与图片进行相乘,并将结果相加
步长:就是卷积核在图像上移动的步幅(为了充分扫码图片,步长一般设为1)
填充(padding):从上面的例子我们发现,卷积之后的图片长宽会变小,如果保持图片大小不变,我们需要在原图周围填充0。padding就是填充0的圈数

filter2D 函数是 OpenCV 中用于进行自定义卷积操作的函数，通常用于图像滤波。这个函数执行的是离散卷积操作，其中输入图像的每个像素都与一个卷积核进行卷积，生成输出图像

语法:filter2D(src,ddepth,kernel[,dst[,anchor[,delta[,borderType]]])
ddepth是卷积之后图片的位深,即卷积之后图片的数据类型,一般设为-1,表示和原图类型一致.
kernel是卷积核大小,用元组或者ndarray表示,要求数据类型必须是float型
anchor锚点,即卷积核的中心带,是可选参数,默认是(-1,-1)
delta可选参数,表示卷积之后额外加的一个值,相当于线性方程中的偏差,默认是0
borderType边界类型,一般不设置
"""
# 读取图片
img= cv2.imread("../image/lookbook.jpg")
# 将RGB通道转换为BGR
#cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
"""
卷积示例1:将图片变模糊
"""
# np.ones 是一个用于创建所有元素都设置为1的数组的函数
# 创建一个 5x5 的卷积核，每个元素的值都是 1，然后将卷积核中的所有值除以 25
# 这样的卷积核实际上是一个平均滤波器，相当于原始图的每个点都被平均了一下，所以图像变模糊了
# kernel必须是float类型
# float16是半精度浮点，float32是单精度浮点，float64是双精度浮点

#kernel=np.ones((5,5),np.float32)/25
"""
卷积示例2:从网上找卷积核进行验证。
"""
# 创建一个3*3的卷积核，轮廓效果
#kernel=np.array([[-1,-1,-1,],[-1,8,-1],[-1,-1,-1]])
# 创建一个3*3的卷积核，浮雕效果
kernel=np.array([[-2,-1,0,],[-1,1,1],[0,1,2]])
"""
展示
"""
# 图像滤波，ddepth=-1表示图片的数据类型不变
dst=cv2.filter2D(img,-1,kernel)
# 展示图片
cv2.imshow('img',np.hstack((img,dst)))
# 等待按键暂停
cv2.waitKey(0)
# 关闭
cv2.destroyAllWindows()