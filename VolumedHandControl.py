import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

cap = cv2.VideoCapture(0)

#############################################
width_Cam ,Height_Cam = 640,480
#############################################


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]


cap.set(3,width_Cam)
cap.set(4,Height_Cam)
pTime = 0

detector = htm.handDetector(maxHands=1,detectionCon=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    # print(lmList)
    if len(lmList) != 0:
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1], lmList[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2

        cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),10,(255,0,255),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
        # print(length) #输出手指之间的长度(15-180)

        #Hand range 50-300
        #Volume Range -65-0

        vol = np.interp(length,[15,150],[minVol,maxVol])  #类比为归一化处理；把前面的[15,300]转换为[min,max]

        # print(int(length),vol)#输出两手指之间的距离以及对于的音量大小，因为pycaw设计的范围是-65.25到0 即-65.25对于音量为0，0对于最大声。
        volume.SetMasterVolumeLevel(vol, None)

        if length<20:
            cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)

    # cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)


    #计算帧率并显示
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime =cTime
    cv2.putText(img,f'FPS:{int(fps)}',(40,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    cv2.imshow('Img',img)
    cv2.waitKey(1)

