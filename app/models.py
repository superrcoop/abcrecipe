import uuid , datetime , random , os ,errno
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from bcrypt import hashpw, gensalt
from . import db ,UPLOAD_FOLDER

def generate_id():
    return int(str(uuid.uuid4().int)[:8])

def generate_rcode():
    return int(str(uuid.uuid4().int)[:6])

def get_date():
    return datetime.datetime.now().today()

def generate_file_URI():
    URI=UPLOAD_FOLDER+'/'+str(uuid.uuid4().get_hex()[0:12])+'/'
    if not os.path.exists(URI):
        try:
            os.makedirs(URI)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    return URI

class account(db.Model, UserMixin):
	__tablename__ 	= 'account'
	id 				= db.Column(db.Integer, primary_key=True)
	username 		= db.Column(db.String(80), unique=True)
	email 			= db.Column(db.String(80), unique=True,nullable=False)
	_password		= db.Column(db.String(255),nullable=False)
	recoveryCode 	= db.Column(db.Integer,nullable=False)
	authenticated   = db.Column(db.Boolean,default=False,nullable=False)
	date_joined		= db.Column(db.Date,nullable=False)
	file_URI 		= db.Column(db.String(80),nullable=False)


	def __init__(self, username, email, plain_password, id=None):
		if id: 
			self.id 		= id
		else:
			self.id 		= generate_id()
		self.username 		= username
		self.email 			= email
		self.password 		= plain_password
		self.recoveryCode 	= generate_rcode()
		self.authenticated  = False
		self.date_joined    = get_date()
		self.file_URI       = generate_file_URI()

	def __repr__(self):
		return '<User %r>' % (self.username)

class person(db.Model):
	__tablename__ 	= 'person'
	id 				= db.Column(db.Integer, primary_key=True)
	first_name 		= db.Column(db.String(80))
	last_name 		= db.Column(db.String(80))



	def __init__(self,first_name, last_name, id=None):
		if id: 
			self.id 		= id
		else:
			self.id 		= generate_id()
		self.first_name 	= first_name 
		self.last_name 		= last_name


	def __repr__(self):
		return '<User %r>' % (self.username)