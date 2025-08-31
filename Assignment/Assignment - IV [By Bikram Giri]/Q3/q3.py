# Image Loading and Basic Processing

import cv2 as cv

# 1. Load a color image from local system
image_path = "D:/Digital Pathshala/AI ML With Python/Assignments/Assignment - IV [By Bikram Giri]/img/Ram.jpeg"
original_img = cv.imread(image_path)

# 2. Convert to grayscale
gray_img = cv.cvtColor(original_img, cv.COLOR_BGR2GRAY)

# 3. Display both original and grayscale images side by side
cv.imshow("Original Image", original_img)
cv.imshow("Grayscale Image", gray_img)

# 4. Saves the grayscale image with a new filename
cv.imwrite(image_path, gray_img)

# 5. Print dimensions
print("Original Image Dimensions (Height, Width, Channels):", original_img.shape)
print("Grayscale Image Dimensions (Height, Width):", gray_img.shape)

# Wait for key press and close windows
cv.waitKey(0)
cv.destroyAllWindows()
