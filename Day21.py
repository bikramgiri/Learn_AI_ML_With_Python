#Day21:

import cv2 as cv 
import numpy as np

img = cv.imread(r"img\Ram.jpeg")
# cv.imshow("Original Image", img)

#Resize the image to a specific size
resized_img = cv.resize(img, (400, 400), interpolation=cv.INTER_CUBIC) # Interpolation is use when image size is resized,  AREA=Good interms of linear, LINEAR=generaly used, AREA and LINEAR are use when image size is less than original image size,  CUBIC=Quality Preserved, it is used when image size i.e resolution is high than original image size.
cv.imshow("Resized Image", resized_img)

# Flipping the image horizontally
flipped_img = cv.flip(resized_img, 1)  # 1 for horizontal
cv.imshow("Flipped Image", flipped_img)

# Flipping the image vertically
flipped_img_vertical = cv.flip(resized_img, 0)  # 0 for vertical
cv.imshow("Flipped Image Vertical", flipped_img_vertical)   

# Flipping the image both horizontally and vertically
flipped_img_both = cv.flip(resized_img, -1)  # -1 for both
cv.imshow("Flipped Image Both", flipped_img_both)

#Cropping the image
cropped_img = resized_img[50:800, 50:800]  
cv.imshow("Cropped Image", cropped_img)

# Translating the image
def translate(resized_img, x, y):
      translate_matrix = np.float32([[1, 0, x], [0, 1, y]]) # (1, 0, x) and (0, 1, y) are translation vectors for x and y axes respectively.
      dimension = (resized_img.shape[1], resized_img.shape[0]) # width, height
      return cv.warpAffine(resized_img, translate_matrix, dimension)
translated_img = translate(resized_img, 50, 40)  # Translate by 50 pixels in x and 40 pixels in y directions
cv.imshow("Translated Image", translated_img)

# Rotating the image
def rotate(resized_img, angle, rotatePoint=None):
    (height, width) = resized_img.shape[:2] # resized_img.shape[:2] returns the height and width of the image.
    if rotatePoint is None:
        rotatePoint = (width // 2, height // 2)
    rotation_matrix = cv.getRotationMatrix2D(rotatePoint, angle, 1)  # 1 is the scale factor, which means no scaling.
    dimension = (width, height)  # width, height
    return cv.warpAffine(resized_img, rotation_matrix, dimension)
rotated_img = rotate(resized_img, 90)  # Rotate by 90 degrees
cv.imshow("Rotated Image", rotated_img)

cv.waitKey(0)