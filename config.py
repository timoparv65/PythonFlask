# tiedostoa käytetään aplikaation konfaamiseen

# 29.1.20130
# seuraava SqlLiten importtaamiseksi. Kalvo s 59
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SERVER_NAME='localhost:3000'

# 29.1.2016. Käytetään token:in luontiin
SECRET_KEY = os.urandom(24)

#29.1.2016
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'data.db')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository') #db_repository = versionhallinta tietokannasta