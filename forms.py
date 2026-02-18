from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField, EmailField, validators

class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField("nombre", {
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese un nombre valido")
    })
    apaterno=StringField("apaterno", {
        validators.DataRequired(message="El campo es requerido"),

    })
    email=EmailField("email", {
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingresa correo valido")
        
    })