import os
import time
from app import app,login_manager, mysql
from flask import Flask, abort, request, jsonify, url_for, render_template, redirect, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import login_Form,reg_Form,recipe_Form
from models import User
from . import db
@app.route("/")
def index():
    error = None
    return render_template('index.html',error=error)

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
            diet=form.diet.data
            health_info=form.health_info.data
            try:
               
                insert_stmt = ("INSERT INTO User(user_name, hash_password) " "VALUES (%s, %s)")
                data  = (user_name, password)
                cursor = mysql.cursor()
                cursor.execute(insert_stmt,data)
                #mysql.commit()
                
                user = User(user_name=user_name,password=password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                
                #profile = Profile(username = username, firstName = first_name, lastName = last_name, email = email, phone=phone, diet="None", health_info="None")
                
                #insert_stmt = ("INSERT INTO Profile(first_name, user_name, last_name, email, phone, diet, health_info) " "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                #data = (first_name, user_name, last_name, email, phone, None, None)
                #cursor.excecute(insert_stmt,data)
                mysql.commit()
                flash('success')
                cursor.close()
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
    session.pop('logged_in', None)
    flash('You have been logged out.', 'danger')
    return redirect(url_for('index'))
    
@app.route('/add_recipe')
#@login_required
def add_recipe():
    form = recipe_Form()
    #if request.method=="POST":
    return render_template('add_recipe.html',form=form)


@app.route('/upload', methods=['POST', 'GET'])
@login_required
def upload_recipe():
    error,message=None,None
    form = upload_Form(CombinedMultiDict((request.files, request.form)))
    if request.method == 'POST' and form.validate_on_submit():
        file = form.upload.data
        if file.filename == '':
            error='No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_user.file_URI, filename))
        else:
             error='File not allowed'
        flash('File Saved', 'success')
    return render_template('upload.html',form=form,error=error)

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