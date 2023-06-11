from flask import Blueprint, render_template, request, flash, redirect, url_for 
from flask_login import login_required, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user 
from flask import current_app

auth = Blueprint('auth',__name__) 

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.get_by_email(email)
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True, fresh=True) # Force a fresh login
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=__name__)

@auth.route('/logout')
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up(): 
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.get_by_email(email)
        if user: 
            flash('Email already exists.', category='error')
        
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else: 
            hashed_password = generate_password_hash(password1, method='sha256')
            new_user = User(id=id, email=email, password=hashed_password, first_name=first_name)
            new_user.save()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            #return redirect(url_for('views.home'))            
    
    return render_template("sign_up.html", user=current_user)


@auth.route('/delete', methods=['POST'])
@login_required
def delete_user():
    password = request.form.get('password')

    # Reload the user data from the database
    user_to_delete = User.get_by_id(current_user.id)
    login_user(user_to_delete, remember=True, fresh=True)

    if not check_password_hash(user_to_delete.password, password):
        flash('Incorrect password, try again', category='error')
        return redirect(url_for('views.home'))

    print("User to delete: ", user_to_delete) # Debugging statement

    if user_to_delete is not None:
        user_to_delete.delete()
        logout_user()
        flash('Your account has been deleted.', category='success')
    else:
        flash('User not found.', category='error')

    return redirect(url_for('auth.login'))


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
   if request.method == 'POST':
       old_password = request.form.get('current_password')
       new_password = request.form.get('new_password')
       confirm_password = request.form.get('new_password_confirm')


       if not old_password or not new_password or not confirm_password:
           flash('Please fill out all fields', category='error')
           return redirect(url_for('auth.change_password'))


       if new_password != confirm_password:
           flash('New passwords do not match', category='error')
           return redirect(url_for('auth.change_password'))


       if not check_password_hash(current_user.password, old_password):
           flash('Old password is incorrect', category='error')
           return redirect(url_for('auth.change_password'))


       new_password_hash = generate_password_hash(new_password, method='sha256')


       # You need to setup your database connection and put it into the app's config under the key 'DATABASE_CONNECTION'
       conn = current_app.config['DATABASE_CONNECTION']
       cur = conn.cursor()
       cur.execute("UPDATE users SET password = %s WHERE id = %s", (new_password_hash, current_user.id))
       conn.commit()


       flash('Password updated successfully', category='success')
       return redirect(url_for('views.home'))


   return render_template('change_password.html')

