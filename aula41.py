import cv2
import numpy as np

balao1= cv2.imread("imagens/balao_vermelho.bmp")

balao2= cv2.imread("imagens/balao_vermelho2.bmp")
subtracao_rgb= cv2.subtract(balao1,balao2)
subtracao_hsv= cv2.cvtColor(subtracao_rgb,cv2.COLOR_BGR2HSV)

limite_inferior= np.array([90,90,90])
limite_superior= np.array([180,255,255])

imagem_segmentada= cv2.inRange(subtracao_hsv, limite_inferior,limite_superior)


cv2.imshow("Resultado", subtracao_rgb)
cv2.imshow("Resultado final",imagem_segmentada)
cv2.waitKey(0)
cv2.destroyAllWindows()