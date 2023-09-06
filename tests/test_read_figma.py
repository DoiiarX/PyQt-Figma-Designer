import re
import pickle
from figma import endpoints

token = 'figd_-QMtU_8nZoTs48qAzWTqQecktPRyh3gCI9rR0Jx5'
file_url = 'https://www.figma.com/file/DEtNOgq9OGnkGPfPpiQeEK/Untitled?type=design&mode=design&t=MXkH4iNj09GBg1aG-0'

match = re.search(r'https://www.figma.com/file/([0-9A-Za-z]+)', file_url.strip())
file_key = match.group(1).strip()
figma_file = endpoints.Files(token, file_key)
f = figma_file.get_file()

with open('../resources/f.fig', 'wb') as file:
    pickle.dump(f, file)
