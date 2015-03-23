from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required, Length, Email, EqualTo


class LoginForm(Form):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])

    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(Form):
    nickname = TextField('nickname', validators=[Required(), Length(min=3, max=25)])
    email = TextField('email', validators=[Required(), Email(message=None), Length(min=6, max=40)])
    password = PasswordField('password', validators=[Required(), Length(min=6, max=25)])
    confirm = PasswordField('Repeat password', validators=[
        Required(), EqualTo('password', message='Passwords must match.')])
