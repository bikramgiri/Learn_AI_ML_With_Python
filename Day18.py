# Day18 : Bluring

import cv2 as cv 
# Load the image
img = cv.imread(r"img\lm.jpeg")

# Resize the image
resized = cv.resize(img, (600, 600))
cv.imshow("Resized Image", resized)

# *Average Blurring(AB): It calculates the average of the pixel values in a specified kernel size (5x5 in this case). Time complexity is O(n^2) where n is the kernel size.
# *It is best for removing noise from the image, especially when the noise is uniformly distributed.
# This technique smooths the image by averaging the pixel values in a neighborhood around each pixel.
# The first parameter is the kernel size, and it can be both odd and even numbers.
average_blur = cv.blur(resized, (10, 10)) # (3,3), (8,8), (9,9) etc. both odd and even can be used. (resized, (kernelWidth, kernelHeight))
cv.imshow("Average Blurred Image", average_blur)

# *Median Blurring(MB): It replaces each pixel value with the median value of the pixel values in a specified kernel size (5x5 in this case). Time complexity is O(n log n) where n is the kernel size.
# *It is best for removing noise from the image, especially salt-and-pepper noise.
# This technique is effective for removing salt-and-pepper noise from the image.
# The first parameter is the kernel size, and it must be an odd number.
median_blur = cv.medianBlur(resized, 9) # 3, 4, 5, 7, etc. only odd values can be used. (resized, kernelSize)
cv.imshow("Median Blurred Image", median_blur)

# *Gaussian Blurring(GB): It applies a Gaussian filter to the image, which is a weighted average of the pixel values in a specified kernel size (5x5 in this case). Time complexity is O(n^2) where n is the kernel size.
# *It is best for reducing noise while preserving edges.
# The Gaussian filter is useful for reducing noise and smoothing the image.
# The first parameter is the kernel size, and the second parameter is the standard deviation in the X and Y directions.
# It is useful for reducing noise while preserving edges.
gaussian_blur = cv.GaussianBlur(resized, (9, 9), 11) # (3,3), (7,7), (9,9) and 0 to 10.....etc. only odd values can also be used. ((kernelWidth, kernelHeight), sigmaX, sigmaY)
cv.imshow("Gaussian Blurred Image", gaussian_blur)

# *Bilateral Blurring(BB): It applies a bilateral filter to the image, which preserves edges while reducing noise. It calculates weighted averages of the pixel values in a specified kernel size (9, 75, 75 in this case). Time complexity is O(n^2) where n is the kernel size.
# *It is best for reducing noise while preserving edges.
# The first parameter is the diameter of the pixel neighborhood, and the second and third parameters are the sigma values for color and space, respectively.
# sigma color: It determines how much the colors within the pixel neighborhood will be mixed.
# sigma space: It determines how much the spatial distance between pixels will be considered.
# It is useful for reducing noise while keeping edges sharp.
bilateral_blur = cv.bilateralFilter(resized, 9, 20, 20) # 9, 11, 13, etc. only odd values can be used, (blurWindowValue, sigmaColor, sigmaSpace)
cv.imshow("Bilateral Blurred Image", bilateral_blur)

cv.waitKey(0)



# Among above blurring techniques, the Bilateral Blurring is the best for reducing noise while preserving edges.
# Among the blurring techniques, which one is slowest and why?
# The Median Blurring is the slowest among the blurring techniques. It is slow because it requires sorting the pixel values in the kernel to find the median, which has a time complexity of O(n log n).
# Among the blurring techniques, which one is fastest and why?
# The Average Blurring is the fastest among the blurring techniques. It is fast because it simply calculates the average of the pixel values in the kernel without any sorting, which has a time complexity of O(n^2).

# Among the blurring techniques:
#In terms of speed: AB>MB>GB>BB
#In terms of edge preservation: BB>GB>MB>AB
#In terms of noise reduction: BB>GB>MB>AB
# In terms of overall performance: BB>GB>MB>AB
# In terms of complexity: AB>GB>BB>MB
# In terms of kernel size: AB can use both odd and even, MB only odd,

