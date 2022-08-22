from PIL import Image
import sys
import os

# gathering the folder paths

image_folder = sys.argv[1]
output_folder = sys.argv[2]
print(image_folder, output_folder)

# Check and create the output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through and convert the image files:
for filename in os.listdir(image_folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{image_folder}{filename}')
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('Accomplished!')


