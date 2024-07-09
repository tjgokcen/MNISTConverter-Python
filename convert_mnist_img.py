from PIL import Image
import idx2numpy

file_images = 'train-images.idx3-ubyte'
images = idx2numpy.convert_from_file(file_images)

# Convert each image to a PNG file
for index, img in enumerate(images):
    image = Image.fromarray(img)
    image.save(f'img\\image_{index}.png')