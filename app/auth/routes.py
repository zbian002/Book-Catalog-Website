from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.catalog import main
from app.auth.models import User

@at.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()
    if current_user.is_authenticated:
        flash('you are already registered')
        return redirect(url_for('main.display_books'))
    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data)
        flash('Registration Successful')
        return redirect(url_for('authentication.do_the_login'))
    return render_template('registration.html', form=form)