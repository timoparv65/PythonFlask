#importoidaa app-paketista objekti app
from app import app

print(__name__) #prints __main__ koska komentokehotteesta ohjelma käynnistetään: python run.py (tämä on main)

app.run(debug=True)