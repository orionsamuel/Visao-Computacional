import cv2


# Carregar uma imagem utilizando o OpenCV
"""
imagem = cv2.imread("imagem.jpg")
cv2.imshow("Imagem exibida", imagem)
cv2.waitKey(1000)
cv2.destroyAllWindows()
"""

#Carregar um vídeo utilizando a biblioteca Opencv

"""
captura = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = captura.read()
    cv2.imshow("Video exibido", frame)

    if cv2.waitKey(60) & 0xFF == ord("q"):
        break

captura.release()
cv2.destroyAllWindows()
"""

captura = cv2.VideoCapture(0)

while True:
    ret, frame = captura.read()
    cv2.imshow("Webcan", frame)
    
    if cv2.waitKey(1) & 0xFF ==  ord("q"):
        break

cature.release()
cv2.destroyAllWindows()
