import numpy as np
import pandas as pd

image_matrix = np.array([
    [50, 100, 150, 200],
    [100, 150, 200, 250],
    [150, 200, 250, 255],
    [255, 150, 200, 255]
])


flat_image = image_matrix.flatten()

histogram, bin_edges = np.histogram(flat_image, bins=range(0, 257))

pdf = histogram / flat_image.size

cdf = np.cumsum(pdf)

cdf_normalized = (cdf - cdf.min()) / (1 - cdf.min())

histogram_data = pd.DataFrame({
    'Intensitas': np.arange(0, 256),
    'Frekuensi': histogram,
    'PDF': pdf,
    'CDF': cdf,
    'CDF Normalisasi': cdf_normalized
})

histogram_data_nonzero = histogram_data[histogram_data['Frekuensi'] > 0]
print(histogram_data_nonzero)
