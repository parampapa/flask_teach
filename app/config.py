import os
import uuid


class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload/'
    SERVER_PATH = ROOT + UPLOAD_PATH

    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SECRET_KEY = str(uuid.uuid4())
