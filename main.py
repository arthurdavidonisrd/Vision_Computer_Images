import cv2

image = cv2.imread("assets/faces.png")

image = cv2.resize(image,(800, 600))

imagem_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Adjustments about the image ⤴️


facial_detector = cv2.CascadeClassifier("assets/haarcascade_frontalface_default.xml")
detections = facial_detector.detectMultiScale(imagem_cinza)

for x,y,w,h in detections:
  cv2.rectangle(image, (x,y), (x + w, y + h), (0, 255, 255), 5)
cv2.imshow("Points in faces", image)


cv2.waitKey(0)
cv2.destroyAllWindows()