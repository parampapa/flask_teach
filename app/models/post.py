from datetime import datetime
from ..extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.Integer, db.ForeignKey('user.id',
                                                  ondelete="CASCADE",
                                                  name='fk_post_teacher'))
    student = db.Column(db.Integer)
    subject = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

