import os
from flask_mail import Message
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash ,session ,abort
from .forms import reg_Form,login_Form,upload_Form
from werkzeug.utils import secure_filename
from .controllers import get_uploaded_images, regexPassword, regexAlpha, regexEmail, regexUsername, allowed_file
from werkzeug.datastructures import CombinedMultiDict
from .models import account
from flask_login import login_user, logout_user, login_required, current_user

@login_manager.user_loader
def load_user(id):
    return account.query.get(int(id))

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
        email = form.email.data
        password = form.password.data
        if regexEmail(email) and regexPassword(password):
            user = account.query.filter_by(email = email).first()
            if user and user.is_correct_password(password): 
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('home'))
            else: 
                error = "Invalid email and/or password"
        else:
            error = "Invalid email and/or password"
    return render_template('login.html',error=error,form=form)

@app.route("/register",methods=['POST', 'GET'])
def register(): 
    error = None
    form = reg_Form()
    if request.method == 'POST' and form.validate_on_submit():
        first_name, last_name, email, password, conf_password, username = form.first_name.data, form.last_name.data, form.email.data, form.password.data, form.conf_password.data, form.username.data
        if regexEmail(email) and regexPassword(password) :
            if regexAlpha(first_name) and regexAlpha(last_name) and regexUsername(username):
                if not account.query.filter_by(email = email).first() and not account.query.filter_by(username = username).first():
                    user = account(username = username, first_name = first_name, last_name = last_name, email = email, plain_password = password)
                    db.session.add(user)
                    db.session.commit()
                    """
                    msg = Message("Hi "+user.first_name+", Thank you for registering at Stashit.website",
                    sender="stashit.no.reply@gmail.com",
                    recipients=[user.email])
                    msg.body="Your authentication code is: "+str(user.recoveryCode)
                    mail.send(msg)
                    """
                    return render_template('login.html', message="Success, You should receive an email with an authentication code", form = login_Form())
                else:
                    error = "Email and/or username already exists"
            else:
                error="Invalid Name and/or Username"
        else:
            error = "Invalid email and/or password. Password must be of length 8 contain at least 1 upper,lower alphanumeric character and character (a-z,A-Z,0-9,!@#\$%\^&\*)"
    return render_template('register.html', error=error, form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


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