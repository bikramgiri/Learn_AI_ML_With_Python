# Linear Algebra in Image Processing
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------- Step 1: Load Image and Convert to Grayscale -------------------
image_path = "D:/Digital Pathshala/AI ML With Python/Assignments/Assignment - IV [By Bikram Giri]/img/krishna.jpeg"  # Change to your image path
img_color = cv2.imread(image_path)

if img_color is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# Convert to grayscale
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# ------------------- Step 2: Represent as 2D NumPy Array -------------------
# Grayscale image is naturally a 2D matrix: rows = height, columns = width
img_matrix = np.array(img_gray, dtype=np.float32)

# ------------------- Step 3a: Covariance Matrix of Image Patches -------------------
patch_size = 5
patches = []

# Extract non-overlapping patches (for simplicity)
for i in range(0, img_matrix.shape[0] - patch_size + 1, patch_size):
    for j in range(0, img_matrix.shape[1] - patch_size + 1, patch_size):
        patch = img_matrix[i:i+patch_size, j:j+patch_size].flatten()
        patches.append(patch)

patches_matrix = np.array(patches).T  # Each column = flattened patch

# Covariance matrix: measures how pixel intensities in patches vary together
cov_matrix = np.cov(patches_matrix)

# ------------------- Step 3b: Eigenvalue Decomposition -------------------
# Eigenvalues = variance along principal directions
# Eigenvectors = directions in which the data varies the most
eig_values, eig_vectors = np.linalg.eigh(cov_matrix)
print("Top 5 Eigenvalues:", eig_values[-5:])

# ------------------- Step 3c: Apply Custom Transformation Matrix -------------------
# Linear algebra operation: Brighten/Darken image by multiplying with scalar matrix
brightness_factor = 1.2  # >1 to brighten, <1 to darken
transform_matrix = np.eye(img_matrix.shape[0]) * brightness_factor  # Identity scaled
# Note: We apply the transformation in a simplified way for demonstration
img_transformed = np.clip(img_matrix * brightness_factor, 0, 255)

# ------------------- Step 4: Compare Original and Transformed Images -------------------
cv2.imshow("Original Grayscale", img_gray)
cv2.imshow("Transformed Image", img_transformed.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------- Step 5: Plot Histograms of Pixel Intensities -------------------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(img_gray.flatten(), bins=256, range=(0, 255), color='gray')
plt.title("Histogram - Original Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(img_transformed.flatten(), bins=256, range=(0, 255), color='gray')
plt.title("Histogram - Transformed Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
