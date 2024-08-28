from flask import Blueprint, render_template, redirect, flash

from ..functions import save_picture
from ..forms import RegistrationForm
from ..extensions import db, bcrypt
from ..models.user import User


user = Blueprint('user', __name__)


@user.route('/user/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        avatar_filename = save_picture(form.avatar.data)
        user = User(name=form.name.data,
                    login=form.login.data,
                    password=hashed_password,
                    avatar=avatar_filename)
        db.session.add(user)
        db.session.commit()
        flash(f'Поздравляем {form.login.data}, регистрация успешна', 'success')
        return redirect('/')
    else:
        print('Ошибка в данных')
    return render_template('user/register.html', form=form)
