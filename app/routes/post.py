from flask import Blueprint
from ..extensions import db
from..models.post import Post


post = Blueprint('post', __name__)


@post.route('/post/<content>')
def create_post(content):
    new_post = Post(content=content)
    db.session.add(new_post)
    db.session.commit()
    return f'Creating post: {content}'