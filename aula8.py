# Rotação de imagens

import cv2
import numpy as np

imagem= cv2.imread("imagem.jpg")

colunas, linhas= imagem.shape[:2]

#matriz_rotacao= cv2.getRotationMatrix2D((colunas/2, linhas/2),30,0.7)
matriz_rotacao= cv2.getRotationMatrix2D((colunas/4, linhas/2),45,0.3)
imagem_rotacionada= cv2.warpAffine(imagem, matriz_rotacao, (colunas,linhas))

cv2.imshow("Imagem rotacionada",imagem_rotacionada)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""
R= [cos(theta) -sin(theta)]
   [sin(theta)  cos(theta)]

"""
