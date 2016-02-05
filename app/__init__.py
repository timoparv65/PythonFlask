#Kun python löytää __init__.py tiedoston app-kansiosta, Python tekee siitä paketin
# joka voidaan myöhemmin importata 

#alustetaan flask
from flask import Flask

#28.1.2016. Importoidaan paketista flask.ext.bootstrap luokka Bootstrap
from flask.ext.bootstrap import Bootstrap

#29.1.2019. SqLite tietokannan asetus. Kalvo 60
from flask.ext.sqlalchemy import SQLAlchemy

# __name__ sisältää paketin nimen. __name__ sisältää myäs __main__:in (kts run.py). Luodaan app objekti
app = Flask(__name__)
#This line configures our app using the config.py file
app.config.from_object('config')

#28.1.2016. Luo bootstrap objekti
bootstrap = Bootstrap(app)

#29.1.2019. SqLite tietokannan alustus, kalvo 60
db = SQLAlchemy(app)

#4.2.2016
from blueprint.ud.ud_blueprint import ud
#Register all needed blueprints
app.register_blueprint(ud)

from app import routers