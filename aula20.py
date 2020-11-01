import cv2

import numpy as np

mist= cv2.imread("mist.jpg")


matriz1= np.array([[-1,-1,-1],
                   [-1,9,-1],
                   [-1,-1,-1]])

matriz2= np.array([[1,1,1],
                   [1,-7,1],
                   [1,1,1]])

matriz3= np.array([[-1,-1,-1,-1,-1],
                   [-1,2,2,2,-1],
                   [-1,2,8,2,-1],
                   [-1,-1,-1,-1,-1]])/8.0


filtro1= cv2.filter2D(mist,-1,matriz1)
filtro2= cv2.filter2D(mist,-1,matriz2)
filtro3= cv2.filter2D(mist,-1,matriz3)

cv2.imshow("Imagem original",mist)
cv2.imshow("Imagem com filtro 1",filtro1)
cv2.imshow("Imagem com filtro 2",filtro2)
cv2.imshow("Imagem com filtro 3",filtro3)
cv2.waitKey(0)
cv2.destroyAllWindows()
