# Day17 : Image Processing with OpenCV

import cv2 as cv

# Reading an image
img = cv.imread(r"img\Ram.jpeg")
cv.imshow("Image", img)

# Image resizing
resized = cv.resize(img, (400, 400))
cv.imshow("Resized Image", resized)

# Image Flipping: 1 for horizontal flip, 0 for vertical flip and -1 for both
flipped = cv.flip(resized, -1)  
cv.imshow("Flipped Image", flipped)

# Grayscale conversion
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

# Drawing a rectangle on the image
cv.rectangle(resized, (100, 100), (300, 300), (150, 0, 0), 2)
cv.imshow("Image with Rectangle", resized)

# Edge detection using Canny
# canny -> ml model -> pre-trained model
edges = cv.Canny(resized, threshold1=100, threshold2=200)
cv.imshow("Canny Edges", edges)

cv.waitKey(0) 


