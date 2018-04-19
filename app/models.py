import uuid
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from . import db 

def generate_id():
    return int(str(uuid.uuid4().int)[:8])
    
class User(db.Model, UserMixin):
	user_name = db.Column(db.String(255), unique=True,primary_key=True)
	hash_password = db.Column(db.String(255))
	__tablename__ 	='User'
	    
	def __init__(self,user_name,hash_password):
	    self.user_name=user_name
	    self.hash_password=hash_password
	 
	def is_active(self):
	    return True

	def get_id(self):
	    return unicode(self.user_name)