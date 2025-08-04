# Day24: OpenCV is a powerful library for computer vision tasks.

# *Edge: Division between two surfaces or objects.
# The line/curve showing the change in gradient of a function.

# *Contour: Unification of points with the same value.
# A line or curve on a graph representing points of equal value.

import cv2 as cv

# Load the image
img = cv.imread(f"img/lm.jpeg")
img_resized = cv.resize(img, (640, 480))

# Convert imgage to grayscale
gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise and improve edge detection
blurred_img = cv.GaussianBlur(gray, (1, 1), 0)

# Canny Edge Detection: It is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.
# It works by detecting areas of the image where there is a rapid change in intensity.
# Convert to binary image using Canny edge detection
# Canny is a popular edge detection algorithm that uses gradients to find edges in an image.
# It is often used as a preprocessing step for contour detection.
# Binary image is an image that has only two pixel values, typically 0 (black) and 255 (white).
edges = cv.Canny(blurred_img, 150, 200)
contours_canny, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count1 = len(contours_canny)
print(f"Number of contours detected using Canny: {count1}")

# Thresholding: It is a technique to create a binary image from a grayscale image.
# Grayscale images are images that contain only shades of gray, with no color information.
# It segments the image into foreground and background based on pixel intensity.
# Convert to binary image using thresholding
thres_val, thres_img = cv.threshold(blurred_img, 160, 255, cv.THRESH_BINARY)
contours_thres, _ = cv.findContours(thres_img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count2 = len(contours_thres)
print(f"Number of contours detected using Threshold: {count2}")

# Draw contours on the original image for both methods(Canny and Threshold)
img_thres = gray.copy()
img_canny = gray.copy()

# Draw contours on the images
cv.drawContours(img_canny, contours_canny, -1, (0, 255, 0), 2)
cv.drawContours(img_thres, contours_thres, -1, (0, 0, 255), 2)

# Display the results
cv.imshow("Canny Contours", img_canny)
cv.imshow("Threshold Contours", img_thres)

cv.waitKey(0)
cv.destroyAllWindows()