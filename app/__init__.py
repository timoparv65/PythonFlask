#Kun python löytää __init__.py tiedoston app-kansiosta, Python tekee siitä paketin
# joka voidaan myöhemmin importata 

#alustetaan flask
from flask import Flask

#28.1.2016. Importoidaan paketista flask.ext.bootstrap luokka Bootstrap
from flask.ext.bootstrap import Bootstrap

# __name__ sisältää paketin nimen. __name__ sisältää myäs __main__:in (kts run.py). Luodaan app objekti
app = Flask(__name__)
#This line configures our app using the config.py file
app.config.from_object('config')

#28.1.2016. Luo bootstrap objekti
bootstrap = Bootstrap(app)

from app import routers