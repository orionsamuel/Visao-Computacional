#Histograma em uma imagem binária

import cv2
import numpy as np
import matplotlib.pyplot as plt

#imagem= cv2.imread("parede.jpg")

"""
cv2.imshow("Imagem",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


#plt.hist(imagem.ravel(),256,[0,256])
#plt.show()
"""
Histograma de em tons de cinza
"""

imagem= cv2.imread("imagem.jpg")
cinza= cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
"""
cv2.imshow("cinza",cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

plt.hist(cinza.ravel(),256,[0,256])
plt.show()

"""
Histograma de imagem em RGB
"""

azul, verde, vermelho= cv2.split(imagem)

plt.hist(azul.ravel(),256,[0,256])
plt.figure()
plt.hist(verde.ravel(),256,[0,256])
plt.figure()
plt.hist(vermelho.ravel(),256,[0,256])
plt.show()

















