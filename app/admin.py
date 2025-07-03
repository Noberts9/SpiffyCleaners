from flask import Blueprint, render_template
from flask_login import login_required
from flask import render_template, redirect, url_for, flash, request
from .models import ContactMessage, Booking
from . import db
from flask_login import login_required

admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
@login_required
def dashboard():
    bookings = Booking.query.order_by(Booking.timestamp.desc()).all()
    messages = ContactMessage.query.order_by(ContactMessage.timestamp.desc()).all()
    return render_template('admin/dashboard.html', bookings=bookings, messages=messages)

@admin.route('/delete-booking/<int:id>', methods=['POST'])
@login_required
def delete_booking(id):
    booking = Booking.query.get_or_404(id)
    db.session.delete(booking)
    db.session.commit()
    flash('Booking deleted.', 'success')
    return redirect(url_for('admin.dashboard'))

@admin.route('/mark-done/<int:id>', methods=['POST'])
@login_required
def mark_done(id):
    booking = Booking.query.get_or_404(id)
    booking.status = 'Completed'
    db.session.commit()
    flash('Booking marked as completed.', 'success')
    return redirect(url_for('admin.dashboard'))

@admin.route('/delete-message/<int:id>', methods=['POST'])
@login_required
def delete_message(id):
    message = ContactMessage.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    flash('Message deleted.', 'success')
    return redirect(url_for('admin.dashboard'))

@admin.route('/mark-denied/<int:id>', methods=['POST'])
@login_required
def mark_denied(id):
    booking = Booking.query.get_or_404(id)
    booking.status = 'Denied'
    db.session.commit()
    flash('Booking marked as denied.', 'warning')
    return redirect(url_for('admin.dashboard'))

