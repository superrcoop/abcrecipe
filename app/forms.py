from wtforms import StringField, PasswordField, FormField, IntegerField, SubmitField,SelectField,TextAreaField,FieldList, SelectMultipleField
from wtforms.validators import Required, Length, Email, EqualTo, DataRequired, Optional
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

class login_Form(FlaskForm):
    username = StringField('Username', validators=[Length(min=1,max=40,message=('Username does not satisfy condition ( 1 < name.length <= 40 )')),Required('Please provide a username')])
    password = PasswordField('Password', validators=[DataRequired('Enter password')])

class reg_Form(FlaskForm):
    first_name = StringField('First Name', validators=[Length(min=1,max=40,message=('First Name does not satisfy condition ( 1 < name.length <= 40 )')),Required('Please provide a First Name')])
    last_name = StringField('Last Name', validators=[Length(min=1,max=40,message=('Last Name does not satisfy condition ( 1 < name.length <= 40 )')),Required('Please provide a Last Name')])
    username = StringField('Username', validators=[Length(min=1,max=40,message=('Username does not satisfy condition ( 1 < name.length <= 40 )')),Required('Please provide a username')])
    email = StringField('Email Address', validators=[Email(message='Email not Valid'),Required('Please provide an email address')])
    password = PasswordField('Password',validators=[DataRequired('Enter a Password'),EqualTo('conf_password',message=('Passwords must Match'))])
    conf_password=PasswordField('ReEnter Password',validators=[DataRequired('Re-enter password')])
    phone = StringField('Phone number',validators=[DataRequired('Enter phone number')])
    diet =SelectField('Diet Type',choices=[('S','Select Diet'),('A','Atkins'),('N','Normal'), ('V','Vegetarian'),('Ve','Vegan')],validators=[Required('Enter your preferred diet')])
    health_info = TextAreaField('Health Information',validators=[Length(min=1,max=300,message=('First Name does not satisfy condition ( 1 < name.length <= 40 )')),DataRequired('Enter your medical information')])

class recipe_Form(FlaskForm):  
    name = StringField("Recipe Name",validators=[DataRequired('Enter a recipe_name')])
    calorie = IntegerField("Calories",validators=[DataRequired('Enter a calories')])
    servings = IntegerField("Serving",validators=[DataRequired('Enter serving')])
    prep_time = StringField("Preparation Time",validators=[DataRequired('Enter prep time')])
    cook_time = StringField("Cook Time",validators=[DataRequired('Enter cook time')])
    instruction1=StringField('Step 1',validators=[DataRequired('Enter step 1')])
    instruction2=StringField('Step 2',validators=[DataRequired('Enter step 2')])
    instruction3=StringField('Step 3',validators=[Optional()])
    instruction4=StringField('Step 4',validators=[Optional()])    
    diet_type =SelectField('Diet',choices=[('S','Select Diet'),('Atkins','Atkins'),('Normal','Normal'), ('Vegetarian','Vegetarian'),('Vegan','Vegan')],validators=[DataRequired('Enter preferred diet')])
    photo = FileField('files[]', validators=[FileRequired(),FileAllowed(ALLOWED_EXTENSIONS, 'File not allowed')])
    ingredients =SelectMultipleField('Ingredients',choices=[('S','Select ingredients'),('Apple','Apple'),('Banana','Banana'), ('Chicken','Chicken'),('Egg','Egg'),('Flour','Flour')],validators=[DataRequired('Enter ingredients')])
