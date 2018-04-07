from wtforms import StringField, PasswordField, HiddenField, BooleanField, IntegerField
from wtforms.validators import Required, Length, Email, EqualTo, DataRequired
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed, FileRequired

ALLOWED_EXTENSIONS = set(['txt','pdf','png', 'jpg', 'jpeg', 'gif'])

class login_Form(FlaskForm):
    email = StringField('Email Address', validators=[Email(message='Email not valid'), Length(min=6, max=60,message=('Email does not satisfy condition ( 6 < email.length <= 60 )')),Required('Please provide an email address')])
    password = PasswordField('Enter Password',validators=[DataRequired()])
    #accept_tos = BooleanField('Remember Me')

class reg_Form(FlaskForm):
    first_name = StringField('First Name', validators=[Length(min=1,max=40,message=('First Name does not satisfy condition ( 1 < name.length <= 40 )')),Required('Please provide a First Name')])
    last_name = StringField('Last Name', validators=[Length(min=1,max=40,message=('Last Name does not satisfy condition ( 1 < name.length <= 40 )')),Required('Please provide a Last Name')])
    username = StringField('Username', validators=[Length(min=1,max=40,message=('Username does not satisfy condition ( 1 < name.length <= 40 )')),Required('Please provide a username')])
    email = StringField('Email Address', validators=[Email(message='Email not Valid'),Required('Please provide an email address')])
    password = PasswordField('Enter Password',validators=[DataRequired('Enter a Password'),EqualTo('conf_password',message=('Passwords must Match'))])
    conf_password=PasswordField('Repeat Password',validators=[DataRequired('Re-enter password')])
    #recaptcha = RecaptchaField()

class upload_Form(FlaskForm):
    upload = FileField('files[]', validators=[FileRequired(),FileAllowed(ALLOWED_EXTENSIONS, 'File not allowed')])

