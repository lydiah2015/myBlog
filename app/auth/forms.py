from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField
from wtforms.validators import Required,EqualTo,DataRequired,Length,Email

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 32)])
    password = PasswordField('Password', validators=[
        DataRequired()])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 32)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')