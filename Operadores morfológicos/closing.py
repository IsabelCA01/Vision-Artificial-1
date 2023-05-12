import numpy as np
import cv2

img = cv2.imread('17.JPG')  # Leemos la imagen
nSize = 1
height, width = img.shape[:2]  # Obtenemos sus dimensiones
imgGray = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, imgGray)
ret, thr = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY_INV)
# kernel = np.zeros((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize=(2*nSize+1, 2*nSize+1))
closing = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('Cierre', np.hstack([thr, closing]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas