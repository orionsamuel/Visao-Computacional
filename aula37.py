import cv2

placa = cv2.imread("placa.jpg")
placa = cv2.cvtColor(placa,cv2.COLOR_BGR2GRAY)
metodo = cv2.THRESH_BINARY_INV
metodo2 = cv2.THRESH_BINARY

retval,placa_binarizada= cv2.threshold(placa,113,255,metodo)
retval2,placa_binarizada2= cv2.threshold(placa,210,255,metodo2)

cv2.imshow("Placa original",placa)
cv2.imshow("Placa binario",placa_binarizada)
cv2.imshow("Placa binario 2",placa_binarizada2)
print("Valor do retval")
print(retval)
print("Valor do retval2")
print(retval2)
cv2.waitKey(0)
cv2.destroyAllWindows()
