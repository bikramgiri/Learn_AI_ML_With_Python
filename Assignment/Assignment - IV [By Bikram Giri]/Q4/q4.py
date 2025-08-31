# Image Resizing and Geometric Transformations
import cv2

image_path = "D:/Digital Pathshala/AI ML With Python/Assignments/Assignment - IV [By Bikram Giri]/img/Ram.jpeg"

def resize_image_operations(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Original dimensions
    original_height, original_width = img.shape[:2]
    print(f"Original Dimensions: {original_width}x{original_height}")

    # 1. 50% smaller (maintain aspect ratio)
    scale_percent = 50  # percent of original size
    width_smaller = int(original_width * scale_percent / 100)
    height_smaller = int(original_height * scale_percent / 100)
    resized_smaller = cv2.resize(img, (width_smaller, height_smaller), interpolation=cv2.INTER_AREA)

    print("\n--- 50% Smaller ---")
    print(f"New Dimensions: {width_smaller}x{height_smaller}")
    print(f"Scaling Factors: {width_smaller/original_width:.2f}, {height_smaller/original_height:.2f}")
    cv2.imwrite("resized_50_percent.jpg", resized_smaller)

    # 2. 200% larger (maintain aspect ratio)
    scale_percent = 200
    width_larger = int(original_width * scale_percent / 100)
    height_larger = int(original_height * scale_percent / 100)
    resized_larger = cv2.resize(img, (width_larger, height_larger), interpolation=cv2.INTER_CUBIC)

    print("\n--- 200% Larger ---")
    print(f"New Dimensions: {width_larger}x{height_larger}")
    print(f"Scaling Factors: {width_larger/original_width:.2f}, {height_larger/original_height:.2f}")
    cv2.imwrite("resized_200_percent.jpg", resized_larger)

    # 3. Fixed size 300x300 (no aspect ratio)
    fixed_size = (300, 300)
    resized_fixed = cv2.resize(img, fixed_size, interpolation=cv2.INTER_LINEAR)

    print("\n--- Fixed Size 300x300 ---")
    print(f"New Dimensions: {fixed_size[0]}x{fixed_size[1]}")
    print(f"Scaling Factors: {fixed_size[0]/original_width:.2f}, {fixed_size[1]/original_height:.2f}")
    cv2.imwrite("resized_fixed_300x300.jpg", resized_fixed)

    # Display images
    cv2.imshow("Original", img)
    cv2.imshow("50% Smaller (Aspect Ratio Maintained)", resized_smaller)
    cv2.imshow("200% Larger (Aspect Ratio Maintained)", resized_larger)
    cv2.imshow("Fixed Size 300x300 (No Aspect Ratio)", resized_fixed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the function with your image path
resize_image_operations(image_path)
