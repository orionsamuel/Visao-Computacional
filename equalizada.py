import cv2

imagem = cv2.imread("mist.jpg",3)

azul, verde, vermelho= cv2.split(imagem)

azul_eq= cv2.equalizeHist(azul)
verde_eq= cv2.equalizeHist(verde)
vermelho_eq= cv2.equalizeHist(vermelho)

equalizada= cv2.merge((azul_eq,verde_eq,vermelho_eq))

cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Equalizada", equalizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
