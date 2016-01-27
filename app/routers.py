"""app kansiosta haetaan objektia app"""
from app import app
#render_template gives you access to Jinja2 template engine
#request objektista voidaan kaivaa kaikki mitä tulee BackEndiin
from flask import render_template,request,make_response

#tämä on myös tapa kommentoida, vain yhdelle riville
"""This is comment
    you can use multiple lines"""

#kun pyyntö tulee serveriltä root kontekstiin, määritellään funktio index()
#@app => @ tarkoitta deklaraatiota, käskee frameworkkia tekemään asialle jotain
@app.route('/')
def index():
    name = 'Markus'
    address = 'Rautatienkatu'
    response = make_response(render_template('template_index.html',title=address,name=name))
    response.headers.add('Cache-Control','no-cache')
    return response
    #return render_template('template_index.html',title=address,name=name)#tokana toteutettu
    #return 'Hello World again with changes'# vaatii neljä välilyöntiä (kts Bracketsin oikea alareuna)#ekana toteutettu

#tämä ns. clean url
@app.route('/user/<name>')
def user(name):
    print(request.headers.get('User-Agent'))
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