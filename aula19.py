import cv2
import numpy as np

predio= cv2.imread("predios.jpg")

tamanho=15

matriz_desfoque= np.zeros((tamanho,tamanho))
matriz_desfoque[int(tamanho-1/2),:]= np.ones(tamanho)
matriz_desfoque= matriz_desfoque/tamanho
#print(matriz_desfoque)


imagem_mov= cv2.filter2D(predio, -1,matriz_desfoque)

cv2.imshow("Imagem original", predio)
cv2.imshow("Imagem com filtro", imagem_mov)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
matriz_33= [0 0 0]
           [1 1 1]
           [0 0 0]

matriz33= [0 1 0]
          [0 1 0]
          [0 1 0]
"""
