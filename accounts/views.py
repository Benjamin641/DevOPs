from flask import Blueprint, render_template, flash, redirect, url_for
from accounts.forms import RegistrationForm
from models import User
from extensions import db

accounts_bp = Blueprint('accounts', __name__, template_folder='templates')


@accounts_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(
            email=form.email.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            phone=form.phone.data,
            password=form.password.data  # hash later
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Account Created', category='success')
        return redirect(url_for('accounts.login'))

    # GET request OR form validation failed
    return render_template('accounts/registration.html', form=form)


@accounts_bp.route('/login')
def login():
    return render_template('accounts/login.html')


@accounts_bp.route('/account')
def account():
    return render_template('accounts/account.html')