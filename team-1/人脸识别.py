# 使用Haar Cascades进行人脸检测 https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#basics
# opencv 官网 https://opencv.org/

import cv2

filename1 = 'D:/faces/pic1.jpg'
filename2 = 'D:/faces/pic2.jpg'
filename3 = 'D:/faces/pic3.jpg'


def detect(filename):
    #产生检测器 获取训练数据
    face_cascade = cv2.CascadeClassifier('C:/Users/Administrator/Downloads/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('C:/Users/Administrator/Downloads/opencv/build/etc/haarcascades/haarcascade_eye.xml')
    
    #读入图像
    img = cv2.imread(filename)
    
    #转化为灰度图像 降低计算强度
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #检测
    faces = face_cascade.detectMultiScale(
        image = gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30,30)
    )
    # scaleFactor - 每张图片的缩放因子
    # minNeighbors - 每个候选矩形应保留多少个邻居
    
    nums=len(faces) #人脸的数量
    if nums == 1:
        text = '1 face'
    else:
        text = '{} faces'.format(nums)

    for (x,y,w,h) in faces: # x y 高 宽
        
        #绘制矩形
        img = cv2.rectangle(
            img = img,
            pt1 = (x,y),
            pt2 = (x+w,y+h),
            color = (0,255,0),
            thickness = 2
        )
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
         
        #眼睛
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 3)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
    
    img = cv2.resize(img,(800,600))
    cv2.putText(
        img = img,
        text = text,
        org = (50,50),
        fontFace = cv2.FONT_HERSHEY_COMPLEX,
        fontScale = 2,
        color = (0,0,0),
        thickness = 2
    ) #写字

    cv2.namedWindow(winname = "Faces", flags = cv2.WINDOW_AUTOSIZE)
    cv2.imshow(winname = 'Faces deteced!', mat = img)
    
    cv2.waitKey(0) #等待键盘输入 参数为0 即无限等待
    
    cv2.destroyAllWindows()

if __name__=="__main__":
    detect(filename1)
    detect(filename2)
    detect(filename3)

'''import cv2
filename1 = 'D:/faces/pic2.jpg'
img=cv2.imread(filename1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('ok', gray)
cv2.waitKey(0)'''



