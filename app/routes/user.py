from flask import Blueprint, render_template
from ..extensions import db
from ..models.user import User


user = Blueprint('user', __name__)


@user.route('/user')
def get_user():
    return 'Look'
