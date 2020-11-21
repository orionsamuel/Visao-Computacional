import cv2

placa= cv2.imread("balao_amarelo.bmp")

estrurante= cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

abertura= cv2.morphologyEx(placa,cv2.MORPH_OPEN,estrurante)

cv2.imshow("Balão",placa)
cv2.imshow("Balão com abertura", abertura)
cv2.waitKey(0)
cv2.destroyAllWindows()
