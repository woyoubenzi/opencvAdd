import cv2
import numpy as np

# 加载数字模板图片并进行预处理
def preprocess_template(image_path):
    img = cv2.imread(image_path)
    ref = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, ref = cv2.threshold(ref, 50, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bounding_boxes = [cv2.boundingRect(c) for c in contours]
    contours, bounding_boxes = zip(*sorted(zip(contours, bounding_boxes), key=lambda k: k[1][0]))
    digits = {}
    for (i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        roi = ref[y:y+h, x:x+w]
        roi = cv2.resize(roi, (57, 58))
        digits[i] = roi
    return digits

# 读取并处理信用卡图片，然后匹配模板中的数字
def match_credit_card(image_path, digits):
    image = cv2.imread(image_path)
    h, w = image.shape[:2]
    width = 300
    r = width / float(w)
    image = cv2.resize(image, (300, int(h * r)))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rect_kernel)

    grad_x = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    min_val, max_val = np.min(grad_x), np.max(grad_x)
    grad_x = ((grad_x - min_val) / (max_val - min_val)) * 255
    grad_x = grad_x.astype('uint8')

    grad_x = cv2.morphologyEx(grad_x, cv2.MORPH_CLOSE, rect_kernel)
    _, thresh = cv2.threshold(grad_x, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    sq_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sq_kernel)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    locs = []

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        if 2.5 < ar < 4.0:
            if 40 < w < 55 and 10 < h < 20:
                locs.append((x, y, w, h))

    locs = sorted(locs, key=lambda x: x[0])

    for (i, (gx, gy, gw, gh)) in enumerate(locs):
        group = gray[gy-5:gy+gh+5, gx-5:gx+gw+5]
        group = cv2.threshold(group, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
        digit_contours, _ = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        digit_contours = sorted(digit_contours, key=lambda c: cv2.boundingRect(c)[0])

        group_output = []

        for c in digit_contours:
            (x, y, w, h) = cv2.boundingRect(c)
            roi = group[y:y+h, x:x+w]
            roi = cv2.resize(roi, (57, 58))

            scores = []
            for digit, digit_roi in digits.items():
                result = cv2.matchTemplate(roi, digit_roi, cv2.TM_CCOEFF)
                (_, score, _, _) = cv2.minMaxLoc(result)
                scores.append(score)
            group_output.append(str(np.argmax(scores)))

        cv2.rectangle(image, (gx-5, gy-5), (gx+gw+5, gy+gh+5), (0, 0, 255), 1)
        cv2.putText(image, "".join(group_output), (gx, gy-15), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

    # 展示结果
    cv2.imshow('Processed Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 预处理模板图片并创建数字字典
digits = preprocess_template('../image/123456789.png')

# 匹配信用卡中的数字
match_credit_card('../image/card4.png', digits)
