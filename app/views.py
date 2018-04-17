import os
import time
from app import app,login_manager, mysql
from flask import Flask, abort, request, jsonify, url_for, render_template, redirect, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import login_Form,reg_Form,recipe_Form,ingredient_Form,instruction_Form
from models import User
from werkzeug.utils import secure_filename
from . import db

@app.route("/")
# @login_required
def index():
    error = None
    return render_template('index.html',error=error)

# @app.before_request
# def before_request():
#     # logout_user()
#     print current_user.is_authenticated

@app.route("/recipe_detail")
def recipe_detail():
    error = None
    return render_template('recipe_detail.html',error=error)

@app.route("/browse_recipe")
def browse_recipe():
    error = None
    return render_template('browse_recipe.html',error=error)

@app.route("/contact-us")
def contact():
    error = None
    return render_template('contact.html',error=error)

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    form = login_Form()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_name = form.user_name.data
            password = form.password.data
            try:
                cursor = mysql.cursor()
                cursor.execute('''select * from User where user_name="%s" and hash_password="%s"''' % (user_name , password))
                result = cursor.fetchall()
                if not result:
                     flash('Invalid login credentials')
                     return render_template('login.html', form=form)
                else:
                    user = User(result[0][0], result[0][1])
                    login_user(user)
                    flash('success')
                    return redirect(url_for('index'))
            except Exception as e:
                return str(e)
        else:
           return render_template('login.html' , form=form)
    else:
        return render_template('login.html', form=form)


@app.route("/register",methods=['GET','POST'])
def register():
    error=None
    form = reg_Form()
    if request.method == 'POST':   
        if form.validate_on_submit():
            first_name =  form.first_name.data
            last_name = form.last_name.data
            user_name = form.user_name.data
            email = form.email.data
            password = form.password.data
            conf_password =form.conf_password.data
            phone = form.phone.data
            # diet=form.diet.data
            # health_info=form.health_info.data
            diet="Normal"
            health_info="Good"
            try:
               
                insert_stmt = ("INSERT INTO User(user_name, hash_password) " "VALUES (%s, %s)")
                data  = (user_name, password)
                cursor = mysql.cursor()
                cursor.execute(insert_stmt,data)
                mysql.commit()
                cursor.close()
                
                try:
                    insert_profile(first_name,user_name,last_name,email,phone,diet,health_info)
                except Exception as e:
                    print e
                    db.session.rollback()
                    flash(str(e))
                    return render_template('register.html', error=error, form=form)
                
                user = User(user_name=user_name,hash_password=password)
                db.session.add(user)
                db.session.commit()

                flash('success')
                login_user(user)
                return redirect(url_for('index'))
            except Exception as e:
                print e
                db.session.rollback()
                flash(str(e))
                return render_template('register.html', error=error, form=form)
        else:
            flash('Error signing up')
            render_template('register.html' , error=error, form=form)
    else:
        return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    # Logout the user and end the session
    # session.pop('logged_in', None)
    logout_user()
    # flash('You have been logged out.', 'danger')
    return redirect(url_for('index'))
    
    
def insert_profile(first_name, user_name, last_name, email, phone, diet , health_info):
    insert_stmt = ("INSERT INTO Profile(first_name, user_name, last_name, email, phone, diet, health_info) " "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    data = (first_name, user_name, last_name, email, phone, diet , health_info)
    cursor = mysql.cursor()
    cursor.execute(insert_stmt,data)
    mysql.commit()
    cursor.close()
    
@app.route('/add_recipe', methods=['GET' , 'POST'])
@login_required
def add_recipe():
    form =recipe_Form()
    error=None
    print (form)
    if request.method == 'POST' :
        if form.validate_on_submit():
            recipe_name = form.recipe_name.data
            calorie = int(form.calorie.data)
            servings = int(form.servings.data)
            prep_time = form.prep_time.data
            cook_time = form.cook_time.data
            steps = form.instructions.data
            diet_type =form.diet_type.data
            images=request.files['images']
            if allowed_file(images.filename):
                filename=secure_filename(images.filename)
                images.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                flash('Incorrect File Format','danger')
                return redirect(url_for('profile'))
            
            instruction1 = steps[0]['instruction1']
            instruction2 = steps[0]['instruction2']
            instruction3 = steps[0]['instruction3']
            instruction4 = steps[0]['instruction4']
            instruction5 = steps[0]['instruction5']
            
            try:
               
                insert_stmt = ("INSERT INTO Recipe(name,calorie,servings,prep_time,cook_time,diet_type) " "VALUES (%s, %d, %d, %s, %s, %s)")
                data  = (recipe_name,calorie,servings,prep_time,cook_time,diet_type)
                cursor = mysql.cursor()
                cursor.execute(insert_stmt,data)
                mysql.commit()
                cursor.close()

                flash('success')
                return redirect(url_for('index'))
            except Exception as e:
                print e
                db.session.rollback()
                flash(str(e))
                return render_template('add_recipe.html',error=error,form=form)
        else:
            flash('Error adding recipe')
            return render_template('add_recipe.html',error=error,form=form)
    else:
            flash('Error posting')
            return render_template('add_recipe.html',error=error,form=form)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_UPLOADS']

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@login_manager.user_loader
def load_user(user_name):
    try:
        cursor = mysql.cursor()
        cursor.execute('''select * from User where user_name="%s"''' % (user_name))
        result = cursor.fetchall()
        if not result:
            return None
        user = User(result[0][0], result[0][1])
        return user
    except Exception as e:
        print str(e)
        return None
    
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(error):
    """Custom 500 page."""
    return render_template('500.html'), 500


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")