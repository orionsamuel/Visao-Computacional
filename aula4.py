#Luma (Y)
# U projeção em azul
# V projeção em vermelho

import cv2

imagem = cv2.imread("imagem.jpg")


imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2YUV)

y, u, v = cv2.split(imagem)

cv2.imshow("Imagem original", imagem)
cv2.imshow("Canal y",y)
cv2.imshow("Canal u",u)
cv2.imshow("Canal v",v)

cv2.waitKey(0)
cv2.destroyAllWindows()
