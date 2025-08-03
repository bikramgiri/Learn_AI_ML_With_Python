# Bitwise Operations in OpenCV

import cv2 as cv
import numpy as np

# Create two blank images
img1 = np.zeros((300, 300, 3), dtype="uint8") # -> blank image -> dark
img2 = np.zeros((300, 300, 3), dtype="uint8") # -> blank image -> dark

# Draw a white rectangle on img1

cv.rectangle(img1, (50, 50), (250, 250), 255, -1)  # (img1, (50= image top,50= image left), (250= image bottom, 250= image right), 255= color, -1= fills the rectangle
cv.imshow("Image 1 - Rectangle", img1)

# Draw a white circle on img2
cv.circle(img2, (150, 150), 120, 255, -1)  # (img2, (150= image center x, 150= image center y), (120= radius), 255= color, -1= fills the circle
cv.imshow("Image 2 - Circle", img2)

#AND operation
and_result = cv.bitwise_and(img1, img2)
cv.imshow("AND Result", and_result)

#OR operation
or_result = cv.bitwise_or(img1, img2)
cv.imshow("OR Result", or_result)

#XOR operation
xor_result = cv.bitwise_xor(img1, img2)
cv.imshow("XOR Result", xor_result)

#NOT operation
not_img1 = cv.bitwise_not(img1)
cv.imshow("NOT Result", not_img1)

#Masking
img = cv.imread(r"img\Ram.jpeg")
resized_img = cv.resize(img, (900, 900))
cv.imshow("Resized Image", resized_img)

# Create a mask
image_mask = np.zeros(resized_img.shape[:2], dtype="uint8")  # Create a blank mask
cv.imshow("Mask", image_mask)

# Draw a white circle on the mask
cv.circle(image_mask, (450, 500), 300, 255, -1) # (mask, (450= center x, 500= center y), (300= radius), 255= color, -1= fills the circle)

# Apply the mask to the image
masked_img = cv.bitwise_and(resized_img, resized_img, mask=image_mask)
cv.imshow("Masked Image", masked_img)

#Splitting the channels
B, G, R = cv.split(masked_img)
cv.imshow("Blue Channel", B)
cv.imshow("Green Channel", G)
cv.imshow("Red Channel", R)

# Merging the channels back
merged_img = cv.merge([B, G, R])
cv.imshow("Merged Image", merged_img)

# Create a zero array for Visualizing individual channels
zeros = np.zeros_like(B) 
Blue_visual = cv.merge([B, zeros, zeros])  # Visualize Blue channel
cv.imshow("Blue Visual", Blue_visual)
Green_visual = cv.merge([zeros, G, zeros])  # Visualize Green channel
cv.imshow("Green Visual", Green_visual)
Red_visual = cv.merge([zeros, zeros, R])  # Visualize Red channel
cv.imshow("Red Visual", Red_visual)

cv.waitKey(0)
