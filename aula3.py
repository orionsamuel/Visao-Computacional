#Hue (matiz)
#Saturation (saturação)
#Value (valor)


import cv2
imagem = cv2.imread("imagem.jpg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

cv2.imshow("Imagem em HSV- original", imagem)

matiz, saturacao, valor = cv2.split(imagem)

cv2. imshow("Matiz", matiz)
cv2. imshow("Suturação", saturacao)
cv2. imshow("Valor", valor)

cv2.waitKey(0)
cv2.destroyAllWindows()