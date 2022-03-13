import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

#Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)   #detectionCon置信值  maxHands 最多允许手的数量

#Find Function(使用numpy拟合出一个用于换算距离的二阶多项式y=ax^2+bx+c x是像素值，y是厘米)
# x is the raw daitance , y is the value in cm
x = [300,245,200,170,145,130,112,103,93,87,80,75,70,67,62,59,57]
y = [20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

coff = np.polyfit(x,y,2) #使用numpy进行拟合，二阶多项式填2 y=ax^2+bx+c  ;三阶多项式3



#Loop
while True:
    success, img = cap.read()
    hands = detector.findHands(img,draw=False)   #img后面加上draw=False 则不显示手部骨架
    # hands, img = detector.findHands(img)   #显示手部骨架

    if hands:
        lmList = hands[0]['lmList']
        x, y, w, h = hands[0]['bbox']
        #print(lmList) #对照hand_landmarks表找到手关节相应对照的点
        x1, y1 ,z1 = lmList[5]
        x2, y2 ,z2 = lmList[17]

        distance = int(math.sqrt((y2-y1)**2 + (x2-x1)**2))
        A, B, C = coff
        distanceCM = A * distance **2 + B * distance + C

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)    #cv2框选手部位置
        cvzone.putTextRect(img, f'{int(distanceCM)} cm' , (x+5,y-10)) #在图像中加入文字
        





    cv2.imshow("Image",img)
    cv2.waitKey(1)
