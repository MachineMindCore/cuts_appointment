from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, Form, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length, InputRequired

class SignupForm(FlaskForm):
    username  = StringField('Usuario', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=4, max=16)])
    password  = PasswordField('Contraseña', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=8, max=16)])
    email = StringField("Email", validators=[InputRequired(message="Este campo no puede estar vacio"), Email(message="Este no es un email valido"), Length(max=60)])
    firstName  = StringField('Nombre', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=4, max=16)])
    lastName  = StringField('Apellido', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=4, max=16)])
    number  = StringField('Numero de celular', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=4, max=16)])
    enviar = SubmitField('Registro')


class LoginForm(FlaskForm):
    username  = StringField('Usuario', validators=[InputRequired(message="Este campo no puede estar vacio"),
Length(min=4, max=16, message="El nombre del usuario tiene que tener entre %(min)d y %(max)d caracteres")])
    password  = PasswordField('Contraseña', validators=[InputRequired(message="Este campo no puede estar vacio"),
Length(min=8, max=16, message="La contraseña tiene que tener entre %(min)d y %(max)d caracteres")])
    remember  = BooleanField('Recordarme')
    enviar = SubmitField('Inicia sesion')


class ProductForm(Form):
    title = StringField('Title')
    price = IntegerField('Price')

class InventoryForm(FlaskForm):
    category_name = StringField('Category Name')
    products = FieldList(FormField(ProductForm))