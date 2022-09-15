from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('login.html', user=current_user)

    # Set form entries to variables 
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username already exists
    user = User.query.filter_by(username=username).first()
    if user:
        # Check if passwords match
        if check_password_hash(user.password, password):
            flash('Logged in successfully.', category='success')
            login_user(user, remember=True)
            return redirect('/')
        else:
            flash('Incorrect username or password.', category='error')
    else:
        flash('Invalid username', category='error')

    return redirect('/login')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':

        return render_template('register.html', user=current_user)

    # Get variables from form 
    username = request.form.get('username')
    password = request.form.get('password')
    confirmation = request.form.get('confirmation')

    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already exists, choose another!', category='error')

    # Check if info entered is acceptable 
    elif len(username) < 3:
        flash('Username must be greater than 2 characters.', category='error')
    elif username == "" or password == "" or confirmation == "":
        flash('Must fill all fields.', category='error')
    elif password != confirmation:
        flash('Passwords must match.', category='error')
    else:
        # Create new user with hashed password 
        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        # Add user to database 
        db.session.add(new_user)
        db.session.commit()

        # Log in user
        login_user(new_user, remember=True)
        flash('Account created!', category='success')

        return redirect(url_for('views.home'))

    return redirect('/register')