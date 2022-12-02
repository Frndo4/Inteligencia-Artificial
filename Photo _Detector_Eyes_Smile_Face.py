#Importamos las librerías
import numpy as np
import cv2              

#Importamos los archivos para la detección de rasgos faciales
#En este caso será el rostro completo, la sonrisa y los ojos
face_cascade=cv2.CascadeClassifier('C:/opencv/haarcascades/haarcascades/haarcascade_frontalface_alt.xml')
eyes_cascade=cv2.CascadeClassifier('C:/opencv/haarcascades/haarcascades/haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('C:/opencv/haarcascades/haarcascades/haarcascade_smile.xml')    

#Importamos la imagen a analizar y la convertimos a escala de grises
imagen = cv2.imread(r'C:\opencv\cara.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#La función "detectMultiScale" puede detectar todas las caras en la imagen y guardar las coordenadas 
#y el tamaño de cada cara con un vector (representado por un rectángulo).
face= face_cascade.detectMultiScale(gray, 1.35, 1)
eye= eyes_cascade.detectMultiScale(gray, 1.35, 1)
smile= smile_cascade.detectMultiScale(gray, 1.35, 1)

#Con estos ciclos for crearemos los rectángulos para poder visualizarlos en la imagen
for(x,y,w,h) in face:
    imagen=cv2.rectangle(imagen, (x,y), (x+w, y+h), (0,0,255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = imagen[y:y+h, x:x+w]

    for(ex,ey,ew,eh) in eye:
        imagen=cv2.rectangle(imagen, (ex,ey), (ex+ew, ey+eh), (255,0,0), 2)
        roi_gray = gray[ey:ey+eh, ex:ex+ew]
        roi_color = imagen[ey:ey+eh, ex:ex+ew]

        for(sx,sy,sw,sh) in smile:
            imagen=cv2.rectangle(imagen, (sx,sy), (sx+sw, sy+sh), (0,255,0), 2)
            roi_gray = gray[sy:sy+sh, sx:sx+sw]
            roi_color = imagen[sy:sy+sh, sx:sx+sw]

#Aquí es donde al compilar, lograremos ver la imagen ya con la detección
cv2.imshow('Detección', imagen)
cv2.imwrite('imagen.jpg', imagen)  #Guardar la imagen
cv2.waitKey(0)
cv2.destroyAllWindows()
