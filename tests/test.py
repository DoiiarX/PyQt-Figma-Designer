import re

from figma import endpoints


def show_dict_tree(d: dict, i=0):
    for k, v in d.items():
        if isinstance(v, dict):
            print(' ' * i + k)
            show_dict_tree(v, i + 1)
        else:
            print(' ' * i + k + ': ' + str(v))


token = 'figd_-QMtU_8nZoTs48qAzWTqQecktPRyh3gCI9rR0Jx5'
file_url = 'https://www.figma.com/file/DEtNOgq9OGnkGPfPpiQeEK/Untitled?type=design&mode=design&t=MXkH4iNj09GBg1aG-0'

match = re.search(r'https://www.figma.com/file/([0-9A-Za-z]+)', file_url.strip())
file_key = match.group(1).strip()
print(file_key)
figma_file = endpoints.Files(token, file_key)
f = figma_file.get_file()
show_dict_tree(f['document']['children'][0]['children'][0])
