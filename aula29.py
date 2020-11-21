# Elemento estruturante

import cv2
import numpy as np
#Retangular

retangular= cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
print("Elemento estruturante retangular:")
print(retangular)

#Eliptico

eliptico= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
print("Elemento estruturante eliptico:")
print(eliptico)

#Cruz

cruz= cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
print("Elemento estruturante cruz:")
print(cruz)


meu_elemento= np.array([0 0 0 1],
                       [0 0 0 1],
                       [1 1 1 1],
                       [0 0 0 1])