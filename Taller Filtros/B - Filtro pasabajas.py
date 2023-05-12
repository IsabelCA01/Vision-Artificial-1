#Diseñar 2 mascaras de convolución, una paso bajo y otra paso alto, y
#aplicárselas a una imagen (No se puede usar las matrices ya definidas en
#las diapositivas, ni tampoco aplicar el filtro de la mediana como filtro pasa
#bajos).

import numpy as np
import cv2

#Filtro pasabajas
img1 = cv2.imread('Figura3.png')  # Leemos la imagen
height, width = img1.shape[:2]  # Obtenemos sus dimensiones
imgFpb = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
kern1 = np.ones((4, 4),np.float32)/16  # Creamos la matriz del kernel
imgFpb = cv2.filter2D(img1, ddepth=-1, kernel=kern1, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img1, imgFpb]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen


#Filtro pasa altas

imgFpa = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
kern = np.array([[2, -4, 2], [-4, 8, -4], [2, -4, 2]])
imgFpa = cv2.filter2D(img1, ddepth=-1, kernel=kern, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img1, imgFpa]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas
