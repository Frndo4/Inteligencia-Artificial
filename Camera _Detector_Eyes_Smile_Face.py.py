import numpy as np
import cv2              

#Importamos los archivos para la detección de rasgos faciales
#En este caso será el rostro completo, la sonrisa y los ojos
face_cascade=cv2.CascadeClassifier('C:/opencv/haarcascades/haarcascades/haarcascade_frontalface_alt.xml')
eyes_cascade=cv2.CascadeClassifier('C:/opencv/haarcascades/haarcascades/haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('C:/opencv/haarcascades/haarcascades/haarcascade_smile.xml')    


#Importamos la imagen a analizar y la convertimos a escala de grises
video=cv2.VideoCapture(0)
while(True):
    ret, frame=video.read()   #Mostrar frame
    cv2.imshow('Video', frame)

    #Escala de grises
    gris=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Escala de grises', gris)

    if cv2.waitKey(1) & 0xFF == ord ('s'):
        break

#La función "detectMultiScale" puede detectar todas las caras en la imagen y guardar las coordenadas 
#y el tamaño de cada cara con un vector (representado por un rectángulo).
face= face_cascade.detectMultiScale(gris, 1.35, 1)
eye= eyes_cascade.detectMultiScale(gris, 1.35, 1)
smile= smile_cascade.detectMultiScale(gris, 1.35, 1)


#Con estos ciclos for crearemos los rectángulos para poder visualizarlos en la imagen
for(x,y,w,h) in face:
    frame=cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    roi_gray = gris[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]

    for(ex,ey,ew,eh) in eye:
        frame=cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), (255,0,0), 2)
        roi_gray = gris[ey:ey+eh, ex:ex+ew]
        roi_color = frame[ey:ey+eh, ex:ex+ew]

        for(sx,sy,sw,sh) in smile:
            frame=cv2.rectangle(frame, (sx,sy), (sx+sw, sy+sh), (0,255,0), 2)
            roi_gray = gris[sy:sy+sh, sx:sx+sw]
            roi_color = frame[sy:sy+sh, sx:sx+sw]

            
#Aquí es donde al compilar, lograremos ver la imagen ya con la detección

while(True):
        
    cv2.imshow('Detección', frame)

    if cv2.waitKey(1) & 0xFF == ord ('d'):
        break

#Finalizar cámara
video.release()
cv2.destroyAllWindows()
