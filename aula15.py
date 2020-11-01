import cv2
import numpy as np


video= cv2.VideoCapture(0)
mascara= np.zeros((480,640),dtype=np.uint8)
mascara= cv2.circle(mascara,(320,240),125,(255,255,255),-1)


while True:
    ret,frame= video.read()
    imagem_mascara= cv2.bitwise_and(frame,frame,mask=mascara)
    cv2.imshow("Imagem mascara",imagem_mascara)

    if cv2.waitKey(0) & 0XFF==ord('q'):
        break

video.release()
cv2.destroyAllWindows()




"""
circulo= cv2.imread("circulo.bmp")
retangulo=cv2.imread("retangulo.bmp")

cv2.imshow("Circulo",circulo)
cv2.imshow("Retangulo",retangulo)


##Operador and

operador_and=cv2.bitwise_and(circulo,retangulo)
operador_or=cv2.bitwise_or(circulo,retangulo)
operador_not=cv2.bitwise_not(circulo)
operador_xor= cv2.bitwise_xor(circulo,retangulo)
#cv2.imshow("Operador and",operador_and)
#cv2.imshow("Operador or",operador_or)
#cv2.imshow("Operador not",operador_not)
cv2.imshow("Operador xor",operador_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()


p -> sentença 1
q -> sentença 2

Tabela verdade 
############################Operador and####################################

p             q             p and q

verdadeiro   verdadeiro      verdadeiro
verdadeiro   falso           falso
falso        verdadeiro      falso
falso        falso           falso   

imagem1 (circulo)      q ( retangulo)             p and q
branco                 branco                     branco
branco                 preto                      preto
preto                  branco                     preto
preto                  preto                      preto 

############################Operador Or####################################
p             q             p or q

verdadeiro   verdadeiro      verdadeiro
verdadeiro   falso           verdadeiro
falso        verdadeiro      verdadeiro
falso        falso           falso   

imagem1 (circulo)      q ( retangulo)             p or q
branco                 branco                     branco
branco                 preto                      branco
preto                  branco                     branco
preto                  preto                      preto 

############################Operador not####################################
p             not p (não p)      

verdadeiro   falso      
falso        verdadeiro           
 

imagem1 (circulo)      not imagem            
branco                 preto
preto                  branco     

############################Operador xor####################################

p             q             p xor q

verdadeiro   verdadeiro      falso
verdadeiro   falso           verdadeiro
falso        verdadeiro      verdadeiro
falso        falso           falso   

imagem1 (circulo)      imagem2 ( retangulo)       imagem1 xor imagem2
branco                 branco                     preto
branco                 preto                      branco
preto                  branco                     branco
preto                  preto                      preto 

"""
