from flask_migrate import Migrate

from config.manage_app import create_app
from config.global_params import db
from server_src.models import *

manage = create_app()
migrate = Migrate(manage, db)

if __name__ == '__main__':
    '''Default launch script.'''
    manage.run(host='0.0.0.0', port='9100')
