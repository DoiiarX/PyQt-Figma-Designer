import argparse

import requests
import json
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
parser.add_argument('-ni', '--no-images',
                    help='Do not download images',
                    action='store_true',
                    required=False,
                    dest='no_images')

if __name__ == '__main__':
    args = parser.parse_args()

    config.set_url(args.url)
    config.set_project_directory(args.path)
    config.token = args.token
    config.check_project_directory()
    print('Downloading figma file...')
    figma_file = endpoints.Files(config.token, config.file_key)
    f = figma_file.get_file()

    with open(config.figma_file_path, 'w', encoding='utf8') as file:
        json.dump(f, file, ensure_ascii=False, indent=4)

    if not args.no_images:
        print('Downloading images...')
        images = figma_file.get_images()
        for i, (image_id, image_url) in enumerate(images.items()):

            # download the url to outputs/id.png
            response = requests.get(image_url)
            with open(f'{config.image_directory}/{image_id}.png', 'wb') as file:
                file.write(response.content)
