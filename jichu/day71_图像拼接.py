import cv2
import numpy as np

"""
两张图片拼接的思路
1.读取图片
2.图片灰度化
3.计算各自的特征点和描述子
4.匹配特征
5.根据特征,计算单应性矩阵
6.对其中一张图片进行透视变换(使两张图视角一样)
7.创建一个大图,放入两张图
"""

# 读取图片
img1=cv2.imread('../image/xuan1.png')
img2=cv2.imread('../image/xuan2.png')

# 灰度化处理
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# 创建sift特征检测对象
sift= cv2.SIFT.create()

# 用于在图像中检测关键点并计算描述子
kp1,des1= sift.detectAndCompute(gray1,mask=None)
kp2,des2= sift.detectAndCompute(gray2,mask=None)


# 创建适用于FLANN的字典
index_params=dict(algorithm=0,trees=5)
search_params = dict(checks=50)

# 创建FLANN特征匹配器
flann= cv2.FlannBasedMatcher(index_params,search_params)

# 使用FLANN匹配特征
matchs=flann.knnMatch(des1,des2,k=2)

# 创建列表存储符合的特征点
goods=[]
# 检索符合条件的特征点(这里也是纯手敲,没提示)
for m,n in matchs:
    if m.distance<0.75*n.distance:
        goods.append(m)

# 如果特征点大于4个(这段完全不会,没提示)
if len(goods)>=4:
    # 根据Dmatch对象拿到各自的特征点
    src_points=np.float32([kp1[m.queryIdx].pt for m in goods]).reshape(-1,1,2)
    dst_points=np.float32([kp2[m.trainIdx].pt for m in goods]).reshape(-1,1,2)

    # 第一个图变成第二个图的视角.计算单应性矩阵(就是找像素与物理世界的坐标)
    H,_=cv2.findHomography(src_points,dst_points,cv2.RANSAC,5)

else:
    print("滴滴")
    exit()

# 获取原始图的宽高
h1,w1=img1.shape[:2]
h2,w2=img2.shape[:2]
print('h1w1',h1,w1)
# 得到原始图的四个角(左上,左下,右下,右上)
pst1= np.float32([[0,0],[0,h1-1],[w1-1,h1-1],[w1-1,0]]).reshape(-1,1,2)
pst2= np.float32([[0,0],[0,h2-1],[w2-1,h2-1],[w2-1,0]]).reshape(-1,1,2)

# 根据前面计算出来的H,计算img1的四个角变换之后的坐标
img1_transorm=cv2.perspectiveTransform(pst1,H)
print(type(img1))

# 将透视变换后的坐标与第二张图按axis=0方向拼接(保证最终合并的图像都能包含两幅图像的全部内容)
#result_pts=np.concatenate((img1_transorm,pst2),axis=0)
# 这个和result_pts的效果一样,将两幅图垂直链接
result_pts = cv2.vconcat([img1_transorm, pst2])

# 对行聚合,返回两列各自的最小值(result_pts里面有小数,这里需要用np.int32转换为整数,ravel是将数组变成一维)
[min_x,min_y]= np.int32(result_pts.min(axis=0).ravel()-1)

# 对行聚合,返回两列各自的最大值
[max_x,max_y]= np.int32(result_pts.max(axis=0).ravel()+1)

# 手动构造平移矩阵(如果不平移图像就不在画面中心,画面就无法拼接)
move_matrix=np.array([[1,0,-min_x],[0,1,-min_y],[0,0,1]])

# 对img1平移后进行透视变换,后面的4个属性表示图像的面积
result_img= cv2.warpPerspective(img1,move_matrix.dot(H),(max_x-min_x,max_y-min_y))

# 将两张图合并在一起
result_img[-min_y:-min_y+h2,-min_x:-min_x+w2]=img2
# 展示图片
cv2.imshow('img',result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()