from rembg import remove
from PIL import Image

input_image='test.jpeg'
output_path='output.png'

print('here we are')

print("opening image...")
image_uploaded=Image.open(input_image)

print("removing background...")
output_image=remove(image_uploaded)

print("saving image in new file path...")
output_image.save(output_path)