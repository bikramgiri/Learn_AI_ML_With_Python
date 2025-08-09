import cv2 as cv
import numpy as np
import os  # To navigate inside folders/files

# Load Haar Cascade face detector
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load the recognizer
recognizer = cv.face.LBPHFaceRecognizer_create()

# Path of training data folder
dataset_path = "training_images"

# Empty lists to store faces and their corresponding labels
faces = []
labels = []

# Dictionary to map labels to person names (used for display)
label_to_name = {}

# Label counter starting from 0
current_label = 0

# Loop over each folder inside 'training_data'
for person_name in os.listdir(dataset_path):  
    person_folder = os.path.join(dataset_path, person_name)

    # Make sure it's a folder (not a file)
    if not os.path.isdir(person_folder):
        continue

    # Map the current label to the person's name
    label_to_name[current_label] = person_name

    # Loop over images inside that person's folder
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)

        # Read image in grayscale
        image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

        if image is None:
            continue  # Skip if image can't be loaded

        # Detect the face in the image
        faces_rect = face_cascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5)

        for (x, y, w, h) in faces_rect:
            # Crop and resize the faces
            face_roi = image[y:y+h, x:x+w]
            face_resized = cv.resize(face_roi, (200, 200))

            # Store the face and its label
            faces.append(face_resized)
            labels.append(current_label)

    current_label += 1  # Move to next label for next person

# Convert lists to numpy arrays
faces = np.array(faces)
labels = np.array(labels)

# Train the recognizer
recognizer.train(faces, labels)
print("Training complete!")

# Load test image
test_img = cv.imread(r"training_images\Ed_Sheeran\ED8.jpg")
test_gray = cv.cvtColor(test_img, cv.COLOR_BGR2GRAY)

# Detect faces in the test image
test_faces = face_cascade.detectMultiScale(test_gray, scaleFactor=1.1, minNeighbors=5)

# Loop through detected faces
for (x, y, w, h) in test_faces:
    face_roi = test_gray[y:y+h, x:x+w]
    face_resized = cv.resize(face_roi, (200, 200))

    # Predict the label of the face
    label, confidence = recognizer.predict(face_resized)

    # Map label to person's name
    person_name = label_to_name[label]

    # Draw rectangle and name on the image
    text = f"{person_name} ({round(confidence, 2)})"
    cv.rectangle(test_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.putText(test_img, text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Show result
cv.imshow("Recognition Result", test_img)
cv.waitKey(0)
cv.destroyAllWindows()
