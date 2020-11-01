import cv2
import numpy as np # Alias (apelido)

imagem = cv2.imread("imagem.jpg")

linhas, colunas= imagem.shape[:2]
"""
print("Linhas")
print(linhas)
print("Colunas")
print(colunas)
"""

matriz_traslacao= np.float32([[1,0,70],
                             [0,1,110]])

#imagem_trasnladada= cv2.warpAffine(imagem,matriz_traslacao,(colunas,linhas),cv2.INTER_LINEAR)
imagem_trasnladada= cv2.warpAffine(imagem,matriz_traslacao,(colunas+70,linhas+110),cv2.INTER_LINEAR)
cv2.imshow("Imagem transladada", imagem_trasnladada)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
T=[1 0 tx]
  [0 1 ty]

"""
