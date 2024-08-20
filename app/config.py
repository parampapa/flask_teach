import uuid


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SECRET_KEY = str(uuid.uuid4())
