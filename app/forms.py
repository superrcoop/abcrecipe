from wtforms import StringField, PasswordField, FormField, IntegerField, SubmitField,SelectField,TextAreaField,FieldList, SelectMultipleField
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
    conf_password= PasswordField('Re-enter password',validators=[Required(),EqualTo('password',message=('Passwords must Match'))])
    phone = StringField('Phone',validators=[DataRequired('Enter phone number')])
    diet =SelectField('Diet',choices=[('S','Select Diet'),('A','Atkins'),('N','Normal'), ('V','Vegetarian'),('V2','Vegan')],validators=[DataRequired('Entered preferred diet')])
    health_info = TextAreaField('Health Information',validators=[DataRequired('Enter your medical information')])
    submit=SubmitField("Submit")

class instruction_Form(FlaskForm):
    instruction1=StringField('Step 1',validators=[Required()])
    instruction2=StringField('Step 2',validators=[Required()])
    instruction3=StringField('Step 3')
    instruction4=StringField('Step 4')
    instruction5=StringField('Step 5')

class recipe_Form(FlaskForm):  
    recipe_name = StringField("Recipe Name",validators=[Required()])
    calories = IntegerField("Calories",validators=[Required()])
    serving = IntegerField("Serving",validators=[Required()])
    prep_time = StringField("Preparation Time",validators=[Required()])
    cook_time = StringField("Cook Time",validators=[Required()])
    instructions = FieldList(FormField(instruction_Form), min_entries=1, validators=[Required()])
    diettype =SelectField('Diet',choices=[('S','Select Diet'),('A','Atkins'),('N','Normal'), ('V','Vegetarian'),('V2','Vegan')],validators=[DataRequired('Enter preferred diet')])
    uploadedfile = FileField('Upload image here', validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'])])
    ingredients = SelectMultipleField('ingredients', choices=[('S','Select'),('A','Apple'),('B','Banana'), ('C','Chickken'),('D','Date'),('E','Eggs')],validators=[DataRequired('Enter diet')])
    submit=SubmitField("Submit")
    
class ingredient_Form(FlaskForm):
    product_name = StringField('product_name',validators=[Required()])
    unit_name = SelectField('Unit',choices=[('S','Select Unit'),('C','Cup'),('Tbs','Tablespoon'), ('Q','Quart'),('G','Gallon')],validators=[DataRequired('Enter a unit')])
    calories_per_unit =  IntegerField('calories_per_unit',validators=[Required()])
    quantity = IntegerField('quantity',validators=[Required()])


