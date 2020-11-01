# Trasformações projetivas

import cv2
import numpy as np

imagem= cv2.imread("imagem.jpg")


linha, coluna= imagem.shape[:2]

entrada_pontos= np.float32([[0,0],
                            [coluna-1,0],
                            [0,linha-1],
                            [coluna-1,linha-1]])

saida_pontos= np.float32([[0,0],
                          [coluna-1,0],
                          [int(0.33*coluna),linha-1],
                          [int(0.66*coluna),linha-1]])

matriz_projecao= cv2.getPerspectiveTransform(entrada_pontos,saida_pontos)

imagem_saida= cv2.warpPerspective(imagem, matriz_projecao,(linha,coluna))

cv2.imshow("Imagem de entrada", imagem)
cv2.imshow("Imagem de saida",imagem_saida)
cv2.waitKey(0)
cv2.destroyAllWindows()

