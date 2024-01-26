from wtforms import Form
from wtforms import SearchField, TextAreaField, RadioField, TextField, StringField, SelectField
from wtforms import EmailField

class UserForm(Form):
    nombre=StringField("nombre")
    email=EmailField("email")
    apaterno=TextField("apaterno")
    materias=SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingels', 'ING')])
    radios=RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])