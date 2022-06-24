import os
from app import ALLOWED_EXTENSIONS, allowed_file, app
from flask import flash, redirect, render_template, request, url_for
from app import db
from models import User
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import secure_filename


@app.route('/')
def base():
    name = 'base'
    return render_template('base.html',n=name)

@app.route('/about')
def about():
    name = 'О сайте'
    return render_template('about.html',n=name)

@app.route('/contactus')
def contactus():
    name = 'Контакты'
    return render_template('contactus.html',n=name)

@app.route('/login',methods=['GET','POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')
    if current_user.is_authenticated:
        return redirect('profile') 
    if request.method == 'POST':
        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password,password):
            rm = True if request.form.get('remainme') else False
            login_user(user,remember=rm)
            return redirect('profile')
        flash("Пароль або логін не існує",category='success')
    return render_template('login.html')


@app.route('/register',methods=['GET','POST'])
def register_page():
    login = request.form.get('login')
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    try:
        login_check = User.query.all()
        if request.method == 'POST':
            for i in login_check:
                if i.login == login:
                    flash("Користувач із таким ім'ям вже існує",category='success')
                elif i.email == email:
                    flash("Користувач із таким email вже існує",category='success')
            if not (login or password or password2):
                flash("Будь ласка, заповніть усі поля",category='success')
            elif password != password2:
                    flash('Два паролі не збігаються',category='success')
            else:
                hash_password = generate_password_hash(password)
                new_user = User(login=login, password=hash_password,email=email)
                db.session.add(new_user)
                db.session.commit()
    except:
        print('Ошибка')

    return render_template('register.html')

@app.route('/logout')
def logout_page():
    logout_user()
    flash("Ви вийшли з акаунту",category='success')
    return redirect('login')


@app.route('/profile')
@login_required
def profilee():
    # if not current_user.is_authenticated:
    #     return redirect('profile') 
    user_image = current_user.image
    print(user_image)
    return render_template('profile.html',user_image=user_image)

    
@app.route('/upload',methods=['GET','POST'])
@login_required
def upload():
    user_id = current_user.id
    file = request.files['file']
    filename = secure_filename(file.filename)
   
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user = User.query.get(user_id)
        user.image = file.filename
        db.session.commit()
    return redirect(url_for('profilee'))
    