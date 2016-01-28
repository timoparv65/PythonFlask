#28.1.201
#tänne määritellään kaikki käytetyt formit

from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField#kentät löytää kalvon sivulta 52
from wtforms.validators import Required,Email#validaatorit kts kalvon sivu 53

#luodaan luokka joka perii Form:in
class LoginForm(Form):
    email = StringField('Enter your email',validators=[Required(),Email()])#Required = kentässä oltava tekstiä, Emai = email oltava validi
    passw = PasswordField('Enter password',validators=[Required()])
    submit = SubmitField('Login')