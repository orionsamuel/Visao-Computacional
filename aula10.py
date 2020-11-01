#Tranformações afins

import cv2
import numpy as np

imagem= cv2.imread("imagem.jpg")

coluna, linha= imagem.shape[:2]

entrada_ponto= np.float32([[0,0],
                         [linha-1,0],
                         [0,coluna-1]])


saida_ponto= np.float32([[0,0],
                         [int(0.6*(linha-1)),0 ],
                         [int(0.4*(linha-1)),coluna-1]])

matriz_affine= cv2.getAffineTransform(entrada_ponto,saida_ponto)

imagem_saida= cv2.warpAffine(imagem, matriz_affine,(coluna,linha))

cv2.imshow("Entrada", imagem)
cv2.imshow("Saída", imagem_saida)
cv2.waitKey(0)
cv2.destroyAllWindows()
