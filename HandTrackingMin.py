import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0



while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks) #输出是否有手，有则输出手的landmarks，没有则输出none
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id ,lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w),int(lm.y*h)
                # print(id,cx,cy)
                # if id ==0:
                cv2.circle(img, (cx,cy),5,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    #设置fps的值
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)






    cv2.imshow('Img',img)
    cv2.waitKey(1)
