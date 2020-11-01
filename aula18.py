import cv2
import numpy as np

predio= cv2.imread("predios.jpg")

matriz33= np.ones((3,3),np.float32)/9.0
matriz55= np.ones((5,5),np.float32)/25.0

#print("Matriz33")
#print(matriz33)
#print("Matriz55")
#print(matriz55)


filtro33= cv2.filter2D(predio,-1,matriz33)
filtro55= cv2.filter2D(predio,-1,matriz55)
filtroblur= cv2.blur(predio,(3,3))

cv2.imshow("Filtro matriz 3x3", filtro33)
cv2.imshow("Filtro com blur do opencv", filtroblur)
#print(matriz33)

cv2.imshow("Imagem original",predio)
cv2.waitKey(0)
cv2.destroyAllWindows()
