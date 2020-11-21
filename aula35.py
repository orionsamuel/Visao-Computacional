import cv2


roda= cv2.imread("predios.jpg")
estruturante= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
gradiente= cv2.morphologyEx(roda,cv2.MORPH_GRADIENT,estruturante)
dilatacao= cv2.dilate(roda,estruturante,iterations=1)
erosao= cv2.erode(roda,estruturante,iterations=1)
diferenca= cv2.subtract(dilatacao,erosao)





cv2.imshow("Imagem original",roda)
cv2.imshow("imagem com gradiente morfologico",gradiente)
cv2.imshow("Imagem com diferenca",diferenca)
cv2.waitKey(0)
cv2.destroyAllWindows()
