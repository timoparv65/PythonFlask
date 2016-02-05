#29.1.2019
#tiedosto sisältää kuvauksen tietokannan mallista

# db määritelty __init__.py:ssä
from app import db
#4.2.2016 Kryptaus. Bcrypt on kohtuu turvallinen
from flask.ext.bcrypt import generate_password_hash

class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128),unique=True)
    passw = db.Column(db.String(128))
    #3.2.2016
    #2. tapa...jos ei 1.tapa määritellä routers.py (@app.route('/',methods=['GET','POST'])) miellytä
    #Relationship Friends-tauluun. Tekee automaattisen join:in Friends-tauluun
    #Hyvä, mutta on myös performance issue..jos ystäviä on paljon
    friends = db.relationship('Friends',backref='user',lazy='dynamic')
    def __init__(self,email,passw):# self => this pointteri, vertaa C++
        self.email = email
        #self.passw = passw
        self.passw = generate_password_hash(passw)#4.2.2016: Kryptataan salasana
    #4.2.2016 alla oleva ei toimi salauksen takia => generate_password_hash
    #def __str__(self):# 3.2.2016: Mitä palauttaa jos objekti viedään print() funktiolle
        #return self.email + ' ' + self.passw + ' ' + str(self.id)

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    age = db.Column(db.Integer)
    filename=db.Column(db.String,default='/static/images/TimoParviainen.jpeg')
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    #This is Friends constructor
    def __init__(self,name,address,age,user_id):
        self.name = name
        self.address = address
        self.age = age
        self.user_id = user_id
    def __str__(self):#3.2.2016: Mitä palauttaa jos objekti viedään print() funktiolle
        text = "This is friend object"
        return text