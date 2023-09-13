import json
import os
import pathlib
import subprocess

from PySide6.QtWidgets import QFileDialog, QMessageBox

from gui_controller import PyqtFigmaDesignerGuiV3Controller

runner_directory = pathlib.Path(__file__).parent.parent.absolute()

scale = 1
scale_min = 0.25
scale_max = 4

overwrite_handlers = False

project_directory = ""
figma_token = ""
figma_file_url = ""

config_file_name = "pyqtfd-config.json"


def slider_to_scale(value: float):
    return value * (scale_max - scale_min) + scale_min


def scale_to_slider(value: float):
    return (value - scale_min) / (scale_max - scale_min)


def load_config():
    global scale, scale_min, scale_max, overwrite_handlers, project_directory, figma_token, figma_file_url
    if os.path.exists(config_file_name):
        with (open(config_file_name, 'r') as file):
            config = json.load(file)
            scale = config['scale']
            scale_min = config['scale_min']
            scale_max = config['scale_max']
            overwrite_handlers = config['overwrite_handlers']
            project_directory = config['project_directory']
            figma_token = config['figma_token']
            figma_file_url = config['figma_file_url']
            update_ui()


def save_config():
    global scale, scale_min, scale_max, overwrite_handlers, project_directory, figma_token, figma_file_url
    config = {
        'scale': scale,
        'scale_min': scale_min,
        'scale_max': scale_max,
        'overwrite_handlers': overwrite_handlers,
        'project_directory': project_directory,
        'figma_token': figma_token,
        'figma_file_url': figma_file_url
    }
    with open(config_file_name, 'w') as file:
        json.dump(config, file)


def update_ui():
    # set slider scale value
    PyqtFigmaDesignerGuiV3Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        CompileOptions0Controller. \
        GroupSliderScale0Controller. \
        slider_scale_1_set_value(scale_to_slider(scale))

    # set figma token text
    PyqtFigmaDesignerGuiV3Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        DownloadOptions0Controller. \
        GroupTextFieldFigmaToken0Controller. \
        custom_text_field_figma_token_1_set_text(figma_token)

    # set project directory text
    PyqtFigmaDesignerGuiV3Controller. \
        TabsView0Controller. \
        Background0Controller. \
        GroupTextFieldProjectDirectory0Controller. \
        custom_text_field_directory_1_set_text(project_directory)

    # set figma file url text
    PyqtFigmaDesignerGuiV3Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        DownloadOptions0Controller. \
        GroupTextFieldFigmaToken2Controller. \
        custom_text_field_figma_token_4_set_text(figma_file_url)

    # set overwrite handlers checkbox
    PyqtFigmaDesignerGuiV3Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        CompileOptions0Controller. \
        checkbox_overwrite_handlers_1_set_checked(overwrite_handlers)

    # set scale text
    PyqtFigmaDesignerGuiV3Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        CompileOptions0Controller. \
        GroupSliderScale0Controller. \
        x1_0_set_text(f'x{scale:.2f}')


def browse_directory():
    global project_directory
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.Directory)
    file_dialog.setOption(QFileDialog.ShowDirsOnly, True)
    file_dialog.exec()
    project_directory = file_dialog.selectedFiles()[0]


def download_figma_file():
    download_command = f'python pyqtfd-download.py -p "{project_directory}" -t {figma_token} -url "{figma_file_url}"'
    print(download_command)
    process = subprocess.Popen(download_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               cwd=runner_directory)
    for line in process.stdout.readlines():
        print(line.decode('utf-8').strip())
    return_code = process.wait()
    if return_code != 0:
        message_box = QMessageBox()
        message_box.setText("Download failed!")
        message_box.exec()
        return


def compile_project():
    compile_command = f'python pyqtfd-compile.py -p "{project_directory}" -s {scale} -oh {overwrite_handlers}'

    print(compile_command)
    process = subprocess.Popen(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               cwd=runner_directory)
    for line in process.stdout.readlines():
        print(line.decode('utf-8').strip())
    return_code = process.wait()
    if return_code != 0:
        message_box = QMessageBox()
        message_box.setText("Compilation failed!")
        message_box.exec()
        return

    message_box = QMessageBox()
    message_box.setText("Project created successfully!")
    message_box.exec()
    process = subprocess.Popen(f'python gui.py', shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, cwd=project_directory)
    for line in process.stdout.readlines():
        print(line.decode('utf-8').strip())
