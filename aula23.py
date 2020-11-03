import cv2

garagem= cv2.imread("garagem.jpg")
#garagem= cv2.cvtColor(garagem, cv2.COLOR_BGR2GRAY)
gaussiana= cv2.GaussianBlur(garagem,(7,7),3)

laplaciana_g= cv2.Laplacian(gaussiana,cv2.CV_8U)
laplaciana_g= cv2.add(laplaciana_g,laplaciana_g)
operador_laplaciano= cv2.Laplacian(garagem, cv2.CV_8U)
cv2.imshow("Imagem original",garagem)
cv2.imshow("Imagem filtro laplaciano",operador_laplaciano)
cv2.imshow("Imagem filtro laplaciano apos o gaussianblur",laplaciana_g)

cv2.waitKey(0)
cv2.destroyAllWindows()
