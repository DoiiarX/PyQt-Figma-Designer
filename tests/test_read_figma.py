import pickle

import requests

from config import token, file_key
from figma import endpoints



figma_file = endpoints.Files(token, file_key)
f = figma_file.get_file()

with open('../resources/f.fig', 'wb') as file:
    pickle.dump(f, file)

for image_id, image_url in figma_file.get_images().items():
    # download the url to resources/id.png
    response = requests.get(image_url)
    with open(f'../resources/images/{image_id}.png', 'wb') as file:
        file.write(response.content)
