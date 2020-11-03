#sobel

### Parâmetros obrigatórios

#1 - Imagem que receberá o operador
#2 - O tipo de variável que armazenará o valor que representa o pixel quando o valor do parâmetro é definido
#3,4 - Definir como o realce será aplicado
#5 - É o tamanho da máscara de filtragem

import cv2

garagem = cv2.imread("garagem.jpg")
garagem = cv2.cvtColor(garagem, cv2.COLOR_BGR2GRAY)

sobel_horizontal = cv2.Sobel(garagem, cv2.CV_64F, 1, 0, ksize = 3)
sobel_vertical = cv2.Sobel(garagem, cv2.CV_64F, 0, 1, ksize = 3)

cv2.imshow("Imagem original", garagem)
cv2.imshow("Sobel horizontal", sobel_horizontal)
cv2.imshow("Sobel vertical", sobel_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
