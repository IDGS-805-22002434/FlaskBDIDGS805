from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField, EmailField, validators

class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField("nombre", {
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese un nombre valido")
    })
    apellidos=StringField("apellidos", {
        validators.DataRequired(message="El campo es requerido"),

    })
    email=EmailField("email", {
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingresa correo valido")
        
    })
    telefono=StringField("telefono", {
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="El numero solo deben ser 10 digitos")
        
    })