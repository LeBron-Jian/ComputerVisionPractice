import cv2
 
# 参数为视频文件目录
videoc = cv2.VideoCapture('test.mp4')
# VideoCapture对象，参数可以是设备索引或视频文件名称，设备索引只是指定哪台摄像机的号码
# 0代表第一台摄像机，1代表第二台摄像机，之后可以逐帧捕获视频，但是最后需要释放捕获
# 调用内置摄像头
# cap = cv2.VideoCapture(0)
# 调用USB摄像头
# cap = cv2.VideoCapture(1)
 
 
# 检查是否打开正确
if videoc.isOpened():
    open, frame = videoc.read()
else:
    open = False
 
# 逐帧显示实现视频播放
while open:
    ret, frame = videoc.read()  # 读取
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if cv2.waitKey(10) & 0xFF == 27:  # 读取完自动退出
        # if cv2.waitKey(1) & 0xFF == ord('q'):  # 读完按 q 退出
            break
 
# 释放摄像头对象和窗口
videoc.release()
cv2.destroyAllWindows()
