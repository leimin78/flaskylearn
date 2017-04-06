from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from ..models import User

class LoginForm(Form):
    email = StringField('email',validators=[Required(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('keep me log in')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    email = StringField('email',validators=[Required(),Length(1,64),Email()])
    username = StringField('username',validators=[Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password',validators=[Required(),EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confrim Password',validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, fid):
        if User.query.filter_by(email=fid.data).first():
            raise ValidationError('Email already registered.')
    def validate_username(self, fid):
        if User.query.filter_by(username=fid.data).first():
            raise ValidationError('Username already in use.')