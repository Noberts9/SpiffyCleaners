from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import BookingForm, ContactForm
from .models import Booking
from . import db
from .forms import LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from .models import Admin
from .models import ContactMessage


main = Blueprint('main', __name__)

auth = Blueprint('auth', __name__)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = Admin.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin.dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('auth/login.html')

@main.route('/')
def home():
    contact_form = ContactForm()
    return render_template('index.html', form=contact_form) 

@main.route('/book-page', methods=['GET'])
def book_page():
    form = BookingForm()
    return render_template('book.html', form=form)

@main.route('/submit-booking', methods=['POST'])
def submit_booking():
    form = BookingForm()
    if form.validate_on_submit():
        booking = Booking(
            name=form.name.data,
            phone=form.phone.data,
            service_type=form.service_type.data,
            address=form.address.data,
            date=form.date.data,
            time=form.time.data
        )
        db.session.add(booking)
        db.session.commit()
        flash("Booking submitted!", "success")
        return redirect(url_for('main.home'))
    else:
        flash("All fields are required or invalid.", "danger")
        return redirect(url_for('main.book_page'))

@main.route('/contact', methods=['GET', 'POST'], endpoint='contact')
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(new_message)
        db.session.commit()
        flash('Message sent successfully!', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'POST':
        flash('All fields are required.', 'danger')
    return redirect(url_for('main.home'))
