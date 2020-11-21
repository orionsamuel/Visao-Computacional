import cv2

moedas = cv2.imread("moedas.jpg")
moedas = cv2.cvtColor(moedas,cv2.COLOR_BGR2GRAY)

metodo = cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV

retval, moeda_binarizada = cv2.threshold(moedas,0,200,metodo)

print("Valor do limiar")
print(retval)

cv2.imshow("Imagem original",moedas)
cv2.imshow("Imagem binarizada",moeda_binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
