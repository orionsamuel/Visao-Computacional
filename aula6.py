# Mesclando canais de imagens

import cv2

imagem = cv2.imread("imagem.jpg")
imagem_hsv= cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV)

azul, verde, vermelho = cv2.split(imagem)
matiz, saturacao, valor = cv2.split(imagem_hsv)
#nova_imagem = cv2.merge((azul, verde,vermelho))
#nova_imagem = cv2.merge((azul,matiz,valor))
#nova_imagem = cv2.merge((matiz,vermelho,valor))
nova_imagem = cv2.merge((azul,matiz,saturacao))

cv2.imshow("Imagem misturada", nova_imagem)

#Salvando uma imagem com Opencv
cv2.imwrite("Nova_imagem.jpg",nova_imagem)

#cv2.imshow("Imagem em rgb", imagem)
#cv2.imshow("Imagem em Hsv", imagem_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()