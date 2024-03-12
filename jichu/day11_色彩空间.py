
import cv2
from pandas import DataFrame

"""
解释色彩空间(HSV,HSL,YUV)，通过DataFrame对图像数据处理：三维转二维，前n行数据；重复数据，形状

openCV用的最多的色彩空间是HSV(HSB)
"""

# 1.HSV(HSB)

"""

H:Hue: 色相(色彩)，取值为0°-360°。
    从红色开始逆时针计算，红色为0°，绿色为120°，蓝色为240°
S:Saturation：饱和度，表示颜色接近光谱色的程度(纯色混入白色的量)。光谱色占比越大，颜色越接近光谱色，饱和度也就越高。
    取值为0%(灰度图像)-100%(鲜艳图像)，值越大颜色越饱和
V(B):Value(Brightness)：明度,明度表示颜色明亮的程度。对于光源色，明度值与发光体的光亮度有关；
    对于物体，明亮度与物体的透射比和反射比有关。通常取值范围为0%(黑)到100%(白)
"""

# 2.HSL
"""
H:Hue：色相
S:Saturation：饱和度
L:Lightness：亮度

HSV和HSL的区别：
H两者完全一致

HSV中的S控制纯色中混入白色的量，值越大，白色越少，颜色越纯
HSV中的B控制纯色中混入黑色的量，值越大，黑色越少，明度越高

HSL中的S和黑白没有关系，表示颜色的浓度，从0%(颜色最淡)-100%（浓度最高）。饱和度不控制颜色中混入黑白的多寡，由L控制
HSL中的L控制纯色中混入的黑白两种颜色
"""

# 3.YUV
"""
YUV是一种颜色编码方法。常使用在各个视频处理组建中。YUV在对照片或视频编码时，考虑到人类的感知能力，允许降低色度的带宽

Y:Luminance(Luma)：明亮度(灰阶值)
'U'和'V'表示的则是色度(Chrominance或Chrome)：作用是描述影像色彩及饱和度，用于指定像素的颜色
YUV的发明在彩色电视与黑白电视的过度时期
YUV最大的优点在于只需占用极少的带宽
 4:4:4 完全取样
 4:2:2 2:1的水平取样，垂直完全取样
 4:2:0 2:1的水平取样，垂直2:1取样
 4:1:1 4:1的水平取样，垂直完全取样
"""

# 1.展示一张图片

cv2.namedWindow('dog',cv2.WINDOW_NORMAL)
cv2.resizeWindow('dog',640,480)

# 2.查看图片中有多少不同颜色
# 读取图像文件 "tur.png"，参数1表示以彩色图像读取
tu = cv2.imread('../image/tur.png', 1)

# 在窗口中显示读取的图像，窗口名称为 'dog'
cv2.imshow('dog', tu)
print(tu)
# 将图像数据转换为DataFrame，reshape(-1, 3)表示将三维数组转换为二维，每行包含三个元素（RGB颜色值）
# 默认是将前两个维度合并在一起，也就是宽度和高度
df = DataFrame(tu.reshape(-1, 3))
print('A==================')
print(df)
# 输出DataFrame的前几行数据，默认5
print('B==================')
print(df.head())

# 输出DataFrame的形状（行数，列数）
print('C==================')
print(df.shape)

# 检查DataFrame中是否存在重复的行，并输出结果
print('D==================')
print(df.duplicated())
print('E==================')
# 不重复的颜色
vv=6-df.duplicated().sum()
print(vv)
cv2.waitKey(0)
cv2.destroyAllWindows()