import cv2 as cv
img = cv.imread(r"img\lm.jpeg")

# Image resizing
resized = cv.resize(img, (800, 800))

# Grayscale conversion
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

# Haar Cascade for face detection
# scaleFactor: How much the image size is reduced at each image scale. It's a parameter that affects the detection speed and accuracy. It's typically set to a value between 1.1 and 1.4. It determines how much the image is scaled down at each step of the detection process. 
# minNeighbors: How many neighbors each candidate rectangle should have to retain it as a valid detection. This parameter affects the quality of the detection. A higher value means fewer detections but with higher confidence. It's typically set to a value between 3 and 6. It determines how many rectangles around a detected face must also be detected for the face to be considered valid.
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

for (x, y, w, h) in faces:
    cv.rectangle(resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Detected Faces", resized)
cv.waitKey(0)


