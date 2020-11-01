import cv2
import numpy as np

predio= cv2.imread("predios.jpg")
predio= cv2.cvtColor(predio, cv2.COLOR_BGR2GRAY)

relevo1= np.array([[0,-1,-1],
                   [1,0,1],
                   [1,1,0]])

relevo2= np.array([[-1,-1,0],
                   [-1,0,1],
                   [0,1,1]])

relevo3= np.array([[1,0,0],
                   [0,0,0],
                   [0,0,-1]])



predio_rele1= cv2.filter2D(predio,-1,relevo1)+128
predio_rele2= cv2.filter2D(predio,-1,relevo1)+156
predio_rele3= cv2.filter2D(predio,-1,relevo1)+200
#predio_rele2= cv2.filter2D(predio,-1,relevo2)+200
#predio_rele3= cv2.filter2D(predio,-1,relevo3)+200

cv2.imshow("Filtro 1", predio_rele1)
cv2.imshow("Filtro 2", predio_rele2)
cv2.imshow("Filtro 3", predio_rele3)
cv2.waitKey(0)
cv2.destroyAllWindows()
