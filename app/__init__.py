from flask import Flask
from flask.ext.login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import MySQLdb


HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE='abcrecipe'

UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)
app.config['SECRET_KEY'] 						= 'H@1lrAstAf@r1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] 	= True
app.config['UPLOAD_FOLDER'] 					= UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/"+DATABASE
app.config['ALLOWED_UPLOADS'] = set(['jpg','png','jpeg'])

mysql = MySQLdb.connect(HOST, USER, PASSWORD ,DATABASE)

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.session_protection = 'strong'
login_manager.login_view = "login"

db = SQLAlchemy(app)
app.config.from_object(__name__)
import views



