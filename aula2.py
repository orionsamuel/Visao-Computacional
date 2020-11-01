# Espaço de cor RGB

#Red (vermelho)
#Green (verde)
#Blue (azul)

import cv2

imagem = cv2.imread("imagem.jpg")

azul, verde, vermelho = cv2.split(imagem) # A biblioteca OpenCv trata o espaço RGB como BGR

#[[azul],[verde],[vermelho]]

cv2.imshow("Imagem Original", imagem)
cv2.imshow("Canal azul", azul)
cv2.imshow("Canal verde",verde)
cv2.imshow("Canal vermelho",vermelho)

cv2.waitKey(0)
cv2.destroyAllWindows()