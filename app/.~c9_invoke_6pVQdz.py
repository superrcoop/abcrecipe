import os
from app import app, db, login_manager, mysql
from flask import render_template, request, redirect, url_for, flash ,session ,abort,jsonify
from forms import reg_Form,login_Form,upload_Form,recipe_Form
from werkzeug.utils import secure_filename
from controllers import get_uploaded_images, regexPassword, regexAlpha, regexEmail, regexUsername, allowed_file
from werkzeug.datastructures import CombinedMultiDict
from models import User,Profile
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import create_engine

engine = create_engine('mysql://root:@localhost:3306/abcrecipe')

@login_manager.user_loader
def load_user(id):
    return Profile.query.get(int(id))

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

@app.route("/login",methods=['POST', 'GET'])
def login():
    error = None
    form = login_Form()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if regexEmail(username) and regexPassword(password):
            user = User.query.filter_by(username=username, password=password).first()
            if user is not None:
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for("home"))
            else:
                flash('Username or Password is incorrect.')  
    return render_template('login.html',error=error,form=form)

#I think this is done wrong
@app.route("/register",methods=['POST', 'GET'])
def register():
    form = reg_Form()
    if request.method == 'POST' :
        if form.validate_on_submit():
            first_name =  form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            conf_password =form.conf_password.data
            username = form.username.data
            phone = form.phone.data
            #user = User(username = username, password=password)
            insert_stmt = ("INSERT INTO User(user_name, hash_password) " "VALUES (%s, %s)")
            data  = (username, password)
            cursor = mysql.cursor()
            print ('Error')
            #profile = Profile(username = username, firstName = first_name, lastName = last_name, email = email, phone=phone, diet="None", health_info="None")
            insert_stmt = ("INSERT INTO Profile(first_name, user_name, last_name, email, phone, diet, health_info) " "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            data = (first_name, username, last_name, email, phone, None, None)
            cursor.excecute(insert_stmt,data)
            #db.session.add(user)
            #db.session.commit()  
            #db.session.add(profile)
            #db.session.commit()  
            return redirect(url_for('home'))
        else:
            flash('Error signing up')
            print ('Error')
            #render_template('register.html' , form=form)
    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/add_recipe')
@login_required
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