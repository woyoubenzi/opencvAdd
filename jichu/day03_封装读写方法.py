import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1 把展示cv2图片的代码封装成函数
def cv_show(name,img):
    # 显示图像
    cv2.imshow(name,img)


# 2 把展示plt图片的代码封装成函数(有BUF)
def plt_show(name,img):
    # 显示图像
    """这行代码不显示，有大问题"""
    plt.imshow(img)
    # 显示标题
    plt.title(name)
    # 显示Matplotlib图像窗口
    plt.show()

# 3 返回图片信息的函数
def calImage(img):
    # shape 形状
    rows=img.shape[0] # 行列
    cols=img.shape[1]
    channel=img.shape[2] # 通道数

    # 图像类型属性
    # uint8格式，即无符号整型八位，可以节省空间
    str1=str(img.dtype)

    # 像素大小
    sizeImg=img.size

    return rows,cols,channel,str1,sizeImg

# 4 保存图像的函数
def imwrite_img(url,img):
    # 接收两个参数：要保存的地址，图片信息
    cv2.imwrite(url, img)

# 5 分别读取通道的方法
def splitImage(img):
    # 一张图像，默认是RGB空间
    # split读取顺序是BGR
    b,g,r=cv2.split(img)
    print("这是B通道", b)
    print("这是G通道", g)
    print("这是R通道", r)
    # cv2.imshow("B", b)
    # cv2.imshow("G", g)
    # cv2.imshow("R", r)

    return b,g,r

# 6 合并通道的方法
def heImage(b,g,r):
    # 1.cv自带 merge合并通道时，也是BGR的顺序
    #newsrc= cv2.merge([b,g,r])

    # 2. 更加快速 stack合并通道时，也是BGR的顺序
    newsrc=np.stack((b, g, r), axis=2)

    cv2.imshow('newsrc',newsrc)

# 7 暂停画像等待用户按键
def waitKey():
    # 等待按键
    key = cv2.waitKey(0) & 0xFF
    if key == ord('s'):
        print("AAAAA")
    # 销毁窗口
    cv2.destroyAllWindows()



# 主函数
if __name__=="__main__":
    # 读取图像
    #img = cv2.imread("C:/Users/MVV/Pictures/Camera Roll/hd1.webp")
    img = cv2.imread("../image/gai4.png")

    # cv2展示图像的方法
    cv_show("PPP",img)

    # plt展示图像的方法（有BUG）
    #plt_show('ppp',img)

    # 保存图像的方法
    #imwrite_img('./TEST.jpg',img)

    # 读取图像信息的方法
    #a,b,c,d,e=calImage(img)

    #b,g,r= spliltImage(img)
    #heImage(b,g,r)

    # 暂停画面等待用户按键的方法(有BUG)
    waitKey()

    # 关闭所有窗口
    #cv2.destroyAllWindows()