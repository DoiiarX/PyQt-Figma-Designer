import os
import re

token: str
overwrite_handler: bool
project_directory: str
scale: float

image_directory: str
svg_directory: str
figma_file_path: str
gui_path: str
gui_handler_path: str
gui_controller_path: str
strings_path: str
components_config_path: str

file_key: str

text_scale = 0.7
figma_file_name = 'figma_file.json'
gui_handler_file_name = 'gui_handler.py'
gui_controller_file_name = 'gui_controller.py'
strings_file_name = 'strings.py'
components_config_file_name = 'components_config.json'

generic_components_directory = 'generator/design/components'


def set_url(url: str):
    global file_key
    match = re.search(r'https://www.figma.com/file/([0-9A-Za-z]+)', url.strip())
    file_key = match.group(1).strip()


def set_project_directory(directory: str):
    global project_directory, \
        image_directory, \
        svg_directory, \
        gui_path, \
        gui_handler_path, \
        figma_file_path, \
        gui_controller_path, \
        strings_path, \
        components_config_path
    project_directory = directory.strip()
    image_directory = f'{project_directory}/images'
    svg_directory = f'{project_directory}/svg'
    figma_file_path = f'{project_directory}/{figma_file_name}'
    gui_path = f'{project_directory}/gui.py'
    gui_handler_path = f'{project_directory}/{gui_handler_file_name}'
    gui_controller_path = f'{project_directory}/{gui_controller_file_name}'
    strings_path = f'{project_directory}/{strings_file_name}'
    components_config_path = f'{project_directory}/{components_config_file_name}'


def check_project_directory():
    if not os.path.exists(project_directory):
        raise Exception(f'Project directory doesn\'t exists : "{project_directory}"')
    if not os.path.exists(image_directory):
        raise Exception(f'Image directory doesn\'t exists : "{image_directory}"')
    if not os.path.exists(svg_directory):
        raise Exception(f'Project directory doesn\'t exists : "{svg_directory}"')
