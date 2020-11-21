import cv2
import numpy as np


ludo_rgb= cv2.imread("imagens/ludo.jpg")
ludo_hsv= cv2.cvtColor(ludo_rgb,cv2.COLOR_BGR2HSV)

azul_rgb= np.uint8([[[255,0,0]]])
azul_hsv= cv2.cvtColor(azul_rgb,cv2.COLOR_BGR2HSV)

limite_inferior= azul_hsv-50
limite_superior= azul_hsv+50

ludo_segmentado= cv2.inRange(ludo_hsv,limite_inferior,limite_superior)


cv2.imshow("Ludo",ludo_rgb)
cv2.imshow("Ludo segmentado",ludo_segmentado)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

azul_rgb= np.uint8([[[255,0,0]]])
azul_hsv= cv2.cvtColor(azul_rgb,cv2.COLOR_BGR2HSV)

print(azul_rgb)
print(azul_hsv)
"""