# Day25:

# **Local Binary Pattern Face Recognition Algorithm (LBPH)**:
# This algorithm is used for face recognition by analyzing the local texture of an image. 
# It works by comparing each pixel with its neighbors and encoding the result as a binary number, which is then used to create a histogram of patterns.
# LBPH is particularly effective for face recognition tasks due to its robustness against variations in lighting and facial expressions.
# LBPH is a simple yet effective algorithm for face recognition that uses local binary patterns to describe the texture of an image.

# The steps involved in the LBPH algorithm are as follows:
# 1. Convert the image to grayscale.
# 2. Divide the image into small regions.
# 3. For each region, compute the Local Binary Pattern (LBP).
# 4. Create a histogram of the LBP values.
# 5. Normalize the histogram.
# 6. Use the histograms as features for face recognition.
# 7. Train a classifier using these features.
# 8. Test the classifier on new images.
# 9. Evaluate the performance of the classifier using appropriate metrics.
# 10. Fine-tune the parameters of the classifier for better accuracy.

# Local Binary Pattern (LBP) is a texture descriptor that labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.
# It is widely used in image processing and computer vision, particularly for face recognition tasks.


# 1. Divide the image into different sections according to its size.
# 2. For each section, calculate the Local Binary Pattern (LBP).
# 3. Create a histogram of the LBP values.
# 4. Normalize the histogram.
# 5. Use the histograms as features for face recognition.
# 6. Train a classifier using these features.
# 7. Test the classifier on new images.
# 8. Evaluate the performance of the classifier using appropriate metrics.
# 9. Fine-tune the parameters of the classifier for better accuracy.
# 10. Save the trained model for future use.


# Pixel grid jastai 3*3 ma:
# bicha ko value bhanda dheri aayo bhane 1, bicha ko value bhandaa kam or equal aayo bhane 0.

# Accept image = If histogram is similar
# Reject image = If histogram is not similar

# Formula lagera ako height < threshold aayo bhnae accept garna but if height > threshold aayo bhnae reject garna parcha

# Low intensity bta high intensity ma janu bhaneko edges ho