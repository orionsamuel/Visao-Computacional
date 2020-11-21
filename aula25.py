#1- Imagem que será tratada em tons de cinza
#2- 2,3- Intensidade


import cv2

garagem= cv2.imread("garagem.jpg")
cinza=  cv2.cvtColor(garagem, cv2.COLOR_BGR2GRAY)

canny_colorida= cv2.Canny(garagem,100,200)
canny_cinza= cv2.Canny(cinza,100,200)

cv2.imshow("Imagem original",garagem)
cv2.imshow("Imagem colorida com filtro Canny",canny_colorida)
cv2.imshow("Imagem cinza com filtro Canny",canny_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
