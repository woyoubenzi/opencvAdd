import cv2
import numpy as np

# 加载数字模板图片并进行预处理
def preprocess_template(image_path):
    # 读取模板图像
    img = cv2.imread(image_path)
    # 将图像转换为灰度图，以便处理
    ref = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 对灰度图应用二值化处理，使其仅包含黑白两色，便于轮廓检测
    _, ref = cv2.threshold(ref, 50, 255, cv2.THRESH_BINARY_INV)
    # 检测二值化图像中的轮廓
    contours, _ = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 计算每个轮廓的外接矩形
    bounding_boxes = [cv2.boundingRect(c) for c in contours]
    # 根据外接矩形的X轴坐标对轮廓进行排序，假设数字是从左到右排列的
    contours, bounding_boxes = zip(*sorted(zip(contours, bounding_boxes), key=lambda k: k[1][0]))
    # 创建一个字典来存储每个数字的图像
    digits = {}
    for (i, c) in enumerate(contours):
        # 重新计算每个轮廓的外接矩形
        (x, y, w, h) = cv2.boundingRect(c)
        # 根据外接矩形裁剪出数字区域
        roi = ref[y:y+h, x:x+w]
        # 将裁剪出的数字区域调整到固定大小
        roi = cv2.resize(roi, (57, 58))
        # 将处理后的数字区域存储到字典中
        digits[i] = roi
    return digits

# 读取并处理信用卡图片，然后匹配模板中的数字
def match_credit_card(image_path, digits):
    # 读取信用卡图像
    image = cv2.imread(image_path)
    h, w = image.shape[:2]
    # 调整图像大小
    width = 300
    r = width / float(w)
    image = cv2.resize(image, (300, int(h * r)))
    # 将调整大小后的图像转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 初始化用于形态学操作的矩形卷积核
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
    # 对灰度图应用顶帽操作，突出更明亮的区域
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rect_kernel)

    # 使用Sobel算子检测边缘
    grad_x = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    # 将边缘检测结果标准化到0到255范围内
    min_val, max_val = np.min(grad_x), np.max(grad_x)
    grad_x = ((grad_x - min_val) / (max_val - min_val)) * 255
    grad_x = grad_x.astype('uint8')

    # 对边缘检测结果应用闭运算，填充数字间的空隙
    grad_x = cv2.morphologyEx(grad_x, cv2.MORPH_CLOSE, rect_kernel)
    # 使用OTSU算法自动找到二值化阈值，并应用二值化
    _, thresh = cv2.threshold(grad_x, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # 对二值化结果再次应用闭运算，确保数字区域是连续的
    sq_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sq_kernel)

    # 检测二值化图像中的轮廓
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 初始化一个列表来存储符合条件的轮廓（数字区域）
    locs = []

    # 遍历找到的轮廓
    for c in contours:
        # 计算每个轮廓的外接矩形
        (x, y, w, h) = cv2.boundingRect(c)
        # 计算长宽比
        ar = w / float(h)
        # 根据长宽比和实际尺寸筛选可能是数字区域的轮廓
        if 2.5 < ar < 4.0:
            if 40 < w < 55 and 10 < h < 20:
                locs.append((x, y, w, h))

    # 根据X轴坐标对筛选出的轮廓进行排序
    locs = sorted(locs, key=lambda x: x[0])

    # 遍历每个筛选出并排序后的轮廓
    for (i, (gx, gy, gw, gh)) in enumerate(locs):
        # 根据轮廓裁剪出数字区域
        group = gray[gy-5:gy+gh+5, gx-5:gx+gw+5]
        # 对裁剪出的区域应用二值化
        group = cv2.threshold(group, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
        # 检测裁剪出的数字区域中的轮廓
        digit_contours, _ = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 根据X轴坐标对数字区域中的轮廓进行排序
        digit_contours = sorted(digit_contours, key=lambda c: cv2.boundingRect(c)[0])

        # 初始化一个列表来存储每个数字区域匹配到的数字
        group_output = []

        # 遍历每个数字区域的轮廓
        for c in digit_contours:
            # 计算轮廓的外接矩形，并裁剪出对应的区域
            (x, y, w, h) = cv2.boundingRect(c)
            roi = group[y:y+h, x:x+w]
            # 将裁剪出的区域调整到固定大小
            roi = cv2.resize(roi, (57, 58))

            # 初始化一个列表来存储每个模板数字的匹配得分
            scores = []
            # 遍历模板数字字典
            for digit, digit_roi in digits.items():
                # 对每个模板数字进行模板匹配
                result = cv2.matchTemplate(roi, digit_roi, cv2.TM_CCOEFF)
                # 获取匹配得分
                (_, score, _, _) = cv2.minMaxLoc(result)
                scores.append(score)
            # 根据得分找到匹配度最高的数字，并将其添加到结果列表中
            group_output.append(str(np.argmax(scores)))

        # 在原图上标记识别到的数字区域
        cv2.rectangle(image, (gx-5, gy-5), (gx+gw+5, gy+gh+5), (0, 0, 255), 1)
        # 在数字区域上方显示匹配到的数字
        cv2.putText(image, "".join(group_output), (gx, gy-15), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

    # 展示处理后的图像
    cv2.imshow('Processed Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 预处理模板图片并创建数字字典
digits = preprocess_template('../image/123456789.png')

# 匹配信用卡中的数字
match_credit_card('../image/card4.png', digits)