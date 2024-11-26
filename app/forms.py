from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

class RegisterForm(FlaskForm):
    first_name = StringField('Nombre', validators=[
        DataRequired(), Length(min=2), Regexp('^[a-zA-Z]+$', message='Solo letras.')
    ])
    last_name = StringField('Apellido', validators=[
        DataRequired(), Length(min=2), Regexp('^[a-zA-Z]+$', message='Solo letras.')
    ])
    email = StringField('Correo', validators=[
        DataRequired(), Email()
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(), Length(min=8),
        Regexp('^(?=.*[A-Z])(?=.*\d)', message='Debe incluir una mayúscula y un número.')
    ])
    confirm_password = PasswordField('Confirmar contraseña', validators=[
        DataRequired(), EqualTo('password', message='Las contraseñas no coinciden.')
    ])
    submit = SubmitField('Registrarse')
