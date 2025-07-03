from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TimeField
from wtforms.validators import DataRequired
from datetime import date, time
from wtforms import StringField, PasswordField, SubmitField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email,EqualTo, Length

class BookingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    service_type = SelectField('Service Type', choices=[
        ('house_cleaning', 'House Cleaning'),
        ('sofa_cleaning', 'Sofa Cleaning'),
        ('carpet_cleaning', 'Carpet Cleaning'),
        ('general_washing', 'General Washing')
    ], validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    date = DateField('Preferred Date', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Preferred Time', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Book Now')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')