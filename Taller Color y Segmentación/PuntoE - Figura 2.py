
import cv2
import numpy as np

img= cv2.imread("Practica3_figura2peque.png")
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#De RGB a escala de Grises 
gris =cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
cv2.imshow("En gris", gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

#De RGB a HSV
hsv =cv2.cvtColor (img, cv2.COLOR_BGR2HSV)
cv2.imshow("En HSV", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()


umbral_bajo = np.array([6, 0, 0],dtype=np.uint8)
umbral_alto= np.array([7, 205, 205],dtype=np.uint8)
mask=cv2.inRange(hsv, umbral_bajo, umbral_alto)
cv2.imshow("Segmentación 2", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

cont,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cont:
    area = cv2.contourArea(c)
cv2.imshow('Calculo de Area y Reconocimiento de imagen', mask)
print(area)
cv2.waitKey(0)
cv2.destroyAllWindows()

#De RGB a escala de Grises 
gris =cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
cv2.imshow("En gris", gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

_,binarizada = cv2.threshold(gris,200, 255,cv2.THRESH_BINARY_INV)
cv2.imshow("Segmentación escala de grises", binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
cont,_ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cont:
    area = cv2.contourArea(c)

print(f"El área en la segmentación escala de grises es: {area}")

