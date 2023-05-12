import numpy as np
import cv2
import math

# Translacion
img = cv2.imread('Blackpanther.jpeg', 0)
rows, cols = img.shape
cv2.imshow('Imagen inicial', img)
translation = np.float32([[1, 0, 125], [0, 1, 100]])
dst = cv2.warpAffine(img, translation, (cols+50, rows+50))
cv2.imshow('Translacion', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotacion

height, width = img.shape[:2]
rotation = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, rotation, (cols, rows))
cv2.imshow('Rotacion', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Shearing
transM = np.float32([[1, -math.tan(0.50), 0], [0, 1, 0]])
dst = cv2.warpAffine(img, transM, (cols, rows), cv2.INTER_LINEAR, cv2.BORDER_CONSTANT)
cv2.imshow('Shearing', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Shearing inv
transM = np.float32([[1, +math.tan(0.50), 0], [0, 1, 0]])
dst = cv2.warpAffine(img, transM, (cols, rows), cv2.INTER_LINEAR, cv2.BORDER_CONSTANT)
cv2.imshow('Shearing inv', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotacion inv

height, width = img.shape[:2]
rotation = cv2.getRotationMatrix2D((cols/2, rows/2), -90, 1)
dst = cv2.warpAffine(img, rotation, (cols, rows))
cv2.imshow('Rotacion inv', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Translacion inv 
img = cv2.imread('Blackpanther.jpeg', 0)
rows, cols = img.shape
translation = np.float32([[1, 0, -125], [0, 1,-100]])
dst = cv2.warpAffine(img, translation, (cols+50, rows+50))
cv2.imshow('Translacion imagen final', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
