import argparse
import pickle
import config
import generator.design.core.script_generator

parser = argparse.ArgumentParser(
    prog='PyQt Figma Designer Compiler',
    description='This program allows you to compile a PyQt-Figma-Designer to a Python project.',
    epilog='This program was created by Romain Birling (github.com/rombirli)')

parser.add_argument('-p', '--project',
                    help='Project directory',
                    action='store',
                    required=True,
                    dest='path')
parser.add_argument('-s', '--scale',
                    help='Scale',
                    action='store',
                    required=False,
                    default=1.0,
                    type=float,
                    dest='scale')
parser.add_argument('-oh', '--overwrite-handler',
                    help='Overwrite handler',
                    action='store',
                    required=False,
                    default=False,
                    type=bool,
                    dest='overwrite_handler')

if __name__ == '__main__':
    args = parser.parse_args()
    config.scale = args.scale
    config.overwrite_handler = args.overwrite_handler
    config.set_project_directory(args.path)

    with open(config.figma_file_path, 'rb') as file:
        figma_file = pickle.load(file)
    figma_node = figma_file['document']['children'][0]
    script_generator = generator.design.core.script_generator.ScriptGenerator(figma_node, None)
    python_code = '\n'.join(script_generator.generate_design())
    handler_code = '\n'.join(script_generator.generate_handler())
    controller_code = '\n'.join(script_generator.generate_controller())
    strings_code = '\n'.join(script_generator.generate_strings())
    with open(config.gui_path, 'w', encoding="utf-8") as file:
        file.write(python_code)
    with open(config.gui_controller_path, 'w', encoding="utf-8") as file:
        file.write(controller_code)
    with open(config.strings_path, 'w', encoding="utf-8") as file:
        file.writelines(strings_code)
    if config.overwrite_handler:
        with open(config.gui_handler_path, 'w', encoding="utf-8") as file:
            file.write(handler_code)
