import numpy as np

image = np.array([[175, 175, 228],
                  [201, 183, 244],
                  [175, 232, 188]])

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])  

alpha = 1.5

def convolution(image, kernel):
    image_rows, image_cols = image.shape
    kernel_rows, kernel_cols = kernel.shape

    output = np.zeros_like(image)

    for i in range(image_rows - kernel_rows + 1):
        for j in range(image_cols - kernel_cols + 1):
            output[i, j] = np.sum(image[i:i+kernel_rows, j:j+kernel_cols] * kernel)

    return output

result = convolution(image, kernel)

high_boost = alpha * result + image

print("Citra hasil high-boost filtering:\n", high_boost)