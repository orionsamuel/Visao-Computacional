import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem= cv2.imread("mist.jpg",3)

#plt.hist(imagem.ravel(),256,[0,256])
#plt.show()
"""
cv2.imshow("Mist", imagemq)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
azul, verde, vermelho= cv2.split(imagem)

azul_eq= cv2.equalizeHist(azul)
verde_eq= cv2.equalizeHist(verde)
vermelho_eq= cv2.equalizeHist(vermelho)



equalizada= cv2.merge((azul_eq,verde_eq,vermelho_eq))
plt.hist(imagem.ravel(),256,[0,256])
plt.figure()
plt.hist(equalizada.ravel(),256,[0,256])
plt.show()
"""
cv2.imshow("Imagem equalizada", equalizada)
cv2.imshow("Imagem original", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""