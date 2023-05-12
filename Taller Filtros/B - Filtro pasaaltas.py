import numpy as np
import cv2

img1 = cv2.imread('Figura1.png', 0)  # Leemos la imagen
height, width = img1 .shape[:2]  # Obtenemos sus dimensiones
imgFpa = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
kern = np.array([[2, -4, 2], [-4, 8, -4], [2, -4, 2]])
imgFpa = cv2.filter2D(img1, ddepth=-1, kernel=kern, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img1, imgFpa]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas

