import cv2
video=cv2.VideoCapture(0)
while(True):
    ret, frame=video.read()   #Mostrar frame
    cv2.imshow('Video', frame)

    #Escala de grises
    gris=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Escala de grises', gris)

    #Bordes
    bordes=cv2.Canny(frame, 100, 200)
    cv2.imshow('Bordes', bordes)

    if cv2.waitKey(1) & 0xFF == ord ('s'):
        break

#Finalizar cámara
video.release()
cv2.destroyAllWindows()