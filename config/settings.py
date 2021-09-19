import os
import socket

# project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_FOLDER = os.path.join(BASE_DIR, 'statics')
STATIC_PATH = '/static'

# upload file absolute directory
# UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'upload')

SALT = r'iw2!@5&mj><ak'
KEY = r'908&#af43$13t4dj'

HTTP_NAME = socket.gethostname()
HTTP_IP = socket.gethostbyname(HTTP_NAME)
HTTP_HOST = f'http://{HTTP_IP}:9096'
