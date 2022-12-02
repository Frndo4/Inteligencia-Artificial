import cv2
import numpy as np

cap=cv2.VideoCapture(0)

#Color Rojo
rojoBajo1=np.array([136, 87, 111],np.uint8)
rojoAlto1=np.array([180, 255, 255],np.uint8)

#rojoBajo2=np.array([175,100,20],np.uint8)
#rojoAlto2=np.array([179,255,255],np.uint8)

#Color Azul
azulBajo=np.array([94, 80, 2],np.uint8)
azulAlto=np.array([120, 255, 255],np.uint8)

#Color Verde
verdeBajo=np.array([25, 52, 72],np.uint8)
verdeAlto=np.array([102, 255, 255],np.uint8)

while True:
    ret,frame=cap.read()
    
    if ret==True:
        frameHSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #Color Rojo
        maskRed1=cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
        #maskRedvis=cv2.bitwise_and(frame, frame, mask= maskRed)

        #Color Azul
        maskAzul=cv2.inRange(frameHSV, azulBajo, azulAlto)
        
        #Color Verde
        maskVerde=cv2.inRange(frameHSV, verdeBajo, verdeAlto)

        contornos,_=cv2.findContours(maskAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contornos1,_=cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contornos2,_=cv2.findContours(maskRed1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
        
        for a in contornos:
            area=cv2.contourArea(a)
            if area > 3000:
                nuevoContorno=cv2.convexHull(a)
                cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3)
                
                
        for b in contornos1:
            area2=cv2.contourArea(b)
            if area2 > 3000:
                nuevoContorno2=cv2.convexHull(b)
                cv2.drawContours(frame, [nuevoContorno2], 0, (0,255,0), 3)
        
        for c in contornos2:
            area3=cv2.contourArea(c)
            if area3 > 3000:
                nuevoContorno3=cv2.convexHull(c)
                cv2.drawContours(frame, [nuevoContorno3], 0, (0,0,255), 3)

        #cv2.imshow('maskRedvis', maskRedvis)
        #cv2.imshow('MaskRed', maskRed)
        #cv2.imshow('maskAzul', maskAzul)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()


