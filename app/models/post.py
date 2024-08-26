from datetime import datetime
from ..extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.String(255))
    student = db.Column(db.String(255))
    subject = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
