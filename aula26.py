import cv2

ressonancia= cv2.imread("ressonancia.jpg")

ressonancia_suavizada= cv2.GaussianBlur(ressonancia,(5,5),7)

ressonancia_detalhada= cv2.subtract(ressonancia,ressonancia_suavizada)

ressonancia_com_realce= cv2.add(ressonancia,ressonancia_detalhada)


cv2.imshow("Ressonancia original", ressonancia)
cv2.imshow("Ressonancia Suavizada", ressonancia_suavizada)
cv2.imshow("Ressonancia detalhada",ressonancia_detalhada)
cv2.imshow("Ressonancia com realce",ressonancia_com_realce)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
imagem_detalhada= imagem_original-imagem_suavizada
imagem_realçada= imagem_original+ imagem_detalhada

"""
