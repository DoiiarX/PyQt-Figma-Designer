import re

token = 'figd_-QMtU_8nZoTs48qAzWTqQecktPRyh3gCI9rR0Jx5'
# below test figma file (complete design)
file_url = 'https://www.figma.com/file/DEtNOgq9OGnkGPfPpiQeEK/Untitled?type=design&mode=design&t=MXkH4iNj09GBg1aG-0'
# below test figma file (one element at a time)
file_url = 'https://www.figma.com/file/PExygXiMSTBEpXXEq0ZPyE/Untitled?type=design&node-id=0-1&mode=design&t=D4pN9YixWIbPDYlb-0'

match = re.search(r'https://www.figma.com/file/([0-9A-Za-z]+)', file_url.strip())
file_key = match.group(1).strip()

scale = .7
