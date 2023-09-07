import pickle

import requests

from config import token, file_key, image_directory, figma_file_path
from figma import endpoints

figma_file = endpoints.Files(token, file_key)
f = figma_file.get_file()

with open(figma_file_path, 'wb') as file:
    pickle.dump(f, file)

for image_id, image_url in figma_file.get_images().items():
    # download the url to outputs/id.png
    response = requests.get(image_url)
    with open(f'{image_directory}/{image_id}.png', 'wb') as file:
        file.write(response.content)
