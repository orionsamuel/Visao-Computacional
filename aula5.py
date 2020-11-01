# Convertendo RGB para tons de cinza

import cv2

imagem = cv2.imread("imagem.jpg")

imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

cv2.imshow("Imagem em tons de cinza", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()