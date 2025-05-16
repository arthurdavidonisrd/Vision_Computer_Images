import cv2

image = cv2.imread("assets/faces.png")

image = cv2.resize(image,(800, 600))

imagem_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(imagem_cinza.shape)

cv2.imshow("My image", imagem_cinza)

cv2.waitKey(0)
cv2.destroyAllWindows()