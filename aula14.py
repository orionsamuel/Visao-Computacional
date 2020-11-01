#addWeighted

#1- imagem 1-> A primeira imagem que queremos misturar
#2- alpha->  Intensidade da primeira imagem (vária de 0.0 a 1.0)
#3- imagem 2-> A segunda imagem que queremos misturar
#4- beta-> Referente a intensidade da segunda imagem (vária de 0.0 a 1.0)
#5- gamma-> valor escalar adionado a cada soma

import cv2 

vermelho= cv2.imread("balao_vermelho.bmp")
amarelo= cv2.imread("balao_amarelo.bmp")

mistura= cv2.addWeighted(vermelho, 0.5, amarelo,0.7,0.9)

cv2.imshow("Resultado final", mistura)
cv2.waitKey(0)
cv2.destroyAllWindows()