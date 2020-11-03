# Harris Corner Detector

import cv2
import numpy as np

presente= cv2.imread("imagens/presente.jpg")
cinza= cv2.cvtColor(presente,cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem antes",presente)
#cantos= cv2.cornerHarris(cinza,blockSize=4,ksize=5,k=0.04)
cantos= cv2.cornerHarris(cinza,blockSize=4,ksize=5,k=0.01)
cantos= cv2.dilate(cantos,None)

presente[cantos>0.01*cantos.max()]=[0,0,0]


cv2.imshow("Cantos exibidos",presente)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Parâmetros
imagem-> Imagem a ser tratada
blockSize-> è o tamanho da vizinhança considerada para a detecção do canto
ksize-> Parâmetro da abertura da derivada de Sobel Usada
k-> Parâmetro livre do detector de Harris na equação
"""