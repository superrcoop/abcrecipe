import uuid
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from . import db 

def generate_id():
    return int(str(uuid.uuid4().int)[:8])
    
class User(db.Model):
	user_name = db.Column(db.String(255), unique=True,primary_key=True)
	password = db.Column(db.String(255))
	__tablename__ 	='User'
	    
	def __init__(self,user_name,password):
	    self.user_name=user_name
	    self.password=password
	    
	def is_authenticated(self):
	    return True
	  
	def is_active(self):
	    return True
	   
	def is_anonymous(self):
	    return False
	    
	def get_id(self):
	    return unicode(self.user_name)