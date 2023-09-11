import os
import re

(project_directory,
 image_directory,
 svg_directory,
 figma_file_path,
 gui_path,
 gui_handler_path,
 gui_controller_path) = '', '', '', '', '', '', ''
gui_handler_file_name = 'gui_handler.py'
gui_controller_file_name = 'gui_controller.py'
scale = .7
text_scale = 0.7

file_key = ''


def set_url(url: str):
    global file_key
    match = re.search(r'https://www.figma.com/file/([0-9A-Za-z]+)', url.strip())
    file_key = match.group(1).strip()


def set_project_directory(directory: str):
    global project_directory, image_directory, svg_directory, gui_path, gui_handler_path, figma_file_path, gui_controller_path
    project_directory = directory.strip()
    image_directory = f'{project_directory}/images'
    svg_directory = f'{project_directory}/svg'
    figma_file_path = f'{project_directory}/figma_file.pickle'
    gui_path = f'{project_directory}/gui.py'
    gui_handler_path = f'{project_directory}/{gui_handler_file_name}'
    gui_controller_path = f'{project_directory}/{gui_controller_file_name}'
    if not os.path.exists(project_directory):
        os.makedirs(project_directory)
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)
    if not os.path.exists(svg_directory):
        os.makedirs(svg_directory)


# set_url('https://www.figma.com/file/PExygXiMSTBEpXXEq0ZPyE')
# set_url('https://www.figma.com/file/DEtNOgq9OGnkGPfPpiQeEK/')
set_url('https://www.figma.com/file/hKK2ZvSS9Xya0MBKvF9UER/')
set_project_directory('../outputs/default_project')
token = 'figd_-QMtU_8nZoTs48qAzWTqQecktPRyh3gCI9rR0Jx5'
overwrite_handler_controller = True
