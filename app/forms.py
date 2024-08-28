from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Length, EqualTo
from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField('ФИО',
                       validators=[Length(min=2, max=20), DataRequired()])
    login = StringField('Login',
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                                   Length(min=8, max=30)])
    confirmPassword = StringField('Подтвердите пароль',
                                  validators=[DataRequired(),
                                              EqualTo('password')])
    avatar = FileField('Загрузите аватар',
                       validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Register')








