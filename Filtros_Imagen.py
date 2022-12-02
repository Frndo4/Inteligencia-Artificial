def sp_noise(image, prob):
    'Agregar ruido sal y pimienta'
    output=np.zeros(image.shape, np.uint8)
    thres=1-prob

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn=random.random()
            if(rdn<prob):
                output[i][j]=0
            elif rdn>thres:
                output[i][j]=225
            else:
                output[i][j]=image[i][j]
        return output

def gasuss_noise(image, mean=0, var=0.001):
    image=np.array(image/255, dtype=float)
    noise=np.random.normal(mean, var**0.5, image.shape)
    out=image+noise
    if out.min()<0:
        low_clip=-1.
    else:
        low_clip=0.
    out=np.clip(out, low_clip, 1.0)
    out=np.uint8(out*255)
    return out

import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread(r"C:\Users\fer-j\Pictures\pai.jpg")

#FILTRO DE CONVOLUCION DE 2 DIMENSIONES con un kernel
kernel=np.ones((3,3),np.float32)/9
f1=cv2.filter2D(img,-1, kernel) #IMAGEN, PROFINDIDAD, Y KERNEL
f2=cv2.blur(img,(3,3)) #FILTRO PROMEDIO
f3=cv2.GaussianBlur(img,(3,3),0) #GAUSIANO
f4=cv2.medianBlur(img,3) #mediano


#Agregar ruido de sal y pimienta P=0.02
out1=sp_noise(img, prob=0.02)

#Agrega ruido gaussiano
out2=gasuss_noise(img, mean=0, var=0.01)

titles=['Imagen original', 'Sal y pimienta', 'Gauss', 'Convolución', 'Promedio', 'Gaussiano', 'Mediano']
images=[img, out1, out2, f1, f2, f3, f4]

plt.figure(figsize=(10, 5))
for i in range(7):
    plt.subplot(1, 7, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


#plt.show()
#cv2.imshow('imagenReal', img)
#cv2.imshow('imagenRuido', out1)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
