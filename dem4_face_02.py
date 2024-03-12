import os
import face_recognition
import cv2

"""
人脸识别系统
功能1：根据图片库识别出对象
功能2：设定特定对象，识别出特定对象后用红框标识

读取并存储数据库中的人名和面部特征
"""
boss_names=['Boss','boss']

# 1 准备工作
face_databases_dir='face_database' # 定义数据库所在文件夹(后面可以换成真正的数据库)
user_names=[] # 存储用户名
user_faces_encodings=[] # 存储用户面部特征(和用户名一一对应)
# 2.1 得到face_databases_dir文件夹下所有的文件名
files= os.listdir(face_databases_dir)
# 2.2 循环读取文件名进行进一步的处理
for image_shot_name in files:
    # 2.2.1 截取文件名的前面部分作为用户名
    user_name,_ = os.path.splitext(image_shot_name) # 返回两个值，第一个是文件名，第二个是类型。_ 表示类型的值不需要
    user_names.append(user_name)
    # 2.2.2 读取图片文件中的面部特征信息存储
    image_file_name= os.path.join(face_databases_dir,image_shot_name) # face_database/xxx.jpg
    image_file =face_recognition.load_image_file(image_file_name)  # 加载图片信息
    face_encoding= face_recognition.face_encodings(image_file)[0]  # 读取图片中人的脸部特征信息,多个人脸会返回多个面部特征，这里选第一个
    user_faces_encodings.append(face_encoding)  # 存储用户面部特征

"""
开摄像头，读取摄像头拍视到的画面
定位到画面中人的脸部，并用绿色的框框把人脸框住
top,right,bottom,left [(30,90,45,100)]

用拍视到的脸部特征和数据库中国的面部特征去匹配
并在绿框上方用用户的姓名做标识，未知用户统一使用unkown

定位和锁定目标人物，改使用红色框把人物的脸框住
"""

# 1 打开摄像头。由于摄像头可能有多个，这里选择第一个
vide_capture = cv2.VideoCapture(0)
# 2 无限循环获取摄像头拍摄的画面，并做进一步处理
while True:
    # 2.1 获取摄像头拍摄的画面（会得到两个对象）
    ret,frame= vide_capture.read() # frame 摄像头所拍摄的画面 ret 布尔值，代表能否获取到画面

    # 2.2 从画图中提取人脸所在区域(列表) 元素是这样的： [(30,90,45,100)],可能会有多个
    # ['第一个人脸所在区域','第二个人脸所在区域',...]
    face_locations=face_recognition.face_locations(frame)

    # 2.2.1 从所有人的头像所在区域提取出脸部特征，可能会有多个
    # ['第一个人脸面部区域','第二个人脸面部区域',...]
    face_encodings=face_recognition.face_encodings(frame,face_locations) # 摄像头拍摄画面，人脸所在区域

    # 2.2.2 定义用于存储拍摄到的用户的姓名的列表
    # ['第一个人的姓名','第二个人的姓名'...]
    # 假如特征匹配不上数据库的特征，则是none
    names=[]

    # 遍历face_encodings_2，和之前数据库中的面部特征做匹配
    for x in face_encodings:
        # compare_faces(['面部特征1'],['面部特征2',...],未知的面部特征)
        # compare_faces返回结果
        # 假如 未知的面部特征 和 面部特征1 匹配，和 面部特征2，面部特征3 不匹配
        # 返回的是 [True,False,False]
        matchs= face_recognition.compare_faces(user_faces_encodings,x) # 第一个是存储的面部特征，第二个是未知的面部特征

        # 定义匹配不上特征时显示的字符
        name="None"
        for index,is_match in enumerate(matchs):
            # 下标,布尔值
            if is_match:
                name=user_names[index] #找的匹配到人的姓名
                break
        names.append(name)  # 把匹配到人的姓名存储
    # 2.3 循环遍历人脸部所在的区域，并画框，标识人的姓名

    # zip(["位置1“,"位置2"],["姓名1","姓名2"])
    # for
    # 位置1，位置2
    # 姓名1，姓名2
    for (top,right,bottom,left),name in zip(face_locations,names):

        color=(0,255,0)
        if name in boss_names:
            color=(0,0,255)
        # 2.3.1 在人像所在区域画框（画面，点位1，点位2，颜色，线条宽度）
        cv2.rectangle(frame,(left,top),(right,bottom),color,1)
        # 定义字体
        font=cv2.FONT_HERSHEY_DUPLEX
        # 显示名字
        cv2.putText(frame,name,(left,top-10),font,0.5,color,1)
    # 2.4 通过opencv把画面展示出来,并把画面取名Video
    cv2.imshow("Video",frame)

    # 2.5 设定按Q退出while循环，退出程序的这样一个机制
    if cv2.waitKey(1) & 0xFF==ord('Q'):
        break
# 3 退出程序，释放摄像头或其他资源
vide_capture.release()
cv2.destroyAllWindows()