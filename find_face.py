import cv2
import time
import requests
capture = cv2.VideoCapture(0)#获取摄像头对象
casc_path = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)
color = (0, 255, 0)
font = cv2.FONT_HERSHEY_SIMPLEX


end_time=0
countdown=0
while(True):
    #读取一帧图像
    ret,frame=capture.read()#第一个返回值是bool值，判断是否有图像，第二个就是图像
    if ret:
        #转换为灰度图
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceRects = faceCascade.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))#这是一个数组，可以输出来看一下，有人脸的大小范围的参数
        count = str(len(faceRects))

        if int(count) > 0:      #大于0则检测到人脸
            start_time = time.time()#要判断发送请求的时间间隔，两次间隔不能少于30秒，不然体验很不好
            if end_time<1:
                requests.get("http://192.168.1.165:8080/")
                end_time = time.time()
            countdown= int(start_time-end_time)
            if start_time-end_time>30:
                requests.get("http://192.168.1.165:8080/") #每次重启电脑都要更换内网ip
                end_time = time.time()
            for faceRect in faceRects: #绘制框框，单独框出每一张人脸
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
        cv2.putText(frame, "count:"+count, (10, 40), font, 0.8, (0, 255, 255), 2)#添加一个人脸个数的文字显示
        #显示图像
        cv2.imshow("test", frame)
        c = cv2.waitKey(10)#等待退出键
        if c & 0xFF == ord('q'):
          break