"""app kansiosta haetaan objektia app"""
from app import app
#28.1.2016
#from app import run#tämä toimii, koska run.py:ssä oleva __name__ sisällöksi moduulin nimen missä se sijaitsee, eli se ei ole __main__
#render_template gives you access to Jinja2 template engine
#request objektista voidaan kaivaa kaikki mitä tulee BackEndiin (client lähettää)
from flask import render_template,request,make_response
from app.forms import LoginForm#28.1.2016 importtaa LoginForm luokka forms.py:stä

#tämä on myös tapa kommentoida, vain yhdelle riville
"""This is comment
    you can use multiple lines"""

#Routerin on aina palautettava vastaus

#kun pyyntö tulee serveriltä root kontekstiin, määritellään funktio index()
#@app => @ = decoration, käskee frameworkkia tekemään asialle jotain
@app.route('/',methods=['GET','POST'])
def index():
    login = LoginForm()
    return render_template('template_index.html',form=login)

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

print('This is not any more included in index() function')
#yllä oleva printataan komentoikkunaan