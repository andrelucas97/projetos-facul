import cv2

def redim(img, largura):
    alt = int(img.shape[0] / img.shape[1] * largura)
    img = cv2.resize(img, (largura, alt), interpolation=cv2.INTER_AREA)
    return img

df1 = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
df2 = cv2.CascadeClassifier('./haarcascades/haarcascade_profileface.xml')

camera = cv2.VideoCapture('./video/filme-1min.mp4')
#camera = cv2.VideoCapture(0) # para reconhecer usando webcam

while True:
    sucesso, frame = camera.read()
    
    if not sucesso:
        break
    
    frame = redim(frame, 320)
    
    frame_pb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces1 = df1.detectMultiScale(frame_pb, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)
    faces2 = df2.detectMultiScale(frame_pb, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)
    
    frame_temp = frame.copy()
    
    for (x, y, lar, alt) in faces1:
        cv2.rectangle(frame_temp, (x, y), (x + lar, y + alt), (0, 255, 255), 2)
    
    for (x, y, lar, alt) in faces2:
        cv2.rectangle(frame_temp, (x, y), (x + lar, y + alt), (255, 0, 255), 2)
    
    cv2.imshow("Encontrando faces...", redim(frame_temp, 640))
    
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()
