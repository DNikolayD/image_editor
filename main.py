from importlib.resources import path

from PIL import Image, ImageEnhance, ImageFilter
from os import listdir, path

path = '/images'
path_out = '/edited_images'

for file_name in listdir(path):
    image_file_path = f'{path}/{file_name}'

    image = Image.open(image_file_path)
    edited_image = image.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    factor = 1.63
    enhancer = ImageEnhance.Contrast(edited_image)

    clean_name = path.split(file_name)[0]

    edited_image_file_path = f'{path_out}/{clean_name}_edited.jpg'

    edited_image.save(edited_image_file_path)