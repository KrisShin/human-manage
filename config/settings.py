import socket
from pathlib import Path

# project root directory
BASE_DIR = Path.cwd()

STATIC_FOLDER = BASE_DIR / 'statics'
STATIC_PATH = '/static'

# upload file absolute directory
# UPLOAD_DIR = os.path.join(STATIC_PATH, 'upload')

SALT = r'iw2!@5&mj><ak'
KEY = r'908&#af43$13t4dj'

# 获取本机计算机名称
HOST_NAME = socket.gethostname()
# 获取本机ip
HOST_IP = socket.gethostbyname(HOST_NAME)

if HOST_IP == '127.0.1.1':
    HOST_IP = '101.34.137.128'

# HTTP_HOST = r'http://127.0.0.1:12005'
HTTP_HOST = f'http://{HOST_IP}:9100'
IMAGE_PREFIX = f'{HTTP_HOST}{STATIC_PATH}'
