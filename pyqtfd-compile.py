import argparse
import json
import os

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
parser.add_argument('-owh', '--overwrite-handler',
                    help='Overwrite handlers file.',
                    action='store_true',
                    required=False,
                    default=False,
                    dest='overwrite_handler')
parser.add_argument('-ows', '--overwrite-strings',
                    help='Overwrite strings file.',
                    action='store_true',
                    required=False,
                    default=False,
                    dest='overwrite_strings')
parser.add_argument('-owc', '--overwrite-config',
                    help='Overwrite config file.',
                    action='store_true',
                    required=False,
                    default=False,
                    dest='overwrite_config')

if __name__ == '__main__':
    args = parser.parse_args()
    config.scale = args.scale
    config.overwrite_handler = args.overwrite_handler
    config.set_project_directory(args.path)
    config.check_project_directory()

    with open(config.figma_file_path, 'r', encoding='utf-8') as file:
        figma_file = json.load(file)
    figma_node = figma_file['document']['children'][0]
    script_generator = generator.design.core.script_generator.ScriptGenerator(figma_node, None)
    python_code = '\n'.join(script_generator.generate_design())
    handler_code = '\n'.join(script_generator.generate_handler())
    controller_code = '\n'.join(script_generator.generate_controller())
    strings_code = '\n'.join(script_generator.generate_strings())
    config_code = '\n'.join(script_generator.generate_config())
    with open(config.gui_path, 'w', encoding="utf-8") as file:
        file.write(python_code)
    with open(config.gui_controller_path, 'w', encoding="utf-8") as file:
        file.write(controller_code)

    if args.overwrite_handler or not os.path.exists(config.gui_handler_path):
        with open(config.gui_handler_path, 'w', encoding="utf-8") as file:
            file.write(handler_code)
    if args.overwrite_strings or not os.path.exists(config.strings_path):
        with open(config.strings_path, 'w', encoding="utf-8") as file:
            file.write(strings_code)
    if args.overwrite_config or not os.path.exists(config.components_config_path):
        with open(config.components_config_path, 'w', encoding="utf-8") as file:
            file.write(config_code)

