from flask import Blueprint
from ..extensions import db
from ..models.user import User


user = Blueprint('user', __name__)


@user.route('/')
def index():
    return 'User API'
