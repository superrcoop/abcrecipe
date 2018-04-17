from flask import Flask
from flask.ext.login import LoginManager
import MySQLdb 
import os,psycopg2


HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE='abcrecipe'
DATABASE_URL = os.environ['DATABASE_URL']
UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config.from_object(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = "strong"

app.config['SECRET_KEY'] = 'H@1lrAstAf@r1'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_UPLOADS'] = set(['jpg','png','jpeg'])

mysql = MySQLdb.connect(HOST, USER, PASSWORD ,DATABASE)

#postgres db connect
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

import views



