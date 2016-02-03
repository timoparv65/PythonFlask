#28.1.201
#tänne määritellään kaikki käytetyt formit

from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField,IntegerField#kentät löytää kalvon sivulta 52
from wtforms.validators import Required,Email,NumberRange#validaatorit kts kalvon sivu 53

#luodaan luokka joka perii Form:in
class LoginForm(Form):
    email = StringField('Enter your email',validators=[Required(),Email()])#Required = kentässä oltava tekstiä, Emai = email oltava validi. 'Enter your email' => label
    passw = PasswordField('Enter password',validators=[Required()])
    submit = SubmitField('Login')

#lisätty 29.1.2016
class RegisterForm(Form):
    email = StringField('Enter your valid email address',validators=[Required(),Email()])
    passw = PasswordField('Give password for this application',validators=[Required()])
    submit = SubmitField('Register')
    
#lisätty 3.2.2016
class FriendForm(Form):
    name = StringField('Enter friend name',validators=[Required()])
    address = StringField('Enter friend address',validators=[Required()])
    age = IntegerField('Enter friend age',validators=[Required(),NumberRange(min=0,max=115,message="Enter value between %(min)-%(max))")])
    submit = SubmitField('Save')
