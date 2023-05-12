import cv2
import numpy as np

img= cv2.imread("Practica3_figura3a.png")
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#De RGB a HSV
hsv =cv2.cvtColor (img, cv2.COLOR_BGR2HSV)
cv2.imshow("En HSV", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

#segmentación
umbral_bajo = np.array([0, 135, 70],dtype=np.uint8)
umbral_alto= np.array([11, 255, 255],dtype=np.uint8)
mask=cv2.inRange(hsv, umbral_bajo, umbral_alto)
cv2.imshow("Segmentación", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

cont,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cont:
    area = cv2.contourArea(c)

print(f"El área en la segmentación HSV es: {area}")

#De RGB a escala de Grises 
gris =cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
cv2.imshow("En gris", gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

umbral_bajo1 = np.array([130],dtype=np.uint8)
umbral_alto1 = np.array([130],dtype=np.uint8)
_,binarizada = cv2.threshold(gris, 145, 255,cv2.THRESH_BINARY_INV)
cv2.imshow("Segmentación escala de grises", binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
cont,_ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cont:
    area = cv2.contourArea(c)

print(f"El área en la segmentación escala de grises es: {area}")

luv =cv2.cvtColor (img, cv2.COLOR_BGR2LUV)
cv2.imshow("En LUV", luv)
cv2.waitKey(0)
cv2.destroyAllWindows()

umbral_bajo3 = np.array([99, 110, 150],dtype=np.uint8)
umbral_alto4= np.array([219, 138, 174],dtype=np.uint8)
maskluv=cv2.inRange(luv, umbral_bajo3, umbral_alto4)
maskluv = cv2.bitwise_not(maskluv)
cv2.imshow("Segmentación LUV", maskluv)
cv2.waitKey(0)
cv2.destroyAllWindows()
cont,_ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cont:
    area = cv2.contourArea(c)

print(f"El área en la segmentación escala de grises es: {area}")

lab =cv2.cvtColor (img, cv2.COLOR_BGR2LAB)
cv2.imshow("En LAB", lab)
cv2.waitKey(0)
cv2.destroyAllWindows()

umbral_bajo5 = np.array([150, 100, 0],dtype=np.uint8)
umbral_alto6= np.array([230, 255, 255],dtype=np.uint8)
masklab=cv2.inRange(lab, umbral_bajo5, umbral_alto6)
masklab = cv2.bitwise_not(masklab)
cv2.imshow("Segmentación LAB", masklab)
cv2.waitKey(0)
cv2.destroyAllWindows()