#importoidaa app-paketista objekti app
from app import app

print(__name__) #prints __main__ koska komentokehotteesta ohjelma käynnistetään: python run.py (tämä on main)
#28.1.2016
#if(__name__ == '__main__'):
#    app.run(debug=True)

app.run(debug=True)