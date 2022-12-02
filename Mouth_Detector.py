#Importamos las librerías
import numpy as np
import cv2              

#Importamos los archivos para la detección de rasgos faciales
#En este caso será el rostro completo, la sonrisa y los ojos

smile_cascade=cv2.CascadeClassifier('C:/opencv/haarcascades/OneDrive_1_30-3-2022/haarcascade_mcs_mouth.xml')   


#Importamos la imagen a analizar y la convertimos a escala de grises
imagen = cv2.imread(r'C:\opencv\ex_U4.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#La función "detectMultiScale" puede detectar todas las caras en la imagen y guardar las coordenadas 
#y el tamaño de cada cara con un vector (representado por un rectángulo).

smile= smile_cascade.detectMultiScale(gray, 10, 2)

for(sx,sy,sw,sh) in smile:
    imagen=cv2.rectangle(imagen, (sx,sy), (sx+sw, sy+sh), (0,255,0), 2)
    roi_gray = gray[sy:sy+sh, sx:sx+sw]
    roi_color = imagen[sy:sy+sh, sx:sx+sw]


#Aquí es donde al compilar, lograremos ver la imagen ya con la detección
cv2.imshow('Detección', imagen)
cv2.imwrite('imagen.jpg', imagen)  #Guardar la imagen
cv2.waitKey(0)
cv2.destroyAllWindows()