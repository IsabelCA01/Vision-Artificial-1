#Para cada una de las imágenes adjuntas a continuación (figura 2, 3 y 4),
#defina el tipo de ruido que la afecta, aplique los filtros aprendidos en clase,
#muestre los resultados y concluya cuál obtuvo el mejor resultado y por qué.


import numpy as np
import cv2

img1 = cv2.imread('Figura1.png')  # Leemos la imagen
height, width = img1.shape[:2]  # Obtenemos sus dimensiones
imgFpb = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
kern1 = np.ones((4, 4),np.float32)/16  # Creamos la matriz del kernel
imgFpb = cv2.filter2D(img1, ddepth=-1, kernel=kern1, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img1, imgFpb]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen

cv2.destroyAllWindows()  # Cierre de ventanas


