import argparse
import os
import shutil

import config

parser = argparse.ArgumentParser(
    prog='PyQt Figma Designer Project Creator',
    description='This program allows you to create a PyQt-Figma-Designer project structure.')

parser.add_argument('-p', '--project',
                    help='Project directory',
                    action='store',
                    required=True,
                    dest='path')
parser.add_argument('-c', '--clear',
                    help='Clear project directory',
                    action='store_true',
                    required=False,
                    default=False,
                    dest='clear')

if __name__ == '__main__':
    args = parser.parse_args()
    config.set_project_directory(args.path)

    if args.clear:
        if os.path.exists(config.project_directory):
            shutil.rmtree(config.project_directory)

    if not os.path.exists(config.project_directory):
        os.makedirs(config.project_directory, exist_ok=True)
    if not os.path.exists(config.image_directory):
        os.makedirs(config.image_directory, exist_ok=True)
    if not os.path.exists(config.svg_directory):
        os.makedirs(config.svg_directory, exist_ok=True)

    config.check_project_directory()

    print('Project structure created !')
