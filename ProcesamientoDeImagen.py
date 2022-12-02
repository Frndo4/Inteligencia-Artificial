import cv2
import numpy as np
from cv2 import COLOR_BGR2GRAY     #IMPORTAR LIBRERÍA 
imagen = cv2.imread(r"C:\Users\fer-j\Pictures\imagen3.jpg")    #LEER IMAGEN

cv2.imshow('Foto', imagen)      #PLOTEAR IMAGEN
cv2.waitKey()                   #MOSTRAR VENTANA
print(imagen.shape[0:2])         #ANCHO Y ALTO

#Escala de grises
grises=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow("Escala de grises", grises)
cv2.waitKey()

#BORRDES
bordes=cv2.Canny(imagen, 100, 200)
cv2.imshow('Bordes', bordes)
cv2.waitKey()

#Para la detección de formas
bordes2=cv2.Canny(imagen, 100, 200)

#Suavizado de imagen
cnts, _=cv2.findContours(bordes2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, cnts, -1, (0,0,255), 2)
print("Formas encontradas", len(cnts))
texto="Formas detectadas" + str(len(cnts))

cv2.imshow('Bordes', bordes2)
cv2.imshow('Imagen', imagen)
cv2.waitKey()