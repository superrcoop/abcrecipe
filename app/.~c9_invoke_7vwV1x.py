from wtforms import StringField, PasswordField, HiddenField, BooleanField, IntegerField, SubmitField,
from wtforms.validators import Required, Length, Email, EqualTo, DataRequired
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed, FileRequired

ALLOWED_EXTENSIONS = set(['txt','pdf','png', 'jpg', 'jpeg', 'gif'])

class login_Form(FlaskForm):
    user_name = StringField('Username',validators=[DataRequired('Enter your username')])
    password = PasswordField('Password', validators=[DataRequired('Enter a password')])

class reg_Form(FlaskForm):
    first_name = StringField('First Name',validators=[DataRequired('Enter a firstname')])
    last_name = StringField('Last Name',validators=[DataRequired('Enter a lastname')])
    user_name = StringField('Username', validators=[DataRequired('Enter a username')])
    email = StringField('Email Address', validators=[Required()])
    password =  PasswordField('Password',validators=[Required()])
    conf_password= PasswordField('Re-enter password',validators=[Required()])
    phone = StringField('Phone',validators=[DataRequired('Enter phone number')])
    submit = SubmitField('Submit') 
    
    
class recipe_Form(FlaskForm):  
    recipe_name = StringField("Recipe Name",validators=[Required()])
    serving = StringField("Serving",validators=[Required()])
    prep_time = StringField("Preparation Time",validators=[Required()])
    cook_time = StringField("Cook Time",validators=[Required()])
    instruction1 = StringField("instruction",validators=[Required()])
    diettype = StringField("diet type",validators=[Required()])
    uploadedfile = FileField('Images', validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'])])

class upload_Form(FlaskForm):
    upload = FileField('files[]', validators=[FileRequired(),FileAllowed(ALLOWED_EXTENSIONS, 'File not allowed')])








































