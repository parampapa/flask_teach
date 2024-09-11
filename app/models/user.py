from datetime import datetime
from ..extensions import db
from flask_login import UserMixin


class User(db.Modelm, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), default='user')
    avatar = db.Column(db.String(200))
    name = db.Column(db.String(50), unique=True, nullable=False)
    login = db.Column(db.String(50))
    password = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=datetime.utcnow)
