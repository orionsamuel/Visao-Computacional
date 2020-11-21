#Shi-tomasi

import cv2

presente= cv2.imread("presente.jpg")
cinza= cv2.cvtColor(presente,cv2.COLOR_BGR2GRAY)

cantos= cv2.goodFeaturesToTrack(cinza,maxCorners=4,qualityLevel=0.05,minDistance=12)

for item in cantos:
    x,y=item[0]
    cv2.circle(presente,(x,y),10,-1)


cv2.imshow("As melhores k cantos",presente)
cv2.waitKey(0)
cv2.destroyAllWindows()



"""
Parâmetros

imagem-> Imagem que vai receber o tratamento
maxCorners-> número máximo de contos a serem retornados 
qualityLevel-> Parâmetro que caracteriza a qualidade mínima aceita dos cantos da imagem
minDistance-> Distância euclidiana mínima possível entre os cantos retornados.

"""
