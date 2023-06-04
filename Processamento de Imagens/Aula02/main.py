import cv2

im = cv2.imread('teste.jpg')


cv2.imshow("modificada", im+im)
cv2.waitKey(0) #espera pressionar qualquer tecla pra fechar, se nao fecha automatico
