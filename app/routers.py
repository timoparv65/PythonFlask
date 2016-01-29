"""app kansiosta haetaan objektia app"""
from app import app
#render_template gives you access to Jinja2 template engine
#request objektista voidaan kaivaa kaikki mitä tulee BackEndiin (client lähettää)
#flash = Flash viestejä varten
from flask import render_template,request,make_response,flash,redirect
from app.forms import LoginForm,RegisterForm#29.1.2016 tuo formit forms.py:stä
from app.db_models import Users#29.1.2016 tuodaan Users malli
from app import db# 29.1.2016 tuodaan tietokanta

#tämä on myös tapa kommentoida, vain yhdelle riville
"""This is comment
    you can use multiple lines"""

#Routerin on aina palautettava vastaus

#kun pyyntö tulee serveriltä root kontekstiin, määritellään funktio index()
#@app => @ = decoration, käskee frameworkkia tekemään asialle jotain
@app.route('/',methods=['GET','POST'])
def index():
    login = LoginForm()#login objekti
    if request.method == 'GET':#29.1.2016 lisätty alla oleva
        return render_template('template_index.html',form=login)
    else:
        #check if form data is valid
        if login.validate_on_submit():#tsekkaa onko formit valideja
            print(login.email.data)
            print(login.passw.data)
            return render_template('template_user.html')
        #form data was not valid
        else:
            flash('Give proper information to email and password fields!')#näyttö toteutettu base.html:ssä (kalvo s.56)
            return render_template('template_index.html',form=login)

#29.1.2016 harjoitustehtävä: routteri rekisteröintiin
@app.route('/register',methods=['GET','POST'])
def registerUser():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('template_register.html',form=form)
    else:
        if form.validate_on_submit():
            user = Users(form.email.data,form.passw.data)
            db.session.add(user)
            db.session.commit()#ei otettu kantaa jos tietokantaan tallentaminen epäonnistuu
            flash("Name {0} registered".format(form.email.data))
            return redirect('/')
        else:
            flash('Invalid email address or no password given')
            return render_template('template_register.html',form=form)

#tämä ns. clean url
@app.route('/user/<name>')#konteksti user
def user(name):#funktio user
    print(request.headers.get('User-Agent'))#voidaan tutkia esim käytetäänkö aplikaatiota mobiililaitteella ja toimia sen mukaan
    print(request.headers.get('Accept-Language'))
    return render_template('template_user.html',name=name)
    #kutsu localhost:3000/user/timo

#luetaan formista tullut data
#Example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)
    #kutsutaan
