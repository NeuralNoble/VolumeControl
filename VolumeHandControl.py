import math

import cv2 , time , numpy as np
import osascript

import HandTrackingModule as htm

wCam , hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(detectionCon=0.7)
vol =0
volBar =400
volper = 0
while True:
    sucess , img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList)!=0:
        # print(lmList[4],lmList[8])
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        cx,cy = (x1+x2)//2 ,(y1+y2)//2

        cv2.circle(img,(x1,y1),15,(255,0,255),-1)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), -1)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img,(cx,cy),15,(255,0,255),-1)

        length = math.hypot(x2-x1,y2-y1)
        # print(length)
        ## hand range from 30 to 300
        ## volume range is from 0 to 100
        vol = np.interp(length,[25,290],[0,100])
        volBar = np.interp(length, [25, 290], [400, 150])
        volper = np.interp(length, [25, 290], [0, 100])

        osascript.osascript("set volume output volume {}".format(vol))
        if length<50:
            cv2.circle(img,(cx,cy),15,(0,255,0),-1)

    cv2.rectangle(img,(50,150),(85,400),(255,0,0),3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255,0,0), -1)
    cv2.putText(img, 'volume : ' + str(int(volper)) + '%', (40,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)




    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, 'FPS : ' + str(int(fps)), (40,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3)





    cv2.imshow('img',img)
    cv2.waitKey(1)