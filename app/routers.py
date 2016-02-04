# Tämä on serveripään tiedosto

"""app kansiosta haetaan objektia app"""
from app import app
#render_template gives you access to Jinja2 template engine
#request objektista voidaan kaivaa kaikki mitä tulee BackEndiin (client lähettää)
#flash = Flash viestejä varten
#session = session objekti käyttäjästä (3.2.2016)
from flask import render_template,request,make_response,flash,redirect,session
from app.forms import LoginForm,RegisterForm,FriendForm
from app.db_models import Users,Friends
from app import db

from flask.ext.bcrypt import check_password_hash#lisätty 4.2.2016

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
        return render_template('template_index.html',form=login,isLogged=False)
    else:
        #check if form data is valid
        if login.validate_on_submit():#tsekkaa onko formit valideja
            #3.2.2016 Check if correct username or password
            #user = Users.query.filter_by(email=login.email.data).filter_by(passw=login.passw.data)
            #yllä oleva luo SQL-lauseen: Select email passw From User Where email="?" And passw="?"
            
            #4.2.2016 passw on kryptattu
            # Check if correct username
            user = Users.query.filter_by(email=login.email.data)
            print(user)
            #if user.count() == 1:#3.2.2016 jos palautetun taulukon koko on yksi
            #4.2.2016: user[0].passw = kryptattu salasana
            if (user.count() == 1) and (check_password_hash(user[0].passw,login.passw.data)):
                print(user[0])
                session['user_id'] = user[0].id#tallennetaan käyttäjän ID
                session['isLogged'] = True
                print(session['user_id'])
                #Haetaan ystävät
                #tapa 1 listata ystävät
                friends = Friends.query.filter_by(user_id =user[0].id)
                print(friends)
                return render_template('template_user.html',isLogged=True,friends=friends)
            else:
                flash('Wrong email or password')
                return render_template('template_index.html',form=login,isLogged=False)
        #form data was not valid
        else:
            flash('Give proper information to email and password fields!')#näyttö toteutettu base.html:ssä (kalvo s.56)
            return render_template('template_index.html',form=login,isLogged=False)

#29.1.2016 harjoitustehtävä: routteri rekisteröintiin
@app.route('/register',methods=['GET','POST'])
def registerUser():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('template_register.html',form=form,isLogged=False)
    else:
        if form.validate_on_submit():
            user = Users(form.email.data,form.passw.data)
            try:
                db.session.add(user)
                db.session.commit()#ei otettu kantaa jos tietokantaan tallentaminen epäonnistuu
            except:
                db.session.rollback()#jos jotain tietoa meni tietokantaan, se otetaan pois
                flash('Username allready in use')
                return render_template('template_register.html',form=form,isLogged=False)
            flash("Name {0} registered".format(form.email.data))
            return redirect('/')
        else:
            flash('Invalid email address or no password given')
            return render_template('template_register.html',form=form,isLogged=False)

#Lisätty 3.2.2016
@app.route('/friends',methods=['GET','POST'])
def friends():
    #routen suojaus
    #Check that user has logged in before you let execute
    if not('isLogged' in session) or (session['isLogged'] == False):
        return redirect('/')#palataan login näkymään
    #lisää ylle: suojaukseen voi käyttää myös valmiita komponentteja Flask-user
    #(vaatii Microsoftin softaa) tai Flask-login:ia
    form = FriendForm()
    if request.method == 'GET':
        return render_template('template_friends.html',form=form,isLogged=True)
    else:
        if form.validate_on_submit():
            temp = Friends(form.name.data,form.address.data,form.age.data,session['user_id'])
            db.session.add(temp)
            db.session.commit()
            #2. tapa listata ystävät. Kts db_models.py
            user = Users.query.get(session['user_id'])
            print(user.friends)
            return render_template('template_user.html',isLogged=True,friends=user.friends)
        else:
            flash('Give proper values to all fields')
            return render_template('template_friends.html',form=form,isLogged=True)


#lisätty 3.2.2016
@app.route('/logout')
def logout():
    #delete user session (clear all values)
    session.clear()
    return redirect('/')

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
