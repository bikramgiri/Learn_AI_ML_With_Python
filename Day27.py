# *Day27: Skin detection using OpenCV

# HSV: Hue, Saturation, Value (good for color filtering)
# Hue: Color type, Gives the true color of image(0 to 179)
# Saturation: Intensity of color, Gives saturation of images (0 to 255)
# Value: Brightness of color, Gives brightness of images (0 to 255)

# RGB and BGR value cannot accurately describe skin color

# HSV value for lower skin color = (0, 20, 70)
# HSV value for upper skin color = (20, 255, 255)

# *Algorithm Steps:
# 1. Load the image
# 2. Convert the image to HSV color space
# 3. Define The HSV range for different skin colors
# 4. Create a mask for skin areas
# 5. Apply the mask to the original image
# 6. Display the results

# *Site to learn:
# 1. HackerRank: https://www.hackerrank.com/, For: Coding Challenges
# 2. Overleaf: https://www.overleaf.com/, For: LaTeX Editing to make beautiful documents
# 3. Kaggle: https://www.kaggle.com/, For: Data Science Competitions
# 4. LeetCode: https://leetcode.com/, For: Coding Challenges
# 5. Hugging Face: https://huggingface.co/, For: NLP and Transformers
# 6. Perplexity: https://www.perplexity.ai/, For: AI Research and Tools
# 7. CS50: https://cs50.harvard.edu/, For: Computer Science Education
# 8. edX: https://www.edx.org/, For: Online Courses

# 9. CodeSignal: https://codesignal.com/, For: Coding Challenges
# 10. GeeksforGeeks: https://www.geeksforgeeks.org/, For: Coding Tutorials

# -------------------- Code ---------------------

import cv2 
import numpy as np  # For handling arrays

# *Step 1: Read the image
image_path = "training_images/Ed_Sheeran/Ed8.jpg"

# Resize the image
image = cv2.imread(image_path)
image = cv2.resize(image, (600, 500))

# Check if the image loaded properly
if image is None:
    print("Error: Image not found! Please check the path.")
    exit()

# *Step 2: Convert to HSV color space 
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# *Step 3: Define skin color range
# These values work for most skin tones, but can be adjusted if needed.
lower_skin = np.array([0, 20, 70], dtype=np.uint8)   # Lower HSV(H=Hue, S= Saturation, V=Value) boundary
upper_skin = np.array([20, 255, 255], dtype=np.uint8)  # Upper HSV(H=Hue, S= Saturation, V=Value) boundary

# *Step 4: Create a mask for skin areas 
mask = cv2.inRange(hsv_image, lower_skin, upper_skin)
# 'mask' will be white where skin is detected, black elsewhere.

# *Step 5: Apply mask to the original image
skin_detected = cv2.bitwise_and(image, image, mask=mask)

# *Step 6: Display the results
# Show the original image
cv2.imshow("Original Image", image)
# Show where skin is detected (white = skin)       
cv2.imshow("Skin Mask", mask) 
# Show the detected skin areas
cv2.imshow("Skin Detected", skin_detected)

# Wait for a key press to close windows
cv2.waitKey(0)
# Destroy all OpenCV windows
cv2.destroyAllWindows()




