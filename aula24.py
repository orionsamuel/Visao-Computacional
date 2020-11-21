import cv2

imagem= cv2.imread("ressonancia.jpg")

laplaciano= cv2.Laplacian(imagem, cv2.CV_8U)
realce= cv2.subtract(imagem,laplaciano)


cv2.imshow("Imagem original",imagem)
cv2.imshow("Imagem com filtro",laplaciano)
cv2.imshow("Imagem com com filtro e realce",realce)
cv2.waitKey(0)
cv2.destroyAllWindows()
