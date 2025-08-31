# Edge Detection and Blurring Techniques
import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Image Filtering: Blurring & Edge Detection")

default_path = "D:/Digital Pathshala/AI ML With Python/Assignments/Assignment - IV [By Bikram Giri]/img/Ram.jpeg"

parser.add_argument("image", nargs="?", default=default_path, help="Path to input image")
parser.add_argument("--gk", type=int, default=15, help="Gaussian blur kernel size (odd number)")
parser.add_argument("--ak", type=int, default=10, help="Average blur kernel size")
parser.add_argument("--mk", type=int, default=9, help="Median blur kernel size (odd number)")
args = parser.parse_args()

img = cv2.imread(args.image)
if img is None:
    raise FileNotFoundError(f"Image not found at {args.image}")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gaussian_blur = cv2.GaussianBlur(img_rgb, (args.gk, args.gk), 0)
average_blur = cv2.blur(img_rgb, (args.ak, args.ak))
median_blur = cv2.medianBlur(img_rgb, args.mk)

gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
canny_edges = cv2.Canny(gray, 100, 200)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

images = [
    (img_rgb, "Original"),
    (gaussian_blur, f"Gaussian Blur ({args.gk}x{args.gk})"),
    (average_blur, f"Average Blur ({args.ak}x{args.ak})"),
    (median_blur, f"Median Blur ({args.mk})"),
    (canny_edges, "Canny Edges"),
    (sobel_x, "Sobel X"),
    (sobel_y, "Sobel Y"),
    (sobel_combined, "Sobel Magnitude")
]

plt.figure(figsize=(12, 8))
for i, (image, title) in enumerate(images):
    plt.subplot(2, 4, i + 1)
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(image)
    plt.title(title)
    plt.axis('off')

plt.tight_layout()
plt.show()
