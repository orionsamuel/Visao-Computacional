import cv2

placa= cv2.imread("balao_amarelo.bmp")

estruturante= cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

fechamento= cv2.morphologyEx(placa,cv2.MORPH_CLOSE,estruturante)

cv2.imshow("Balão original",placa)
cv2.imshow("Balão com fechamento",fechamento)
cv2.waitKey(0)
cv2.destroyAllWindows()
