import cv2
video=cv2.VideoCapture(0)
while(True):
    ret, frame=video.read()   #Mostrar frame
    cv2.imshow('Video', frame)

    #Bordes
    bordes=cv2.Canny(frame, 100, 200)
    cv2.imshow('Bordes', bordes)

    #Escala de grises
    gris=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Escala de grises', gris)
    
    #Para la detección de formas
    imagen_1=cv2.Canny(gris, 100, 200)

    #Suavizado de imagen
    cnts, _=cv2.findContours(imagen_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(gris, cnts, -1, (0,255,0), 3)
    print("Formas encontradas", len(cnts)-10)
    texto="Formas detectadas" + str(len(cnts)-10)


    if cv2.waitKey(1) & 0xFF == ord ('s'):
        break

#Finalizar cámara
video.release()
cv2.destroyAllWindows()