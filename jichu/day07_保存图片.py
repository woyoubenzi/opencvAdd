import cv2
"""
imwrite保存图片
"""
# 保存图像方法
def baocunimg():
    # 创建窗口
    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    # 给指定窗口设定宽高
    cv2.resizeWindow('img',820,480)

    # 读取图片
    img=cv2.imread('../image/tur.png')

    while True:
        # 展示图像
        cv2.imshow('img',img)
        key= cv2.waitKey(0)

        if key==ord('Q'):
            break
        elif key==ord('S'):
            # 保存图像
            cv2.imwrite('./123.png',img)
        else:
            print(key)


if __name__=='__main__':
    baocunimg()

    cv2.destroyAllWindows()