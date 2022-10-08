

# RUTAS

home = Blueprint('home', __name__, template_folder='templates',
                 static_folder='static')


@home.route('/')
def index():
    template_vars = {
        "title": "Barber",
        "state": "inicio"
    }
    return render_template("index.html", **template_vars)


@home.route('/salon')
def salon():
    template_vars = {
        "title": "Barber - Salon",
        "state": "salon"
    }
    return render_template("salon.html", **template_vars)


@home.route("/registro", methods=['GET', 'POST'])
def register():
    registro = CreateUserForm()

    if registro.validate_on_submit():
        new_user = User(username=registro.username.data, email=registro.email.data, password=registro.password.data,
                        firstName=registro.firstName.data, lastName=registro.lastName.data, number=registro.number.data, flag="1")
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('register.html', formi=registro)


@home.route("/login", methods=['GET', 'POST'])
def login():
    login = Loginform()

    if login.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', formi=login)


# FORMS.PY
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import  InputRequired, Email, Length   


class Loginform(FlaskForm):
    username  = StringField('Usuario', validators=[InputRequired(message="Este campo no puede estar vacio"),
Length(min=4, max=16, message="El nombre del usuario tiene que tener entre %(min)d y %(max)d caracteres")])
    password  = PasswordField('Contraseña', validators=[InputRequired(message="Este campo no puede estar vacio"),
Length(min=8, max=16, message="La contraseña tiene que tener entre %(min)d y %(max)d caracteres")])
    remember  = BooleanField('Recordarme')
    enviar = SubmitField('Inicia sesion')

class CreateUserForm(FlaskForm):
   
    username  = StringField('Usuario', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=4, max=16)])
    password  = PasswordField('Contraseña', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=8, max=16)])
    email = StringField("Email", validators=[InputRequired(message="Este campo no puede estar vacio"), Email(message="Este no es un email valido"), Length(max=60)])
    firstName  = StringField('Nombre', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=4, max=16)])
    lastName  = StringField('Apellido', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=4, max=16)])
    number  = StringField('Numero de celular', validators=[InputRequired(message="Este campo no puede estar vacio"), Length(min=4, max=16)])
    enviar = SubmitField('Registro')

# DATABASE.PY
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True, nullable=False)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(10), unique=True, nullable=False)
    flag = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f'{self.id, self.username, self.email, self.password}'