import argparse
import pickle

import requests

import config
from figma import endpoints

parser = argparse.ArgumentParser(
    prog='PyQt Figma Designer Downloader',
    description='This program allows you to generate a PyQt-Figma-Designer project from a Figma URL.',
    epilog='This program was created by Romain Birling (github.com/rombirli)')

parser.add_argument('-p', '--project',
                    help='Project directory',
                    action='store',
                    required=True,
                    dest='path')
parser.add_argument('-t', '--token',
                    help='Figma token',
                    action='store',
                    required=True,
                    dest='token')
parser.add_argument('-url', '--url',
                    help='Figma URL',
                    action='store',
                    required=True,
                    dest='url')

if __name__ == '__main__':
    args = parser.parse_args()

    config.set_url(args.url)
    config.set_project_directory(args.path)
    config.create_project_directories()
    config.token = args.token

    figma_file = endpoints.Files(config.token, config.file_key)
    f = figma_file.get_file()

    with open(config.figma_file_path, 'wb') as file:
        pickle.dump(f, file)

    for image_id, image_url in figma_file.get_images().items():
        # download the url to outputs/id.png
        response = requests.get(image_url)
        with open(f'{config.image_directory}/{image_id}.png', 'wb') as file:
            file.write(response.content)
