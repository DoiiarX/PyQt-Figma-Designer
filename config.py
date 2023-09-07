import os
import re

token = 'figd_-QMtU_8nZoTs48qAzWTqQecktPRyh3gCI9rR0Jx5'
# file_url = 'https://www.figma.com/file/DEtNOgq9OGnkGPfPpiQeEK/Untitled?type=design&mode=design&t=MXkH4iNj09GBg1aG-0'
file_url = 'https://www.figma.com/file/PExygXiMSTBEpXXEq0ZPyE/Untitled?type=design&node-id=0-1&mode=design&t=D4pN9YixWIbPDYlb-0'
project_directory = '../outputs/gui1'
overwrite_handler = True

image_directory = f'{project_directory}/images'
svg_directory = f'{project_directory}/svg'
figma_file_path = f'{project_directory}/figma_file.pickle'
gui_path = f'{project_directory}/gui.py'
gui_handler_file_name = 'gui_handler.py'
gui_handler_path = f'{project_directory}/{gui_handler_file_name}'
scale = .7
text_scale = 0.7

match = re.search(r'https://www.figma.com/file/([0-9A-Za-z]+)', file_url.strip())
if not os.path.exists(project_directory):
    os.makedirs(project_directory)
if not os.path.exists(image_directory):
    os.makedirs(image_directory)
if not os.path.exists(svg_directory):
    os.makedirs(svg_directory)

file_key = match.group(1).strip()
