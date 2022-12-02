import cv2
imagen = cv2.imread(r"C:\Users\fer-j\Documents\Python\coins.png")
cv2.imshow('Foto', imagen)      #PLOTEAR IMAGEN
cv2.waitKey()                   

#Borrosa
borrosa=cv2.GaussianBlur(imagen, (5,5), 4)
cv2.imshow("Ruido", borrosa)
cv2.waitKey()

#Para la detección de formas
imagen_1=cv2.Canny(borrosa, 100, 200)

#Suavizado de imagen
cnts, _=cv2.findContours(imagen_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(borrosa, cnts, -1, (0,0,255), 2)
print("Formas encontradas", len(cnts))
texto="Formas detectadas" + str(len(cnts))

cv2.imshow('Bordes', imagen_1)
cv2.imshow('Imagen', borrosa)
cv2.waitKey()