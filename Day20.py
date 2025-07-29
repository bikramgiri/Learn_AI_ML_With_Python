import cv2 as cv

# **This script captures video from the webcam and displays it in a window.
cap = cv.VideoCapture(0)

while True:
    set_f, frame = cap.read()
    if not set_f:
        break
    cv.imshow("Face", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


# **This script detects faces in a video stream from the webcam using OpenCV's Haar Cascade classifier. 
face_casade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while True:
      tr, frame = cap.read()
      gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
      # scaleFactor is used to scale the image, minNeighbors is the number of neighbors each candidate rectangle should have to retain it.
      faces = face_casade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) # ((x, y, w, h), (x, y, w, h), ...)
      
      for (x, y, w, h) in faces:
          cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
      cv.imshow("Face Detection", frame)
      
      if cv.waitKey(1) & 0xFF == ord('q'):
          break
    
cap.release()
cv.destroyAllWindows()
