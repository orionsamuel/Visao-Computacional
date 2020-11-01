import cv2


posicao1= cv2.imread("balao_vermelho.bmp")
posicao2= cv2.imread("balao_vermelho2.bmp")

#cv2.imshow("Posicao 1", posicao1)
#cv2.imshow("Posicao 2", posicao2)

subtracao = cv2.subtract(posicao1, posicao2)
cv2.imshow("Resultado final", subtracao)


cv2.waitKey(0)
cv2.destroyAllWindows()