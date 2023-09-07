import pickle
import subprocess

import pyqt_generator
from config import figma_file_path, gui_path, gui_handler_path, project_directory, overwrite_handler

with open(figma_file_path, 'rb') as file:
    figma_file = pickle.load(file)
python_code = '\n'.join(pyqt_generator.generate_pyqt_design(figma_file))
with open(gui_path, 'w', encoding="utf-8") as file:
    file.write(python_code)
if overwrite_handler:
    handler_code = '\n'.join(pyqt_generator.generate_handler(figma_file))
    with open(gui_handler_path, 'w', encoding="utf-8") as file:
        file.write(handler_code)

subprocess.Popen(f'python gui.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                 cwd=project_directory)
