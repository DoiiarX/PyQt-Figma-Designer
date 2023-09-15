import json
import os
import pathlib
import subprocess

from PySide6.QtWidgets import QFileDialog, QMessageBox

from gui_controller import PyqtFigmaDesignerGuiV4Controller

runner_directory = pathlib.Path(__file__).parent.parent.absolute()

tab = 0

scale = 1
scale_min = 0.25
scale_max = 4

text_scale = 1
text_scale_min = 0.5
text_scale_max = 2

clear_project = False
overwrite_handlers = False
overwrite_config = False
overwrite_strings = False
skip_images = False

project_directory = ""
figma_token = ""
figma_file_url = ""

config_file_name = "pyqtfd-config.json"


def slider_to_scale(value: float, v_min: float, v_max: float):
    return value * (v_max - v_min) + v_min


def scale_to_slider(value: float, v_min: float, v_max: float):
    return (value - v_min) / (v_max - v_min)


def load_config():
    global scale, scale_min, scale_max, overwrite_handlers, project_directory, figma_token, figma_file_url, \
        overwrite_config, overwrite_strings, text_scale, text_scale_min, text_scale_max, tab, skip_images, clear_project
    if os.path.exists(config_file_name):
        with (open(config_file_name, 'r') as file):
            config = json.load(file)
            tab = config['tab']
            scale = config['scale']
            scale_min = config['scale_min']
            scale_max = config['scale_max']
            overwrite_handlers = config['overwrite_handlers']
            project_directory = config['project_directory']
            figma_token = config['figma_token']
            figma_file_url = config['figma_file_url']
            overwrite_config = config['overwrite_config']
            overwrite_strings = config['overwrite_strings']
            text_scale = config['text_scale']
            text_scale_min = config['text_scale_min']
            text_scale_max = config['text_scale_max']
            skip_images = config['skip_images']
            clear_project = config['clear_project']
            update_ui()


def save_config():
    config = {
        'tab': tab,
        'scale': scale,
        'scale_min': scale_min,
        'scale_max': scale_max,
        'overwrite_handlers': overwrite_handlers,
        'project_directory': project_directory,
        'figma_token': figma_token,
        'figma_file_url': figma_file_url,
        'overwrite_config': overwrite_config,
        'overwrite_strings': overwrite_strings,
        'text_scale': text_scale,
        'text_scale_min': text_scale_min,
        'text_scale_max': text_scale_max,
        'skip_images': skip_images,
        'clear_project': clear_project
    }
    with open(config_file_name, 'w') as file:
        json.dump(config, file)


def update_ui():
    # set slider scale value
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Compile0Controller. \
        GroupSliderScale0Controller. \
        slider_scale_1_set_value(scale_to_slider(scale, scale_min, scale_max))
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Compile0Controller. \
        GroupSliderScale0Controller. \
        x1_0_set_text(f'x{scale:.2f}')

    # set slider text scale value
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Compile0Controller. \
        GroupSliderTextScale0Controller. \
        slider_scale_4_set_value(scale_to_slider(text_scale, text_scale_min, text_scale_max))
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Compile0Controller. \
        GroupSliderTextScale0Controller. \
        x1_2_set_text(f'x{text_scale:.2f}')

    # set overwrite handlers checkbox
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Compile0Controller. \
        checkbox_overwrite_handlers_1_set_checked(overwrite_handlers)

    # set overwrite config checkbox
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Compile0Controller. \
        checkbox_overwrite_config_1_set_checked(overwrite_config)

    # set overwrite strings checkbox
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Compile0Controller. \
        checkbox_overwrite_strings_1_set_checked(overwrite_strings)

    # set project directory text
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        GroupTextFieldProjectDirectory0Controller. \
        custom_text_field_directory_1_set_text(project_directory)

    # set figma token text
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Download0Controller. \
        GroupTextFieldFigmaToken0Controller. \
        custom_text_field_figma_token_1_set_text(figma_token)

    # set figma file url text
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Download0Controller. \
        GroupTextFieldFigmaToken2Controller. \
        custom_text_field_figma_token_4_set_text(figma_file_url)

    # set clear project checkbox
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        CreateProject0Controller. \
        checkbox_clear_project_directory_1_set_checked(clear_project)

    # set skip images checkbox
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller. \
        TabsView0Controller. \
        TabsContent0Controller. \
        Download0Controller. \
        checkbox_skip_images_1_set_checked(skip_images)

    # set tab
    PyqtFigmaDesignerGuiV4Controller. \
        PyqtFigmaDesignerGuiV42Controller.tabs_view_1_set_tab(tab)


def browse_directory():
    global project_directory
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.Directory)
    file_dialog.setOption(QFileDialog.ShowDirsOnly, True)
    file_dialog.setDirectory('..')
    file_dialog.exec()
    project_directory = file_dialog.selectedFiles()[0]
    update_ui()


def create_project():
    global tab
    create_project_command = f'python pyqtfd-create.py -p "{project_directory}"'
    if clear_project:
        create_project_command += ' -c'
    print(create_project_command)
    process = subprocess.Popen(create_project_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               cwd=runner_directory)
    for line in process.stdout.readlines():
        print(line.decode('utf-8').strip())
    return_code = process.wait()
    message_box = QMessageBox()
    if return_code != 0:
        message_box.setText("Create project failed!")
    else:
        message_box.setText("Create project done!")
        tab += 1
    message_box.exec()
    update_ui()


def download_figma_file():
    global tab
    download_command = f'python pyqtfd-download.py -p "{project_directory}" -t {figma_token} -url "{figma_file_url}"'
    if skip_images:
        download_command += ' -ni'
    print(download_command)
    process = subprocess.Popen(download_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               cwd=runner_directory)
    for line in process.stdout.readlines():
        print(line.decode('utf-8').strip())
    return_code = process.wait()
    message_box = QMessageBox()
    if return_code != 0:
        message_box.setText("Download failed!")
    else:
        message_box.setText("Download done!")
        tab += 1
    message_box.exec()
    update_ui()


def compile_project():
    global tab
    flags = f'-p "{project_directory}" -s {scale} -ts {text_scale}'
    if overwrite_config:
        flags += ' -owc'
    if overwrite_strings:
        flags += ' -ows'
    if overwrite_handlers:
        flags += ' -owh'
    compile_command = f'python pyqtfd-compile.py  {flags}'

    print(compile_command)
    process = subprocess.Popen(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               cwd=runner_directory)
    for line in process.stdout.readlines():
        print(line.decode('utf-8').strip())

    return_code = process.wait()
    message_box = QMessageBox()
    if return_code != 0:
        message_box.setText("Compile failed!")
    else:
        message_box.setText("Compile done!")
        tab += 1
    message_box.exec()
    update_ui()


def run_project():
    process = subprocess.Popen(f'python gui.py', shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, cwd=project_directory)
    for line in process.stdout.readlines():
        print(line.decode('utf-8').strip())
    return_code = process.wait()
    message_box = QMessageBox()
    if return_code != 0:
        message_box.setText("Run finished with errors!")
    else:
        message_box.setText("Run finished successfully!")
    message_box.exec()
