import cv2
import numpy as np
import imutils

black = (0,0,0)
imOrig = cv2.imread('FotoCachorros.jpg')
imMani = imOrig.copy()
# Recorta os cachorros em imagens diferentes
recorte1 = imMani[100:450,100:290]
recorte2 = imMani[100:320,290:470]
recorte3 = imMani[230:450,290:500]
recorte4 = imMani[50:390,475:628]
recorte5 = imMani[230:450,490:720]
recorte6 = imMani[100:430,680:850]

#Adiciona uma máscara em cima dos cachorros
mascara = np.zeros(imMani.shape[:2], dtype="uint8")

cv2.rectangle(mascara,(80,95),(300,450),255,-1)
cv2.rectangle(mascara,(300,100),(475,300),255,-1)
cv2.rectangle(mascara,(200,240),(500,450),255,-1)
cv2.rectangle(mascara,(480,50),(630,320),255,-1)
cv2.rectangle(mascara,(480,225),(715,450),255,-1)
cv2.rectangle(mascara,(690,110),(850,450),255,-1)

im_mask = cv2.bitwise_and(imMani,imMani,mask= mascara)

#Rotaciona a imagem com o centro no meio da imagem
(alt,larg) = imMani.shape[:2]

meio = (larg //2,alt//2)

M1 = cv2.getRotationMatrix2D(meio,45,1.0)

img_rotac_centro = cv2.warpAffine(imMani,M1,(larg,alt))

#Rotaciona a Imagem com o centro no cachorro mais abaixo e direita da imagem
Cachorro_mais_direita = (597,337)

M2 = cv2.getRotationMatrix2D(Cachorro_mais_direita,-30,1.0)

img_rotac_Cachorro = cv2.warpAffine(imMani,M2,(larg,alt))

#reduz a imagem do maior cachorro pela metade
Cachorro_Maior = recorte1.copy()

prop = 100.0/ Cachorro_Maior.shape[1]

tam_novo1 = (int(Cachorro_Maior.shape[1]*prop), int(Cachorro_Maior.shape[0]*prop))

Cachorro_Maior_redm = cv2.resize(Cachorro_Maior,tam_novo1, interpolation=cv2.INTER_AREA)


#Amplia a imagem do menor cachorro duas vezes

Cachorro_Menor = recorte3.copy()

tam_novo2 = (Cachorro_Menor.shape[1]*2,Cachorro_Menor.shape[0]*2)

Cachorro_Menor_redm = cv2.resize(Cachorro_Menor,tam_novo2, interpolation=cv2.INTER_AREA)

#Flip Horizontal, Flip Vertical e Flip Horizontal e vertical

Cachorro_Maior_FH = cv2.flip(Cachorro_Maior,1)
Cachorro_Maior_FV = cv2.flip(Cachorro_Maior,0)
Cachorro_Maior_FHV = cv2.flip(Cachorro_Maior,-1)

Cachorro_Menor_FH = cv2.flip(Cachorro_Menor,1)
Cachorro_Menor_FV = cv2.flip(Cachorro_Menor,0)
Cachorro_Menor_FHV = cv2.flip(Cachorro_Menor,-1)


#Salva as fotos individuais dos cachorros
cv2.imwrite("Cachorro 1.jpg",recorte1)
cv2.imwrite("Cachorro 2.jpg",recorte2)
cv2.imwrite("Cachorro 3.jpg",recorte3)
cv2.imwrite("Cachorro 4.jpg",recorte4)
cv2.imwrite("Cachorro 5.jpg",recorte5)
cv2.imwrite("Cachorro 6.jpg",recorte6)
#Salva a foto dos cachorros com máscara
cv2.imwrite("Cachorros Com mascára.jpg", im_mask)
#Salva as fotos rotacionadas
cv2.imwrite("Foto Rotacionada Centro = Meio.jpg",img_rotac_centro)
cv2.imwrite("Foto Rotacionada Centro = Cachorro mais Direita.jpg", img_rotac_Cachorro)
#Salva as imagens redimensionadas
cv2.imwrite("Imagem do cachorro maior com metade do tamanho.jpg", Cachorro_Maior_redm)
cv2.imwrite("Imagem do menor cachorro com o dobro do tamanho.jpg", Cachorro_Menor_redm)
#Salva os imagens flipadas do cachorro menor e maior
cv2.imwrite("Cachorro maior Flip Horizontal.jpg",Cachorro_Maior_FH)
cv2.imwrite("Cachorro maior Flip Vertical.jpg",Cachorro_Maior_FV)
cv2.imwrite("Cachorro maior Flip Vertical e Horizontal.jpg",Cachorro_Maior_FHV)

cv2.imwrite("Cachorro Menor Flip Horizontal.jpg",Cachorro_Menor_FH)
cv2.imwrite("Cachorro Menor Flip Vertical.jpg",Cachorro_Menor_FV)
cv2.imwrite("Cachorro Menor Flip Vertical e Horizontal.jpg",Cachorro_Menor_FHV)