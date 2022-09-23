from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=10)])
    password = PasswordField('password', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    number = IntegerField('number', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('submit')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=10)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember')
    submit = SubmitField('submit')

