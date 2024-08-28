from flask import Blueprint, render_template, redirect

from ..forms import RegistrationForm
from ..extensions import db
from ..models.user import User


user = Blueprint('user', __name__)


@user.route('/user/register')
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.login.data)
        print(form.password.data)
        redirect('/')
    else:
        print('Ошибка в данных')
    return render_template('user/register.html')
