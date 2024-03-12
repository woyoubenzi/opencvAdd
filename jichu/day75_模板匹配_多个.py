"""
匹配多个对象
"""
import cv2
import numpy as np

kupao=cv2.imread('../image/ganten2.jpg')
print(kupao.shape)
# 灰度化
kupao_gray=cv2.cvtColor(kupao,cv2.COLOR_BGR2GRAY)
#template=cv2.imread('../image/gai4.png',0)
# 加载含有透明度的模板图像
template_with_alpha = cv2.imread('../image/gai4.png', cv2.IMREAD_UNCHANGED)
# 获取alpha通道作为掩码，alpha通道是最后一个通道
mask = template_with_alpha[:, :, 3]
# 将模板转换为BGR，忽略透明度通道
template_a = cv2.cvtColor(template_with_alpha, cv2.COLOR_BGRA2BGR)
# 将模板转换为灰度图像
template = cv2.cvtColor(template_a, cv2.COLOR_BGR2GRAY)

h,w=template.shape[:2]
# 匹配
res= cv2.matchTemplate(kupao_gray,template,cv2.TM_CCORR_NORMED)

# 设置阈值,系数大于0.99视为匹配成功
# 瓶盖的系数为0.97978
threshold=0.86
# 返回满足条件的索引(x,y轴索引)
loc= np.where(res>=threshold)
print('匹配次数:', len(loc[0]))
#np.argwhere(res>=threshold)
for pt in zip(*loc[::-1]):
    bottom_right=(pt[0]+w,pt[1]+h)
    # 画图
    cv2.rectangle(kupao,pt,bottom_right,(0,0,255),2)
print(kupao.shape)
cv2.namedWindow('kupao',cv2.WINDOW_NORMAL)
cv2.resizeWindow('kupao', 800, 800)
cv2.imshow('kupao',kupao)
cv2.imshow('template',template_a)
cv2.waitKey(0)
cv2.destroyAllWindows()