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
    images = open_selected_images(os.path.join(os.getcwd(), "solar_object_detection.zip/test/images"), selected_images)
    for i, image_path in enumerate(images):
        image = Image.open(image_path)
        image = image.convert('RGB')
        image.save(f'solar_panel{i}.jpg')
    return url

# Example usage
selected_images = ['9_JPG.rf.6b8a4049fd4b98a4bb2b58bb17dbba6f.jpg', '122v5_jpg.rf.1645735acb7c35f33a3acd2f27b0522c.jpg', '132v7_jpg.rf.8bdab9ef588c6164589e39c8aad4a0b6.jpg', '127_jpg.rf.3d447e2913076b4664c55d624ec85fc2.jpg']  # Replace with your actual image names
visualise_image(selected_images)
