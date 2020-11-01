import cv2


imagem= cv2.imread("imagens/caleidoscopio.jpg") # Lendo um arquivo que está em outro diretório
cv2.imshow("Apenas um teste",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()