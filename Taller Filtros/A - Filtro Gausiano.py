import numpy as np
import cv2

imgA = cv2.imread('Figura4.png', 0)  # Leemos la imagen

imgB = cv2.GaussianBlur(imgA, (35, 35), sigmaX=0, sigmaY=0)  # Aplicamos el kernel a la imagen con la funcion filter2D

cv2.imshow('Imagen A                               Imagen B', np.hstack([imgA, imgB]))  # Mostramos las imagenes

add1 = cv2.addWeighted(imgA, 0.3, imgB, 0.7, 0)
imgC1 = add1 - 34

imgC2 = imgA*0.3 + imgB*0.7 - 34

cv2.imshow('Imagen C1                              Imagen C2', np.hstack([imgC1, imgC2]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas

