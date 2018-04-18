from wtforms import StringField, PasswordField, FormField, IntegerField, SubmitField,SelectField,TextAreaField,FieldList, SelectMultipleField
from wtforms.validators import Required, Length, Email, EqualTo, DataRequired, Optional
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from app import mysql

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
    diet =SelectField('Diet',choices=[('S','Select Diet'),('Atkins','Atkins'),('Normal','Normal'), ('Vegetarian','Vegetarian'),('Vegan','Vegan')],validators=[DataRequired('Enter preferred diet')])
    health_info = TextAreaField('Health Information',validators=[DataRequired('Enter your medical information')])
    submit=SubmitField("Submit")
    
class ingredient_Form(FlaskForm):
    product_name = StringField('product_name',validators=[Required()])
    unit_name = SelectField('Unit',choices=[('S','Select Unit'),('C','Cup'),('Tbs','Tablespoon'), ('Q','Quart'),('G','Gallon')],validators=[DataRequired('Enter a unit')])
    calories_per_unit =  IntegerField('calories_per_unit',validators=[Required()])
    quantity = IntegerField('quantity',validators=[Required()])

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
    # health_info = StringField('Health',validators=[DataRequired('Enter your health information')])
    photo= FileField('images', validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'], 'Only jpg,jpeg and png images can be uploaded')])
    submit=SubmitField("Submit")
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM Ingredients")
    result = cursor.fetchall()
    choices = [('S','Select ingredients')]
    for row in result:
        choices.append((str(int(row[0])), row[1])) #gvh
    # print choices
    # ingredients =SelectMultipleField('Ingredients',choices=[('S','Select ingredients'),('Apple','Apple'),('Banana','Banana'), ('Chicken','Chicken'),('Egg','Egg'),('Flour','Flour')],validators=[DataRequired('Enter ingredients')])
    ingredients =SelectMultipleField('Ingredients',choices=choices,validators=[DataRequired('Enter ingredients')])
    