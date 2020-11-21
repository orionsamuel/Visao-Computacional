import cv2

epiderme= cv2.imread("predios.jpg")
epiderme= cv2.cvtColor(epiderme,cv2.COLOR_BGR2GRAY)

estrurante= cv2.getStructuringElement(cv2.MORPH_CROSS,(100,100))

epiderme_abertura= cv2.morphologyEx(epiderme,cv2.MORPH_OPEN,estrurante)
#epiderme_abertura= cv2.morphologyEx(epiderme,cv2.MORPH_CLOSE,estrurante)
epiderme_subtracao= cv2.subtract(epiderme,epiderme_abertura)
epiderme_final= cv2.add(epiderme_subtracao,epiderme_subtracao)



cv2.imshow("Imagem original",epiderme)
cv2.imshow("Imagem com abertura",epiderme_abertura)
cv2.imshow("Imagem com subtracao",epiderme_subtracao)
cv2.imshow("Imagem final",epiderme_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
