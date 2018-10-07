from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.catalog import main
from app.auth.models import User

@at.route('/register', methods=['GET', 'POST'])
def register_user():
    name = None
    email = None
    form = RegistrationForm()
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data

    return render_template('registration.html', form=form, email=email)