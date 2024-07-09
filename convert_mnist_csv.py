import idx2numpy
import numpy as np
import pandas as pd

# Paths to the MNIST dataset files
file_images = 'train-images.idx3-ubyte'
file_labels = 'train-labels.idx1-ubyte'

# Read the image and label files
images = idx2numpy.convert_from_file(file_images)
labels = idx2numpy.convert_from_file(file_labels)

# Flatten the image array and normalize pixel values
images_flattened = images.reshape(images.shape[0], -1) / 255.0

# Combine labels and images
data = np.column_stack((labels, images_flattened))

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('mnist.csv', index=False, header=False)