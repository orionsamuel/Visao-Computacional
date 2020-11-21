# Acessar e modificar valores de pixels

import cv2

imagem= cv2.imread("imagem.jpg")

"""
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

#[[Azul],[Verde], [Vermelho]]

linha, coluna= imagem.shape[:2]
"""
print("linha")
print(linha)
print("Coluna")
print(coluna)
"""

#pixel= imagem[linha,coluna]
pixel= imagem[150,150]
print("Valor do pixel")
print(pixel)
#Valor do pixel é uma lista [176  99  42]

cinza= cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
"""
cv2.imshow("Cinza",cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
pixel_cinza= cinza[150,150]
print("Valor do pixel cinza")
print(pixel_cinza)

imagem[150,150]= [255,255,255]
print("Pixel alterado")
print(imagem[150,150])

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()


















