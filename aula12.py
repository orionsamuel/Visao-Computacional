import cv2


vermelho= cv2.imread("balao_vermelho.bmp")
amarelo= cv2.imread("balao_amarelo.bmp")

#adicao= cv2.add(amarelo,vermelho)
adicao= cv2.add(vermelho,40)
adicao2= cv2.add(vermelho,-40)
#cv2.imshow("Vermelho",vermelho)
#cv2.imshow("Amarelo",amarelo)
cv2.imshow("Resultado final 1",adicao)
cv2.imshow("Resultado final 2",adicao2)

cv2.waitKey(0)
cv2.destroyAllWindows()