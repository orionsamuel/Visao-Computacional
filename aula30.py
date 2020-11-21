import cv2

roda= cv2.imread("balao_amarelo.bmp")

estruturante= cv2.getStructuringElement(cv2.MORPH_CROSS,(13,13))

erosao= cv2.erode(roda,estruturante,iterations=3)

cv2.imshow("Balão amarelo original",roda)
cv2.imshow("Balão amarelo tratado",erosao)
cv2.waitKey(0)
cv2.destroyAllWindows()
