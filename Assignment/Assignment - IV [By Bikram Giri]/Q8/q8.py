# Integrated Project- Image Analysis Pipeline
import cv2
import numpy as np
import os
from glob import glob
from tqdm import tqdm
import matplotlib.pyplot as plt

class ImageAnalysisPipeline:
    def __init__(self, input_dir, output_dir, image_size=(512, 512)):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.image_size = image_size
        self.cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(self.cascade_path)
        if self.face_cascade.empty():
            raise IOError("Error: Haar Cascade file not found!")
        os.makedirs(output_dir, exist_ok=True)
        self.summary_matrix = []

    # ------------------- Input Stage -------------------
    def load_images(self):
        if not os.path.exists(self.input_dir):
            raise FileNotFoundError(f"Input folder does not exist: {self.input_dir}")

        # Get all files
        images = os.listdir(self.input_dir)
        # Filter only image extensions
        images = [os.path.join(self.input_dir, f) for f in images
              if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"))]

        if not images:
            raise FileNotFoundError(f"No images found in {self.input_dir}. Check folder contents and extensions.")

        print(f"✅ Found {len(images)} image(s) in folder:")
        for img in images:
            print(f"   {img}")
        return images

    # ------------------- Preprocessing Stage -------------------
    def preprocess_image(self, img):
        print("🔹 Preprocessing image...")
        img_resized = cv2.resize(img, self.image_size)
        img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
        return img_resized, img_gray, img_blur

    # ------------------- Feature Extraction -------------------
    def extract_features(self, img_gray, img_blur):
        edges = cv2.Canny(img_blur, 100, 200)
        edge_density = np.sum(edges > 0) / edges.size
        faces = self.face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5)
        num_faces = len(faces)
        mean_intensity = np.mean(img_gray)
        contrast = np.std(img_gray)
        print(f"   Features extracted -> Edge Density: {edge_density:.4f}, Faces: {num_faces}, Mean Intensity: {mean_intensity:.2f}, Contrast: {contrast:.2f}")
        return [edge_density, num_faces, mean_intensity, contrast], edges, faces

    # ------------------- Analysis Stage -------------------
    def analyze_features(self):
        feature_matrix = np.array(self.summary_matrix)
        cov_matrix = np.cov(feature_matrix.T)
        eig_values, eig_vectors = np.linalg.eigh(cov_matrix)
        return feature_matrix, cov_matrix, eig_values, eig_vectors

    def find_highest_edge_density(self):
        edge_densities = [f[0] for f in self.summary_matrix]
        idx = np.argmax(edge_densities)
        return idx, edge_densities[idx]

    # ------------------- Output Stage -------------------
    def save_results(self, original, processed, edges, faces, filename):
        base_name = os.path.splitext(os.path.basename(filename))[0]
        cv2.imwrite(os.path.join(self.output_dir, f"{base_name}_gray.jpg"), processed)
        cv2.imwrite(os.path.join(self.output_dir, f"{base_name}_edges.jpg"), edges)
        img_faces = original.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(img_faces, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite(os.path.join(self.output_dir, f"{base_name}_faces.jpg"), img_faces)
        print(f"   ✅ Saved processed images for {base_name}")
        return img_faces

    def generate_report(self, image_files):
        print("\n--- Image Analysis Report ---")
        for i, img_file in enumerate(image_files):
            features = self.summary_matrix[i]
            print(f"{os.path.basename(img_file)} | Edge Density: {features[0]:.4f} | Faces: {features[1]} | Mean Intensity: {features[2]:.2f} | Contrast: {features[3]:.2f}")

    def create_collage(self, images_list, collage_name="collage.jpg"):
        rows = []
        for i in range(0, len(images_list), 2):
            row_imgs = images_list[i:i + 2]
            if len(row_imgs) < 2:
                blank = np.zeros_like(row_imgs[0])
                row_imgs.append(blank)
            row = np.hstack(row_imgs)
            rows.append(row)
        collage = np.vstack(rows)
        cv2.imwrite(os.path.join(self.output_dir, collage_name), collage)
        print(f"\n✅ Collage saved as {collage_name}")

    # ------------------- Run Pipeline -------------------
    def run(self):
        image_files = self.load_images()
        processed_images_for_collage = []

        for img_file in tqdm(image_files, desc="Processing Images"):
            print(f"\nProcessing: {img_file}")
            img = cv2.imread(img_file)
            if img is None:
                print(f"⚠ Could not read {img_file}, skipping.")
                continue

            original, gray, blur = self.preprocess_image(img)
            features, edges, faces = self.extract_features(gray, blur)
            self.summary_matrix.append(features)

            img_faces = self.save_results(original, gray, edges, faces, img_file)
            processed_images_for_collage.append(original)
            processed_images_for_collage.append(img_faces)

        self.generate_report(image_files)
        feature_matrix, cov_matrix, eig_values, eig_vectors = self.analyze_features()
        idx, max_edge_density = self.find_highest_edge_density()
        print(f"\nImage with highest edge density: {os.path.basename(image_files[idx])} ({max_edge_density:.4f})")
        print(f"\nCovariance Matrix of Features:\n{cov_matrix}")
        print(f"\nEigenvalues:\n{eig_values}")

        self.create_collage(processed_images_for_collage)
        print(f"\n✅ Pipeline completed. Collage saved in {self.output_dir}")


# ------------------- Example Usage -------------------
if __name__ == "__main__":
    input_dir = r"D:\Digital Pathshala\AI ML With Python\Assignments\Assignment - IV [By Bikram Giri]\images"
    output_dir = r"D:\Digital Pathshala\AI ML With Python\Assignments\Assignment - IV [By Bikram Giri]\images\output"

    pipeline = ImageAnalysisPipeline(input_dir, output_dir)
    pipeline.run()



# import os
# input_dir = r"D:\Digital Pathshala\AI ML With Python\Assignments\Assignment - IV [By Bikram Giri]\images"
# files = os.listdir(input_dir)
# print("Files in folder:", files)
