import uuid

from flask import Flask
from .extensions import db


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = str(uuid.uuid4())

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
