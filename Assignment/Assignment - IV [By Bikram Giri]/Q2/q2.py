# NumPy Array Manipulation
import numpy as np

def matrix_operations():
    try:
        # 1. Generate 6×6 matrix with random integers (10–100)
        matrix = np.random.randint(10, 101, size=(6, 6))
        print("Original 6x6 Matrix:\n", matrix, "\n")

        # 2. Extract diagonal elements
        diagonal = np.diag(matrix)
        print("Diagonal Elements:", diagonal, "\n")

        # 3. Replace even numbers with their square roots
        modified_matrix = matrix.astype(float)  # Ensure we can store decimals
        even_mask = modified_matrix % 2 == 0
        modified_matrix[even_mask] = np.sqrt(modified_matrix[even_mask])
        print("Modified Matrix (even numbers replaced with sqrt):\n", modified_matrix, "\n")

        # 4. Mean, Median, Standard Deviation
        mean_val = np.mean(modified_matrix)
        median_val = np.median(modified_matrix)
        std_dev = np.std(modified_matrix)
        print(f"Mean: {mean_val:.2f}")
        print(f"Median: {median_val:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}\n")

        # 5. Reshape into 4×9 matrix
        reshaped_matrix = modified_matrix.reshape(4, 9)
        print("Reshaped 4x9 Matrix:\n", reshaped_matrix)

    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An error occurred:", e)

# Run the program
matrix_operations()


