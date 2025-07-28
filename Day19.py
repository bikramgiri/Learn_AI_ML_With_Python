import numpy as np 
import cv2 as cv 
img = cv.imread(r"img\Building.jpg")

# Resize the image
resized = cv.resize(img, (400, 400))
cv.imshow("Resized Image", resized)

# Grayscale conversion
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

#*Laplacian Method -> method to detect edges
lap = cv.Laplacian(gray, cv.CV_64F) # second derivative -> +ve and -ve
lap = np.uint8(np.absolute(lap)) # convert to uint8
cv.imshow("Laplacian Image", lap)

#*Sobel Method
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow("Sobel-X", sobelx)
cv.imshow("Sobel-Y", sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
combained_sobel = np.uint8(np.absolute(combined_sobel))  # Convert to uint8
cv.imshow("Combined Sobel Image", combined_sobel)

# Canny edge detection
edges = cv.Canny(gray, threshold1=50, threshold2=200)
cv.imshow("Canny Edges", edges)

cv.waitKey(0)
 
 
 