import config

url = ''
api_token = ''
output_directory = ''
checkbox_overwrite_handler = True


def q_Text_Field_Inut_File_URL___text_changed(current_text: str):
    global url
    url = current_text


def q_Text_Field_Figma_API_Token___text_changed(current_text: str):
    global api_token
    api_token = current_text


def q_Text_Field_Output_Directory___text_changed(current_text: str):
    global output_directory
    output_directory = current_text


def q_ButtonCreateProject___clicked():
    config.set_url(url)
    config.set_project_directory(output_directory)
    config.token = api_token
    config.overwrite_handler_controller = checkbox_overwrite_handler
    print('Reading Figma file (+png)...')
    import runner.read_figma
    print('Writing Python code (+svg)...')
    import runner.write_python
    print('Running GUI...')
    import subprocess
    subprocess.Popen(f'python {config.project_directory}/gui.py')


def q_ButtonBrowse___clicked():
    print("Button q_ButtonBrowse__ clicked")


def q_CheckboxOverwriteHandler_check_changed(checked: bool):
    global checkbox_overwrite_handler
    checkbox_overwrite_handler = checked
