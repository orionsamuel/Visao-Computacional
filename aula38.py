import cv2

moedas= cv2.imread("moedas.jpg")
moedas= cv2.cvtColor(moedas,cv2.COLOR_BGR2GRAY)
moedas_mb= cv2.medianBlur(moedas,5)

modo=cv2.ADAPTIVE_THRESH_GAUSSIAN_C
metodo=cv2.THRESH_BINARY_INV

moeda_binarizada= cv2.adaptiveThreshold(moedas_mb,255,modo,metodo,7,5)


cv2.imshow("Moedas original",moedas)
cv2.imshow("Moedas com medianblur",moedas_mb)
cv2.imshow("Moedas Binarizada",moeda_binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
