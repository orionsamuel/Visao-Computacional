import cv2

roda= cv2.imread("balao_amarelo.bmp")

estruturante= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

diltada= cv2.dilate(roda,estruturante,iterations=3)
cv2.imshow("Imagem original", roda)
cv2.imshow("Imagem dilatada", diltada)
cv2.waitKey(0)
cv2.destroyAllWindows()
