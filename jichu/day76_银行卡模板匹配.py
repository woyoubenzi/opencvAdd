import cv2
import numpy as np

"""
匹配银行卡
"""

"""
对模板进行处理
"""
# 读取
img= cv2.imread('../image/123456789.png')
# 灰度化
ref= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化处理(将图像变成两种值)
_,ref= cv2.threshold(ref,50,255,cv2.THRESH_BINARY_INV)
# 查找轮廓(提取最外层轮廓并只保留角点)
contours,hierarchy=cv2.findContours(ref.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓
cv2.drawContours(img,contours,-1,(0,0,255),1)
print('轮廓数量:',len(contours))
# 对轮廓进行排序,按数字大小
# 排序思路:根据每个数字的最大外接矩阵的X轴坐标进行排序
# 列表推导式
bounding_boxes=[cv2.boundingRect(c) for c in contours]
# 排序函数,对首位进行对比排序
sorted(bounding_boxes,key=lambda b:b[0])
# 把排序之后的外接矩形和轮廓建立关系
(contours,bounding_boxes)= zip(*sorted(zip(contours,bounding_boxes),key=lambda k:k[1][0]))
# 创建一个字典
digits={}
for (i,c) in enumerate(contours):
    # 重新计算外接矩形
    (x,y,w,h)=cv2.boundingRect(c)
    # 取出每个数字,region of interest 感兴趣的区域
    roi=ref[y:y+h,x:x+w]
    # resize成合适的大小
    roi=cv2.resize(roi,(57,88))
    digits[i]=roi
    # 显示所有分割出来的数字
    # cv2.imshow(f'name{i}',roi)

"""
处理图片
"""
# 读取图片
image=cv2.imread('../image/card4.png')

# 对信用卡图像进行resize(调整大小)
h,w=image.shape[:2]
width=300
r=width/w

image=cv2.resize(image,(300,int(h*r)))

# 对变小后的卡片灰度化处理
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 初始化卷积核
rect_kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(9,3))
# 顶帽操作,突出更明亮的区域
tophat= cv2.morphologyEx(gray,cv2.MORPH_TOPHAT,rect_kernel)

# 索贝尔算子X轴(检测边缘)
grad_x= cv2.Sobel(tophat,ddepth=cv2.CV_32F,dx=1,dy=0,ksize=-1)
# 把grad_x变成0到255之间的整数
min_val,max_val=np.min(grad_x),np.max(grad_x)
grad_x= ((grad_x-min_val)/(max_val-min_val))*255
# 修改一下数据类型为整数
grad_x = grad_x.astype('uint8')

# 闭运算,先膨胀,再腐蚀
grad_x=cv2.morphologyEx(grad_x,cv2.MORPH_CLOSE,rect_kernel)

# 通过大津(OTSU)算法找的合适的阈值,进行全局二值化操作
_,thresh= cv2.threshold(grad_x,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# 中间还有空洞,再次闭操作
sq_kerner=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sq_kerner)

# 寻找轮廓
contours,hierarchy= cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# 在copy图上画轮廓
image_copy=image.copy()
cv2.drawContours(image_copy,contours,-1,(0,255,255),3)

locs=[]

# 遍历轮廓,计算外接矩形,然后根据实际信用卡数字区域的长宽闭,找到真正的数字区域
for c in contours:
    # 计算外接矩形
    (x,y,w,h)=cv2.boundingRect(c)
    # 计算外接矩形的长宽比例
    ar= w/float(h)
    # 选择合适的区域
    if ar>2.5 and ar<4.0:
        # 根据实际的长宽做进一步的筛选
        if(w >30 and w<55) and (h>10 and h<20):
            # 符合条件的外接矩形留下来
            locs.append((x,y,w,h))
# 对符合要求的轮廓进行从左到右的排序
locs =sorted(locs,key=lambda x:x[0])

# 遍历每一个外接矩形,通过外接矩形可以把原图中的数字抠出来
for (i,(gx,gy,gw,gh)) in enumerate(locs):
    # 抠出数字区域,并且加点余量
    group= gray[gy-5:gy+gh+5,gx-5:gx+gw+5] 

    # 对取出的灰色区域做全局二值化处理
    group= cv2.threshold(group,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # 计算轮廓
    digit_contours, hierarchy = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 列表推导式
    bounding_boxes = [cv2.boundingRect(c) for c in digit_contours]  # 这里改为使用digit_contours
    # 对轮廓进行排序
    digit_contours = sorted(digit_contours, key=lambda c: cv2.boundingRect(c)[0])

    # 定义每一组匹配到的数字的存放列表
    group_output=[]
    # 遍历排好序的轮廓
    for c in digit_contours:
        # 找的当前数字的轮廓,resize成合适的大小,然后再进行模板匹配
        (x,y,w,h)=cv2.boundingRect(c)
        # 取出数字
        roi=group[y:y+h,x:x+w]
        roi=cv2.resize(roi,(57,88))
        cv2.imshow('img',roi)

        # 进行模板匹配
        scores = []
        for digit_key, digit_roi in digits.items():  # 假设digits是之前处理好的模板数字字典
           result = cv2.matchTemplate(roi, digit_roi, cv2.TM_CCOEFF_NORMED) 
           _, score, _, _ = cv2.minMaxLoc(result)
           scores.append(score)  # 将得分添加到scores列表中

        # 找到得分最高的数字
        matched_digit = str(np.argmax(scores))  # 这假设每个模板的键是0-9的字符串
        group_output.append(matched_digit)
    # 画出轮廓和显示数字
    cv2.rectangle(image,(gx-5,gy-5),(gx+gw+5,gy+gh+5),(0,0,255),1)
    cv2.putText(image,"".join(group_output),(gx,gy-15),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
# 展示
cv2.imshow('name',image)
cv2.imshow('123',img)
cv2.waitKey(0)
cv2.destroyAllWindows()