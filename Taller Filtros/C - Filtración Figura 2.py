#Imagen 2: Ruido blanco?

#filtro mediana 
import numpy as np
import cv2

img1 = cv2.imread('Figura2.png')  # Leemos la imagen
height, width = img1.shape[:2]  # Obtenemos sus dimensiones
imgFm = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
imgFm = cv2.medianBlur(img1, 3)
cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img1, imgFm]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen


imgFsh = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
kern1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
imgFsh = cv2.filter2D(imgFm, ddepth=-1, kernel=kern1, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow('Imagen filtro mediana                               Imagen filtro sharpen', np.hstack([imgFm, imgFsh]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas
