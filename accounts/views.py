from flask import Blueprint, render_template, flash, redirect, url_for
from accounts.forms import RegistrationForm
from models import User
from extensions import db
import logging

accounts_bp = Blueprint('accounts', __name__, template_folder='templates')
logger = logging.getLogger(__name__)

@accounts_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    logger.info("Registration page accessed")

    if form.validate_on_submit():
        logger.info(f"New registration attempt for email: {form.email.data}")
        new_user = User(
            email=form.email.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            phone=form.phone.data,
            password=form.password.data  # hash later
        )

        db.session.add(new_user)
        db.session.commit()

        logger.info(f"User successfully created: {form.email.data}")
        flash('Account Created', category='success')
        return redirect(url_for('accounts.login'))
    if form.errors:
        logger.warning(f"Registration validation failed: {form.errors}")

    # GET request OR form validation failed
    return render_template('accounts/registration.html', form=form)


@accounts_bp.route('/login')
def login():
    logger.info("login page accessed")
    return render_template('accounts/login.html')


@accounts_bp.route('/account')
def account():
    logger.info("Account page accessed")
    return render_template('accounts/account.html')