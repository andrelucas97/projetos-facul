import cv2

# Carregar os classificadores de cascata
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

# Ler a imagem
img = cv2.imread('./elenco-palmeiras/elenco-palmeiras3.jpg')

# Converter a imagem para tons de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Realizar detecção de rostos
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Realizar detecção de olhos dentro das regiões de rosto detectadas
for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

# Exibir a imagem com as detecções
cv2.imshow('Detecção de Rostos e Olhos', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
