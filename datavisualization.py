from data_extraction import extract_data
from PIL import Image
import requests
from io import BytesIO
import os
import zipfile

def open_selected_images(path, image_names):
    image_paths = [os.path.join(path, name) for name in image_names]
    return image_paths

def visualise_image(selected_images):
    url = extract_data()
    url_response = requests.get(url)
    with zipfile.ZipFile(BytesIO(url_response.content)) as z:
        z.extractall('.')
    images = open_selected_images(os.path.join(os.getcwd(), "solar_soli_detection/test/images"), selected_images)
    for i, image_path in enumerate(images):
        image = Image.open(image_path)
        image = image.convert('RGB')
        image.save(f'solar_panel{i}.jpg')
    return url

# Example usage
selected_images = ['Imgdirty_131_1_jpg.rf.dc27e20f067e8c95c81fa7b1a9fad7ec.jpg', 'Imgdirty_151_1_jpg.rf.9c8391892e5473fd8b828c5e20e0f4f0.jpg', 'Imgclean_114_0_jpg.rf.1ad865a31d4dc5e3bde44d9891676df9.jpg', 'Imgclean_38_0_jpg.rf.1ac4c1cd38afbd15c2810ec18dfee9e3.jpg']  # Replace with your actual image names
visualise_image(selected_images)
