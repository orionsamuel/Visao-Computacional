#Trabalhando com escalas

import cv2


imagem= cv2.imread("imagem.jpg")

imagem_escalonada= cv2.resize(imagem,None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)
imagem_escalonada2= cv2.resize(imagem,None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
imagem_reduzida= cv2.resize(imagem,(450,450),interpolation=cv2.INTER_AREA)

cv2.imshow("Escala- interpolacao linear", imagem_escalonada)
cv2.imshow("Escala- interpolacao cubica", imagem_escalonada2)
cv2.imshow("Escala- interpolacao area", imagem_reduzida)
cv2.waitKey(0)
cv2.destroyAllWindows


""" 
0 0 0 0 0
0 0 0 0 0 
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
"""
