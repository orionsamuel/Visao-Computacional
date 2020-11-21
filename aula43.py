import cv2

hexagono= cv2.imread("imagens/hexagono.png",0)

tipo= cv2.THRESH_BINARY_INV
retval,hexagono_binzarizado= cv2.threshold(hexagono,127,255,tipo)

#Obter contornos
modo=cv2.RETR_TREE
metodo= cv2.CHAIN_APPROX_SIMPLE
contornos, hierarquia= cv2.findContours(hexagono_binzarizado,modo,metodo)

#Recuperar os contornos
obj= contornos[0]

#Calcular a área

area= cv2.contourArea(obj)

perimetro= cv2.arcLength(obj,False)

print("Área calculada")
print(area)
#print(hierarquia)
print("Perímetro calculado")
print(perimetro)

#####
#Perímetro
######

"""
cv2.imshow("hexagono",hexagono_binzarizado)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
Outros modos
RETR_EXTERNAL
RETR_LIST
RETR_CCOMP
RETR_TREE
"""

"""
CHAIN_APPROX_NONE
CHAIN_APPROX_SIMPLE
CHAIN_APPROX_TC89_L1
CHAIN_APPROX_TC89_KCOS
"""